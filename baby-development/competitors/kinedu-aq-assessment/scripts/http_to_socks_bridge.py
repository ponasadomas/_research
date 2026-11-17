#!/usr/bin/env python3
"""Local HTTP CONNECT proxy (127.0.0.1:8099) that relays through the NordVPN SOCKS5 proxy with auth.
Chrome cannot authenticate to SOCKS5 itself, so point Chrome at this bridge instead.
Credentials come from ~/.config/nordvpn-socks.env; never printed."""
import asyncio, os, struct, sys
env = {}
for line in open(os.path.expanduser('~/.config/nordvpn-socks.env')):
    if '=' in line: k, v = line.strip().split('=', 1); env[k] = v
USER, PASS = env['NORD_USER'].encode(), env['NORD_PASS'].encode()
SOCKS_HOST = os.environ.get('NORD_SOCKS_HOST', 'amsterdam.nl.socks.nordhold.net'); SOCKS_PORT = 1080
async def pipe(r, w):
    try:
        while True:
            d = await r.read(65536)
            if not d: break
            w.write(d); await w.drain()
    except Exception: pass
    finally:
        try: w.close()
        except Exception: pass
async def socks_connect(host, port):
    r, w = await asyncio.open_connection(SOCKS_HOST, SOCKS_PORT)
    w.write(b'\x05\x01\x02'); await w.drain()
    if (await r.readexactly(2)) != b'\x05\x02': raise RuntimeError('socks: no user/pass auth')
    w.write(b'\x01' + bytes([len(USER)]) + USER + bytes([len(PASS)]) + PASS); await w.drain()
    if (await r.readexactly(2))[1] != 0: raise RuntimeError('socks: auth failed')
    h = host.encode()
    w.write(b'\x05\x01\x00\x03' + bytes([len(h)]) + h + struct.pack('>H', port)); await w.drain()
    rep = await r.readexactly(4)
    if rep[1] != 0: raise RuntimeError(f'socks: connect failed {rep[1]}')
    if rep[3] == 1: await r.readexactly(6)
    elif rep[3] == 3: n = (await r.readexactly(1))[0]; await r.readexactly(n + 2)
    elif rep[3] == 4: await r.readexactly(18)
    return r, w
async def handle(cr, cw):
    try:
        line = await cr.readline()
        parts = line.decode(errors='replace').split()
        if len(parts) < 2 or parts[0] != 'CONNECT':
            cw.write(b'HTTP/1.1 405 Only CONNECT supported\r\nConnection: close\r\n\r\n'); await cw.drain(); cw.close(); return
        host, port = parts[1].rsplit(':', 1)
        while (await cr.readline()) not in (b'\r\n', b''): pass
        rr, rw = await socks_connect(host, int(port))
        cw.write(b'HTTP/1.1 200 Connection established\r\n\r\n'); await cw.drain()
        await asyncio.gather(pipe(cr, rw), pipe(rr, cw))
    except Exception as e:
        try: cw.write(b'HTTP/1.1 502 Bad Gateway\r\n\r\n'); await cw.drain(); cw.close()
        except Exception: pass
async def main():
    srv = await asyncio.start_server(handle, '127.0.0.1', int(os.environ.get('BRIDGE_PORT','8099')))
    print('bridge listening on 127.0.0.1:' + os.environ.get('BRIDGE_PORT','8099') + '  ->', SOCKS_HOST, flush=True)
    async with srv: await srv.serve_forever()
asyncio.run(main())
