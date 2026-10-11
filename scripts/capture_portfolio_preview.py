"""Capture the portfolio's actual Three.js scene as a six-second WebP loop.

Requires Python Playwright, Chromium, and ffmpeg. Serve the portfolio locally,
then run: python scripts/capture_portfolio_preview.py --url http://localhost:4173/
The capture-only hook makes ambient animations periodic; it never edits the site.
"""
import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--url', default='http://localhost:4173/')
parser.add_argument('--chromium', default='/usr/bin/chromium')
args = parser.parse_args()
assets = Path(__file__).resolve().parents[1] / 'assets'
fps, seconds = 20, 6

with tempfile.TemporaryDirectory(prefix='factory-preview-') as directory:
    frames = Path(directory)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=args.chromium, args=[
            '--no-sandbox', '--enable-webgl', '--use-angle=swiftshader',
            '--enable-unsafe-swiftshader',
        ])
        page = browser.new_page(viewport={'width': 1200, 'height': 600},
                                reduced_motion='reduce', device_scale_factor=1)

        def capture_scene(route):
            response = route.fetch()
            source = response.text()
            anchor = "window.dispatchEvent(new CustomEvent('factory-ready'"
            assert anchor in source, 'The portfolio scene changed; update the capture hook.'
            # Preserve the original amplitudes, matching their periods to the loop.
            for old, new in [('t*.45', 't*Math.PI/3'), ('t*.25', 't*Math.PI/3'),
                             ('t*.18', 't/6')]:
                assert old in source, f'Animation not found: {old}'
                source = source.replace(old, new)
            hook = """window.captureFactoryFrame=(value)=>{
              cancelAnimationFrame(raf);raf=0;paused=true;time=value;
              current=desired=0;overviewMix=0;draw(0);
            };\n  """
            route.fulfill(response=response, body=source.replace(anchor, hook + anchor))

        page.route('**/scene-*.js', capture_scene)
        page.goto(args.url, wait_until='networkidle')
        page.wait_for_function('typeof window.captureFactoryFrame === "function"')
        page.add_style_tag(content='''
            .site-header,.road-footer,#station-card,#object-tooltip,.skip-link
            {visibility:hidden!important}
        ''')
        page.mouse.move(0, 0)
        for frame in range(fps * seconds):
            page.evaluate('(t)=>window.captureFactoryFrame(t)', frame / fps)
            page.screenshot(path=str(frames / f'{frame:04d}.png'))
            if frame % fps == 0:
                print(f'Captured {frame}/{fps * seconds} frames', flush=True)
        browser.close()
    shutil.copyfile(frames / '0000.png', assets / 'factory-road.png')
    subprocess.run([
        'ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(fps),
        '-i', str(frames / '%04d.png'), '-c:v', 'libwebp_anim',
        '-quality', '88', '-compression_level', '6', '-loop', '0',
        str(assets / 'factory-road.webp'),
    ], check=True)
    for name in ('factory-road.webp', 'factory-road.png'):
        print(f'{name}: {(assets / name).stat().st_size:,} bytes')
