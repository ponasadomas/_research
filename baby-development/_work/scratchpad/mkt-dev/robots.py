import sys, urllib.robotparser, urllib.request
UA="Mozilla/5.0 (X11; Linux x86_64) Chrome/126"
for url in sys.argv[1:]:
    from urllib.parse import urlparse
    p=urlparse(url); r=f"{p.scheme}://{p.netloc}/robots.txt"
    try:
        req=urllib.request.Request(r,headers={"User-Agent":UA}); txt=urllib.request.urlopen(req,timeout=20).read().decode('utf-8','replace'); code=200
    except Exception as e:
        txt=""; code=getattr(e,'code',str(e))
    rp=urllib.robotparser.RobotFileParser(); rp.parse(txt.splitlines())
    res={ua:rp.can_fetch(ua,url) for ua in ["*","ClaudeBot","Claude-User","GPTBot","ChatGPT-User"]}
    print(code, url, res)
