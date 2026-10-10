"""Render self-contained GitHub profile SVGs and their accessible text version."""
from pathlib import Path
from html import escape
import textwrap

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    ('PLC AI Studio', 'AI-assisted PLC analysis & change review.', 'AI + RULES / IN DEVELOPMENT', None, '#bcb0ff'),
    ('Local LLM × LabVIEW', 'Natural-language tools for existing systems.', 'LOCAL AI / SYSTEM INTEGRATION', 'https://github.com/fortex66/local-llm-field-monitoring-agent', '#bcb0ff'),
    ('Manufacturing Process Optimization', 'Feedback-driven manufacturing improvement.', 'CONTROL / PROCESS ENGINEERING', None, '#e0b382'),
    ('Vision & Robot Alignment', 'Vision, robotics, and production integration.', 'VISION / ROBOTICS / MES', None, '#e0b382'),
    ('G90 · GV90 Programs', 'Project participation & process engineering.', 'AUTOMOTIVE / MANUFACTURING', None, '#e0b382'),
    ('Industrial Embedded Controllers', 'Industrial HMI and embedded control software.', 'C++ / QT / LINUX', None, '#7de2d8'),
    ('Water Treatment SCADA', 'Connected facilities and remote operation.', 'INDUSTRIAL MONITORING / CONTROL', 'https://fortex66.tistory.com/17', '#7de2d8'),
    ('ForTex-Viewer', 'PLC-connected monitoring and visualization.', 'PLC / WEB / DATA', 'https://github.com/fortex66/ForTex-Viewer', '#7de2d8'),
    ('EV Battery Management', 'Sensor-based energy monitoring and control.', 'ENERGY / EMBEDDED SYSTEMS', 'https://github.com/fortex66/Lithium-Ion-Battery-Management-System', '#7de2d8'),
    ('JourneyMate', 'Travel information and real-time collaboration.', 'WEB / REAL-TIME SERVICES', 'https://github.com/fortex66/JourneyMate', '#7de2d8'),
    ('SmartFarm', 'A trading platform for the smart-farm domain.', 'WEB / PHP / MYSQL', 'https://github.com/fortex66/SmartFarm', '#7de2d8'),
]

DEFS = '''<defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101a29"/><stop offset="1" stop-color="#090e18"/></linearGradient>
<linearGradient id="surface" x2="1" y2="1"><stop stop-color="#24354c"/><stop offset=".55" stop-color="#19273b"/><stop offset="1" stop-color="#111c2d"/></linearGradient>
<linearGradient id="edge" x2="0" y2="1"><stop stop-color="#25374d"/><stop offset="1" stop-color="#0d1624"/></linearGradient>
<linearGradient id="rim"><stop stop-color="#63849b" stop-opacity=".7"/><stop offset="1" stop-color="#25394c" stop-opacity=".3"/></linearGradient>
<filter id="shadow" x="-20%" y="-25%" width="150%" height="180%"><feGaussianBlur stdDeviation="8"/></filter>
<style>text{font-family:Arial,Helvetica,sans-serif}.mono{font-family:'Courier New',monospace}</style>
</defs>'''

def text(x, y, value, size=24, color='#d5e1ef', extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(value)}</text>'

def cube(x, y, color, scale=1):
    return f'''<g transform="translate({x} {y}) scale({scale})" stroke="{color}" stroke-linejoin="round">
<path d="M0 0L18 -9L36 0L18 9Z" fill="{color}" fill-opacity=".4"/>
<path d="M0 0V20L18 29V9Z" fill="{color}" fill-opacity=".18"/>
<path d="M18 9L36 0V20L18 29Z" fill="{color}" fill-opacity=".08"/>
</g>'''

def card(x, y, w, h, color):
    return f'''<rect x="{x+10}" y="{y+20}" width="{w-8}" height="{h}" rx="16" fill="#000" opacity=".42" filter="url(#shadow)"/>
<rect x="{x+7}" y="{y+12}" width="{w}" height="{h}" rx="16" fill="url(#edge)" stroke="#26394f"/>
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="url(#surface)" stroke="url(#rim)"/>
<path d="M{x+18} {y+1}H{x+w-18}" stroke="{color}" stroke-opacity=".5"/>
<path d="M{x+4} {y+24}V{y+h-24}" stroke="{color}" stroke-width="2" stroke-opacity=".5"/>'''

def panel(w, h, title, desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>', DEFS,
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="24" fill="url(#bg)" stroke="#283448"/>']

def write(name, parts):
    (ROOT/'assets'/name).write_text('\n'.join(parts+['</svg>'])+'\n')

def career(mobile=False):
    w,h = (700,640) if mobile else (1200,324)
    s=panel(w,h,'Profile — career & focus','SL Corporation, Production Technology Center, SA Team. Production technology software and control engineer, July 2025 to present. Previously industrial software development, October 2020 to June 2023. Major: 컴퓨터학부.')
    s += [text(40,48,'01 / PROFILE',16,'#9db1c9','class="mono" letter-spacing="2"'),text(40,95,'Grounded in the factory floor.',32,'#f0f4fa','font-weight="700"')]
    if mobile:
        layouts=[(32,124,624,150),(32,302,624,130),(32,460,624,120)]
    else:
        layouts=[(32,125,536,156),(594,125,300,156),(920,125,240,156)]
    x,y,cw,ch=layouts[0]
    s += [card(x,y,cw,ch,'#7de2d8'),cube(x+cw-66,y+33,'#7de2d8',.7),text(x+24,y+30,'CURRENT / 2025.07 — PRESENT',14 if not mobile else 19,'#7de2d8','class="mono"'),text(x+24,y+68,'SL Corporation',30,'#f0f4fa','font-weight="700"'),text(x+24,y+99,'Production Technology Center · SA Team',20 if not mobile else 24),text(x+24,y+130,'Production technology SW & control engineer',19 if not mobile else 23,'#9db1c9')]
    x,y,cw,ch=layouts[1]
    s += [card(x,y,cw,ch,'#e0b382'),text(x+24,y+30,'PREVIOUS / 2020–2023',14 if not mobile else 19,'#e0b382','class="mono"'),text(x+24,y+67,'Industrial software',23 if not mobile else 28,'#f0f4fa','font-weight="700"'),text(x+24,y+101,'Controllers · HMI · SCADA',19 if not mobile else 24,'#9db1c9')]
    x,y,cw,ch=layouts[2]
    s += [card(x,y,cw,ch,'#bcb0ff'),text(x+24,y+30,'MAJOR',14 if not mobile else 19,'#bcb0ff','class="mono"'),text(x+24,y+74,'컴퓨터학부',29 if not mobile else 32,'#f0f4fa','font-weight="700"')]
    write('profile-mobile.svg' if mobile else 'profile.svg',s)

def projects(mobile=False):
    w=700 if mobile else 1200
    columns=1 if mobile else 2
    rows=(len(PROJECTS)+columns-1)//columns
    ch=190 if mobile else 160
    step=ch+26
    h=128+rows*step+28
    desc='; '.join(p[0]+': '+p[1] for p in PROJECTS)
    s=panel(w,h,'Project collection — eleven projects',desc)
    s += [text(40,48,'02 / PROJECT COLLECTION',16,'#9db1c9','class="mono" letter-spacing="2"'),text(40,95,'Systems, from field to software.',32,'#f0f4fa','font-weight="700"')]
    for i,(name,summary,tag,url,color) in enumerate(PROJECTS):
        x=32 if mobile else 32+(i%2)*580
        y=124+(i//columns)*step
        cw=624 if mobile else 554
        s += [card(x,y,cw,ch,color),cube(x+cw-62,y+31,color,.65),text(x+26,y+30,f'{i+1:02d} / '+tag,16 if mobile else 12,color,'class="mono" letter-spacing=".4"')]
        title_size=29 if mobile else (23 if len(name)>29 else 27)
        s += [text(x+26,y+76,name,title_size,'#f0f4fa','font-weight="700"')]
        lines=textwrap.wrap(summary,width=43 if mobile else 48)
        for j,line in enumerate(lines):s.append(text(x+26,y+114+j*29,line,24 if mobile else 20,'#a8bbd1'))
        if i==0:s.append(text(x+26,y+ch-15,'PRIVATE REPOSITORY',13 if mobile else 11,'#8a9db5','class="mono"'))
    # An unnumbered closing tile balances the odd project count.
    if not mobile:
        x,y=612,124+(rows-1)*step
        s += [card(x,y,554,ch,'#7de2d8'),text(x+26,y+36,'ONE CONNECTED THREAD',13,'#7de2d8','class="mono" letter-spacing="1"'),text(x+26,y+83,'Equipment → Data → Decisions',25,'#f0f4fa','font-weight="700"'),text(x+26,y+122,'Built around engineering judgment.',20,'#a8bbd1')]
    write('projects-mobile.svg' if mobile else 'projects.svg',s)

def stack(mobile=False):
    w,h=(700,848) if mobile else (1200,412)
    s=panel(w,h,'Core stack & research direction','Control: PLC, LabVIEW, robotics, vision. Software: Python, C++, Qt, React, Node.js, SQL. AI integration: local LLMs, tool calling, rule-based validation. Research interest: knowledge-guided manufacturing AI, combining process data with engineering constraints.')
    s += [text(40,48,'03 / CAPABILITIES',16,'#9db1c9','class="mono" letter-spacing="2"'),text(40,95,'Three layers. One engineering mindset.',30 if mobile else 32,'#f0f4fa','font-weight="700"')]
    data=[('CONTROL / OT',['PLC · LabVIEW','Robotics · Vision'],'#e0b382'),('SOFTWARE / IT',['Python · C++ / Qt','React · Node.js · SQL'],'#7de2d8'),('AI INTEGRATION',['Local LLM · Tool calling','Rule-based validation'],'#bcb0ff')]
    for i,(title,lines,color) in enumerate(data):
        x=32 if mobile else 32+i*386
        y=124+i*170 if mobile else 124
        cw=624 if mobile else 362
        s += [card(x,y,cw,140,color),cube(x+cw-64,y+33,color,.7),text(x+26,y+32,title,20 if mobile else 16,color,'class="mono"')]
        for j,line in enumerate(lines):s.append(text(x+26,y+78+j*32,line,28 if mobile else 24,'#d5e1ef'))
    y=666 if mobile else 318
    s += [text(40,y,'RESEARCH INTEREST / KNOWLEDGE-GUIDED MANUFACTURING AI',16 if mobile else 17,'#bcb0ff','class="mono"'),text(40,y+38,'Process data + engineering constraints',25,'#f0f4fa','font-weight="600"'),text(40,y+70,'for human-centered decision support.',23,'#9db1c9')]
    write('stack-mobile.svg' if mobile else 'stack.svg',s)

def picture(stem,alt):
    return f'''<p align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="./assets/{stem}-mobile.svg" />
    <img src="./assets/{stem}.svg" width="100%" alt="{escape(alt,quote=True)}" />
  </picture>
</p>'''

def readme():
    original=(ROOT/'README.md').read_text()
    header=original[:original.index('</p>')+4]
    body=[header,'',picture('profile','Current: SL Corporation, Production Technology Center, SA Team — production technology SW & control engineer, Jul. 2025–Present. Previously industrial software development, Oct. 2020–Jun. 2023. Major: 컴퓨터학부.'),'',picture('projects','Eleven projects: '+', '.join(p[0] for p in PROJECTS)+'. Each project is summarized in a raised card.'),'',picture('stack','Core stack: control, industrial software, and AI integration. Research interest: knowledge-guided manufacturing AI.'),'', '''<p align="center">
  <a href="https://fortex66.github.io/">Portfolio</a> ·
  <a href="https://fortex66.tistory.com/">Tech blog</a> ·
  <a href="mailto:fortex66@naver.com">Email</a>
</p>

<details>
<summary>Text version & project links</summary>

**Current:** SL Corporation · Production Technology Center, SA Team — Production technology SW & control engineer (Jul. 2025–Present).<br/>
**Previously:** Industrial software development (Oct. 2020–Jun. 2023).<br/>
**Major:** 컴퓨터학부.
''']
    for i,(name,summary,tag,url,color) in enumerate(PROJECTS):
        label=f'[{name}]({url})' if url else name
        if i==0:summary+=' In development; private repository.'
        if name=='G90 · GV90 Programs':summary='G90 · GV90 프로젝트 참여 — process engineering.'
        if name=='Manufacturing Process Optimization':summary='제조 공정 최적화 기술 — feedback-driven process improvement.'
        body.append(f'- **{label}** — {summary}')
    body += ['', '**Core stack:** PLC · LabVIEW · Robotics · Vision / Python · C++ / Qt · React · Node.js · SQL / Local LLM · Tool calling · Rule-based validation.', '', '**Research interest:** Knowledge-guided manufacturing AI — process data and engineering constraints for human-centered decision support.', '', '</details>', '']
    (ROOT/'README.md').write_text('\n'.join(body))

if __name__=='__main__':
    for mobile in [False,True]:
        career(mobile);projects(mobile);stack(mobile)
    readme()
