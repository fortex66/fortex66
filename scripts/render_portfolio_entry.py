"""Build self-contained README cards from the generated 3D entrance artwork.

Run from any directory: python scripts/render_portfolio_entry.py
The embedded WebP keeps image-mode SVG independent of external resource loading.
"""
from base64 import b64encode
from pathlib import Path

assets = Path(__file__).resolve().parents[1] / 'assets'
art = b64encode((assets / 'portfolio-door.webp').read_bytes()).decode('ascii')
for mobile in (False, True):
    width, height = (420, 212) if mobile else (760, 204)
    x, headline, subtitle = (24, 29, 16) if mobile else (32, 32, 17)
    ix, iy, size = (294, 98, 110) if mobile else (518, 2, 198)
    for still in (False, True):
        suffix = ('-mobile' if mobile else '') + ('-still' if still else '')
        motion = '' if still else '''
    .entrance{animation:light 6s ease-in-out infinite}
    @keyframes light{0%,100%{filter:brightness(1)}50%{filter:brightness(1.13)}}
    @media(prefers-reduced-motion:reduce){.entrance{animation:none}}
'''
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Explore my work — The Factory Road</title>
  <desc id="desc">Robotics, software and applied AI. An open metal doorway with a blue-lit interior leads into my portfolio.</desc>
  <defs>
    <linearGradient id="background" x2="1" y2="1"><stop stop-color="#131e2d"/><stop offset="1" stop-color="#090e17"/></linearGradient>
    <radialGradient id="ambient"><stop stop-color="#4678b3" stop-opacity=".15"/><stop offset="1" stop-color="#4678b3" stop-opacity="0"/></radialGradient>
  </defs>
  <style>text{{font-family:Arial,Helvetica,sans-serif}}{motion}</style>
  <rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="12" fill="url(#background)" stroke="#2c3b4f"/>
  <ellipse cx="{ix+size*.58}" cy="{iy+size*.55}" rx="{size*.52}" ry="{size*.44}" fill="url(#ambient)"/>
  <text x="{x}" y="43" fill="#9aaec5" font-size="12" letter-spacing="2">THE FACTORY ROAD</text>
  <text x="{x}" y="94" fill="#f2f6fc" font-size="{headline}" font-weight="600">Explore my work <tspan fill="#9dc5ff">→</tspan></text>
  <text x="{x}" y="128" fill="#b1bdcd" font-size="{subtitle}">Robotics · Software · Applied AI</text>
  <text x="{x}" y="174" fill="#83a9dc" font-size="13">fortex66.github.io</text>
  <image class="entrance" x="{ix}" y="{iy}" width="{size}" height="{size}" xlink:href="data:image/webp;base64,{art}"/>
</svg>
'''
        path = assets / f'portfolio-entry-3d{suffix}.svg'
        path.write_text(svg)
        print(f'{path.name}: {path.stat().st_size:,} bytes')
