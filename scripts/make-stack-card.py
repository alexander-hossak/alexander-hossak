"""Make assets/stack-{light,dark}.svg from the certdirectory stack card, without the name line.

certdirectory draws "MY STACK", then the name, then the icons. This script removes
the name, moves the rest up and sets the title to "My stack". Run it again when the
stack on certdirectory changes: python3 scripts/make-stack-card.py
"""
import re
import urllib.request
from pathlib import Path

URL = "https://certdirectory.io/badge/stack/frederik-hossak.svg"
SHIFT = 38  # vertical space the name line used

out = Path(__file__).resolve().parent.parent / "assets"
for theme, query in (("light", ""), ("dark", "?theme=dark")):
    req = urllib.request.Request(URL + query, headers={"User-Agent": "curl/8"})
    svg = urllib.request.urlopen(req, timeout=30).read().decode()
    paths = [m for m in re.finditer(r"<path [^>]*/>", svg)]
    name = paths[1]  # path 0 is the "MY STACK" label, path 1 is the name
    assert 50 < float(re.search(r'd="M[\d.]+ ([\d.]+)', name.group()).group(1)) < 80, "layout changed"
    head, tail = svg[: name.start()], svg[name.end() :]
    tail = tail.replace("</svg>", "</g></svg>")
    svg = head + f'<g transform="translate(0,-{SHIFT})">' + tail

    h = int(re.search(r'height="(\d+)"', svg).group(1))
    svg = re.sub(r'height="\d+" viewBox="0 0 (\d+) \d+"', lambda m: f'height="{h - SHIFT}" viewBox="0 0 {m.group(1)} {h - SHIFT}"', svg, count=1)
    svg = re.sub(r'(<rect x="\.5" y="\.5" width="\d+" height=")(\d+)"', lambda m: f'{m.group(1)}{int(m.group(2)) - SHIFT}"', svg, count=1)
    svg = re.sub(r'aria-label="[^"]*"', 'aria-label="My stack"', svg, count=1)
    svg = re.sub(r"<title>[^<]*</title>", "<title>My stack</title>", svg, count=1)

    f = out / f"stack-{theme}.svg"
    f.write_text(svg)
    print(f, len(svg), "bytes")
