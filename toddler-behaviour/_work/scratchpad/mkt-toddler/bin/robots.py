#!/usr/bin/env python3
"""robots.py <url>... : print HTTP status of robots.txt, AI-crawler groups, and whether '*' allows the path."""
import sys, subprocess, urllib.parse, urllib.robotparser
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
AI=["GPTBot","ClaudeBot","anthropic-ai","Claude-Web","CCBot","Google-Extended","ChatGPT-User","Claude-User","PerplexityBot"]
for url in sys.argv[1:]:
    u=urllib.parse.urlparse(url); r=f"{u.scheme}://{u.netloc}/robots.txt"
    p=subprocess.run(["curl","-sS","-L","--max-time","20","-A",UA,"-w","\n%{http_code}",r],capture_output=True,text=True)
    body,_,code=p.stdout.rpartition("\n")
    rp=urllib.robotparser.RobotFileParser(); rp.parse(body.splitlines() if code=="200" else [])
    bans=[a for a in AI if not rp.can_fetch(a,url)]
    print(f"{u.netloc}{u.path} robots={code} star_ok={rp.can_fetch('*',url)} ai_banned={bans}")
