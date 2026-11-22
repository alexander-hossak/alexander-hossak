"""Generate assets/header.svg: a low-poly banner with an animated tagline.

Run: python3 scripts/make-header.py
Deterministic (fixed seed), so the output only changes when this file changes.
"""
import random
from pathlib import Path

W, H = 1280, 300
COLS, ROWS = 22, 7
random.seed(1991)

# Jittered grid; edge points stay on the border so the mesh fills the frame.
pts = []
for r in range(ROWS + 1):
    row = []
    for c in range(COLS + 1):
        x, y = c * W / COLS, r * H / ROWS
        if 0 < c < COLS:
            x += random.uniform(-0.35, 0.35) * W / COLS
        if 0 < r < ROWS:
            y += random.uniform(-0.35, 0.35) * H / ROWS
        row.append((x, y))
    pts.append(row)


def colour(cx, cy):
    # Dark navy on the left (text area), brighter cyan-blue to the right.
    t = max(0.0, (cx / W - 0.30) / 0.70)
    j = random.uniform(-0.06, 0.06)
    t = min(1.0, max(0.0, t + j))
    a = (13, 17, 35)    # #0d1123
    b = (33, 80, 209)   # #2150d1
    c = (0, 190, 255)   # #00beff
    lo, hi, k = (a, b, t / 0.6) if t < 0.6 else (b, c, (t - 0.6) / 0.4)
    rgb = [round(lo[i] + (hi[i] - lo[i]) * k) for i in range(3)]
    return "#%02x%02x%02x" % tuple(rgb)


tris = []
for r in range(ROWS):
    for c in range(COLS):
        p00, p10 = pts[r][c], pts[r][c + 1]
        p01, p11 = pts[r + 1][c], pts[r + 1][c + 1]
        for tri in ((p00, p10, p11), (p00, p11, p01)) if random.random() < 0.5 else ((p00, p10, p01), (p10, p11, p01)):
            cx = sum(p[0] for p in tri) / 3
            cy = sum(p[1] for p in tri) / 3
            d = " ".join(f"{x:.1f},{y:.1f}" for x, y in tri)
            col = colour(cx, cy)
            tris.append(f'<polygon points="{d}" fill="{col}" stroke="{col}" stroke-width="0.8"/>')

LINES = [
    "Kubernetes platforms that are secure by default.",
    "SRE work, done forward-deployed.",
    "AI agents and LLM infrastructure I run myself.",
]
n = len(LINES)
period = 4 * n  # seconds; each line shows for 4 s
keyframes = []
tagline = []
for i, line in enumerate(LINES):
    s, e = 100 * i / n, 100 * (i + 1) / n
    keyframes.append(
        f"@keyframes l{i}{{0%,{s:.2f}%{{opacity:0;clip-path:inset(0 100% 0 0)}}"
        f"{s + 0.01:.2f}%{{opacity:1;clip-path:inset(0 100% 0 0)}}"
        f"{s + 100 / n * 0.35:.2f}%{{opacity:1;clip-path:inset(0 0 0 0)}}"
        f"{e - 100 / n * 0.08:.2f}%{{opacity:1;clip-path:inset(0 0 0 0)}}"
        f"{e:.2f}%,100%{{opacity:0;clip-path:inset(0 0 0 0)}}}}"
        f".l{i}{{animation:l{i} {period}s linear infinite}}"
    )
    tagline.append(f'<text class="tag l{i}" x="64" y="214">{line}</text>')

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Frederik Hossak. Kubestronaut, platform engineer, AI-native.">
<title>Frederik Hossak · Kubestronaut · Platform Engineer · AI-native</title>
<defs>
<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#0d1123" stop-opacity="0.92"/><stop offset="0.55" stop-color="#0d1123" stop-opacity="0.55"/><stop offset="1" stop-color="#0d1123" stop-opacity="0"/></linearGradient>
<clipPath id="r"><rect width="{W}" height="{H}" rx="14"/></clipPath>
<style>
text{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}}
.name{{font-size:64px;font-weight:700;fill:#ffffff;letter-spacing:-1px}}
.role{{font-size:24px;font-weight:500;fill:#9ecbff}}
.tag{{font-size:22px;fill:#e6edf3;opacity:0}}
{"".join(keyframes)}
</style>
</defs>
<g clip-path="url(#r)">
{"".join(tris)}
<rect width="{W}" height="{H}" fill="url(#fade)"/>
<text class="name" x="60" y="122">Frederik Hossak</text>
<text class="role" x="64" y="164">Kubestronaut · Platform &amp; SRE Engineer · AI-native</text>
{"".join(tagline)}
</g>
</svg>
"""

out = Path(__file__).resolve().parent.parent / "assets" / "header.svg"
out.parent.mkdir(exist_ok=True)
out.write_text(svg)
print(out, len(svg), "bytes")
