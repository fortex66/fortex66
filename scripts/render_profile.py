"""Render self-contained GitHub profile SVGs and their accessible text version."""
from pathlib import Path
from html import escape
from hashlib import sha256
import textwrap

ROOT = Path(__file__).resolve().parents[1]
ASSETS = {}
PROJECTS = [
    ('PLC AI Studio', 'AI-assisted PLC analysis & change review.', 'AI + RULES / IN DEVELOPMENT', None, '#bcb0ff'),
    ('Local LLM × LabVIEW', 'Natural-language tools for existing systems.', 'LOCAL AI / SYSTEM INTEGRATION', 'https://github.com/fortex66/local-llm-field-monitoring-agent', '#bcb0ff'),
    ('Manufacturing Process Optimization', 'Feedback-driven manufacturing improvement.', 'CONTROL / PROCESS ENGINEERING', None, '#e0b382'),
    ('Vision & Robot Alignment', 'Vision, robotics, and production integration.', 'VISION / ROBOTICS / MES', None, '#e0b382'),
    ('G90 · GV90 Programs', 'Project participation & process engineering.', 'AUTOMOTIVE / MANUFACTURING', None, '#e0b382'),
    ('Industrial Embedded Controllers', 'Industrial HMI and embedded control software.', 'C++ / QT / LINUX', None, '#7de2d8'),
    ('Water Treatment SCADA', 'Connected facilities and remote operation.', 'INDUSTRIAL MONITORING / CONTROL', 'https://github.com/fortex66/Water-Treatement-SCADA', '#7de2d8'),
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
    content='\n'.join(parts+['</svg>'])+'\n'
    # GitHub's raw images may remain cached after a merge. A content-derived
    # filename gives every changed identity image a new, immutable URL.
    filename=name
    if name.startswith('architecture'):
        digest=sha256(content.encode()).hexdigest()[:12]
        filename=f'{Path(name).stem}-{digest}.svg'
    ASSETS[name]=filename
    (ROOT/'assets'/filename).write_text(content)

def asset(stem):
    name=stem+'.svg'
    return './assets/'+ASSETS.get(name,name)

def architecture(mobile=False, animated=True):
    """An exploded isometric structure, with career as its foundation."""
    w,h = (700,1320) if mobile else (1200,930)
    s=panel(w,h,'Engineering identity — control, software, and AI',
        'A conceptual map of my engineering identity: industrial control feeds connected software and structured data; AI supports interpretation and human decisions. Current: SL Corporation, Production Engineering Center, July 2025 to present. Previous: Automation Company, Software Developer, October 2020 to June 2023. Education: Bachelor’s Degree, Computer Science, March 2018 to February 2025. Research interest: knowledge-guided manufacturing AI.')
    if animated:
        s.append('''<style>
.float-ai{animation:float 6s ease-in-out infinite}
.float-it{animation:float 7s ease-in-out -2s infinite}
.float-ot{animation:float 8s ease-in-out -4s infinite}
.robot-arm{animation:reach 8s ease-in-out infinite}
.data-flow{stroke-dasharray:4 14;animation:flow 5s linear infinite}
.live-node{animation:pulse 4s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes reach{0%,100%{transform:rotate(0deg);transform-origin:28px 55px}50%{transform:rotate(-8deg);transform-origin:28px 55px}}
@keyframes flow{to{stroke-dashoffset:-72}}
@keyframes pulse{0%,100%{opacity:.55}50%{opacity:1}}
@media(prefers-reduced-motion:reduce){.float-ai,.float-it,.float-ot,.robot-arm,.data-flow,.live-node{animation:none}}
</style>''')
    s += [text(40,48,'01 / ENGINEERING IDENTITY',16,'#9db1c9','class="mono" letter-spacing="2"'),text(40,95,'Manufacturing software engineer.',31 if mobile else 36,'#f0f4fa','font-weight="700"')]
    cx=200 if mobile else 330
    half=140 if mobile else 210
    depth=55 if mobile else 75
    ys=[240,415,590] if mobile else [225,380,535]
    colors=['#bcb0ff','#7de2d8','#e0b382']
    # Vertical feedback spine connects layers rather than isolating capabilities.
    spine=28 if mobile else 72
    s.append(f'<path class="data-flow" d="M{spine} {ys[2]}V{ys[0]}" fill="none" stroke="#7f99b1" stroke-width="2" stroke-dasharray="4 7"/>')
    for cy in ys:s.append(f'<path d="M{spine} {cy}H{cx-half}" stroke="#52687f"/>')
    s += [text(spine+7,ys[0]-18,'↑',26,'#7de2d8'),text(spine+7,ys[2]+35,'↓',26,'#7de2d8')]
    for index in [2,1,0]:
        cy,color=ys[index],colors[index]
        # The bevel and rear face establish thickness, instead of stacked rectangles.
        s.append(f'<ellipse cx="{cx+8}" cy="{cy+depth+24}" rx="{half-35}" ry="20" fill="#000" opacity=".4" filter="url(#shadow)"/>')
        s.append(f'<path d="M{cx-half} {cy}L{cx} {cy+depth}L{cx+half} {cy}V{cy+22}L{cx} {cy+depth+22}L{cx-half} {cy+22}Z" fill="url(#edge)" stroke="#40576e"/>')
        s.append(f'<path d="M{cx-half} {cy}L{cx} {cy-depth}L{cx+half} {cy}L{cx} {cy+depth}Z" fill="url(#surface)" stroke="{color}" stroke-opacity=".8"/>')
        s.append(f'<path d="M{cx-half+8} {cy+10}L{cx} {cy+depth+9}L{cx+half-8} {cy+10}" fill="none" stroke="{color}" stroke-opacity=".65" stroke-width="2"/>')
        # Grid etched into each slab is an engineering motif, not extra decoration.
        for t in [-.5,0,.5]:
            x1=cx-half/2+t*half/2;y1=cy-depth/2-t*depth/2
            x2=cx+half/2+t*half/2;y2=cy+depth/2-t*depth/2
            s.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-opacity=".12"/>')
        size=1 if mobile else 1.2
        s.append(f'<g class="float-{["ai","it","ot"][index]}"><g transform="translate({cx-36*size} {cy-38*size}) scale({size})" stroke-linejoin="round">')
        if index==0:
            s.append('''<path d="M0 12L36 -6L72 12L36 30Z" fill="#a69bff" fill-opacity=".35" stroke="#d0c5ff"/>
<path d="M0 12V51L36 69V30Z" fill="#8b7dde" fill-opacity=".25" stroke="#a99cee"/>
<path d="M36 30L72 12V51L36 69Z" fill="#574693" fill-opacity=".3" stroke="#a99cee"/>
<path d="M17 28L36 17L56 29L52 49L36 58L20 47Z M17 28L52 49L36 17L20 47L56 29L36 58Z" fill="none" stroke="#e0d8ff" stroke-width="1.5"/>''')
            for x,y in [(17,28),(36,17),(56,29),(52,49),(36,58),(20,47)]:s.append(f'<circle class="live-node" cx="{x}" cy="{y}" r="2.8" fill="#ece7ff"/>')
        elif index==1:
            s.append('''<path d="M1 12L30 -3L67 15L38 30Z" fill="#547d88" stroke="#9ad9dd"/>
<path d="M1 12V61L38 79V30Z" fill="#213f4d" stroke="#6599a6"/>
<path d="M38 30L67 15V64L38 79Z" fill="#142937" stroke="#6599a6"/>
<path d="M9 29L30 39M9 43L30 53M9 57L30 67" stroke="#8dbecb" stroke-width="2"/>
<path d="M51 38L82 22V60L51 76Z" fill="#132b38" stroke="#7de2d8"/>
<path class="live-node" d="M56 65L61 53L66 56L74 40L78 43" fill="none" stroke="#7de2d8" stroke-width="2"/>''')
        else:
            s.append('''<path d="M7 65L35 51L64 65L35 79Z" fill="#c08f5c" stroke="#eacba4"/>
<path d="M7 65V72L35 86V79Z" fill="#8a5f3b"/><path d="M35 79L64 65V72L35 86Z" fill="#543c2a"/>
<g class="robot-arm">
<path d="M32 59L18 29L44 4L67 20" fill="none" stroke="#67482e" stroke-width="17" stroke-linecap="round"/>
<path d="M28 55L14 25L40 0L64 16" fill="none" stroke="#d4a36e" stroke-width="13" stroke-linecap="round"/>
<path d="M65 17L75 23L77 34M75 23L86 19L89 29" fill="none" stroke="#b8c6d5" stroke-width="4" stroke-linecap="round"/>''')
            for x,y in [(28,55),(14,25),(40,0)]:s.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#e0b382" stroke="#f4d4ad"/><circle cx="{x}" cy="{y}" r="3" fill="#725139"/>')
            s.append('</g>')
        s.append('</g></g>')
        s.append(text(cx,cy+depth+17,['AI','IT','OT'][index],13,color,'class="mono" text-anchor="middle" letter-spacing="4"'))
        lx=380 if mobile else 640
        end=lx-16
        s.append(f'<path d="M{cx+half} {cy}H{end}" fill="none" stroke="{color}" stroke-opacity=".5"/>')
        s.append(f'<path class="data-flow" d="M{cx+half} {cy}H{end}" fill="none" stroke="{color}" stroke-width="2"/>')
        s.append(f'<circle class="live-node" cx="{end}" cy="{cy}" r="3" fill="{color}"/>')
        title=['INTERPRET & ASSIST','CONNECT & STRUCTURE','OBSERVE & CONTROL'][index]
        s += [text(lx,cy-46,['03 / INTELLIGENCE','02 / SOFTWARE','01 / CONTROL'][index],14 if mobile else 16,color,'class="mono" letter-spacing=".6"'),text(lx,cy-9,title,21 if mobile else 28,'#f0f4fa','font-weight="700"')]
        tools=([['Local LLM · Tool calling','Rules · Human review'],['Python · C++ / Qt','React · Node.js · SQL'],['PLC · LabVIEW · Robotics','Vision · Process engineering']][index])
        if mobile:
            tools=[['Local LLM · Tool calling','Rules · Human review'],['Python · C++ / Qt','React · Node.js · SQL'],['PLC · LabVIEW','Robotics · Vision']][index]
        for j,line in enumerate(tools):s.append(text(lx,cy+28+j*31,line,20 if mobile else 25,'#9db1c9'))
    ry=725 if mobile else 668
    s += [text(40,ry,'RESEARCH / KNOWLEDGE-GUIDED MANUFACTURING AI',16,'#bcb0ff','class="mono"'),text(40,ry+36,'Process knowledge + data + engineering constraints',22 if mobile else 28,'#d5e1ef','font-weight="600"')]
    fy=810 if mobile else 755
    s += [f'<path d="M40 {fy}H{w-40}" stroke="#2d4256"/>',text(40,fy+31,'EXPERIENCE / THE FOUNDATION',14,'#9db1c9','class="mono" letter-spacing="1.2"')]
    foundation=[
        ('SL Corporation','Production Engineering Center','2025.07 — PRESENT','#7de2d8'),
        ('Automation Company','Software Developer','2020.10 — 2023.06','#e0b382'),
        ('Bachelor’s Degree','Computer Science','2018.03 — 2025.02','#bcb0ff'),
    ]
    # Three equal-width columns, with matching title and detail baselines.
    # Narrow screens use equally spaced rows at a readable type size.
    column_width=(w-80-64)/3
    for i,(title,detail,dates,color) in enumerate(foundation):
        x=40 if mobile else 40+i*(column_width+32)
        y=fy+73+(i*150 if mobile else 0)
        s += [text(x,y,title,30 if mobile else 28,'#f0f4fa','font-weight="700"'),
              text(x,y+35,detail,24 if mobile else 20,color)]
        if dates:s.append(text(x,y+66,dates,16,'#9db1c9','class="mono"'))
        if i<2:
            if mobile:
                s.append(f'<path d="M40 {y+99}H{w-40}" stroke="#2d4256"/>')
            else:
                divider=x+column_width+16
                s.append(f'<path d="M{divider} {fy+57}V{fy+150}" stroke="#2d4256"/>')
    stem='architecture-mobile' if mobile else 'architecture'
    write(stem+('' if animated else '-static')+'.svg',s)

def projects(mobile=False):
    w=700 if mobile else 1200
    columns=1 if mobile else 2
    rows=(len(PROJECTS)+columns-1)//columns
    ch=190 if mobile else 160
    step=ch+26
    h=128+rows*step+28
    desc='; '.join(p[0]+': '+p[1] for p in PROJECTS)
    s=panel(w,h,'Project collection — eleven projects',desc)
    s += [text(40,48,'02 / PROJECT ARCHIVE',16,'#9db1c9','class="mono" letter-spacing="2"'),text(40,95,'Systems, from field to software.',32,'#f0f4fa','font-weight="700"')]
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

CONTACTS = [
    ('portfolio', 'Portfolio', 'fortex66.github.io', 'https://fortex66.github.io/', '#bcb0ff'),
    ('blog', 'Tech Blog', 'fortex66.tistory.com', 'https://fortex66.tistory.com/', '#7de2d8'),
    ('email', 'Email', 'fortex66@naver.com', 'mailto:fortex66@naver.com', '#e0b382'),
]

def contacts():
    """Separate image buttons keep all three destinations clickable on GitHub."""
    for stem,label,address,url,color in CONTACTS:
        s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="380" height="180" viewBox="0 0 380 180" role="img" aria-labelledby="title desc">',
           f'<title id="title">{escape(label)}</title><desc id="desc">Open {escape(address)}.</desc>',DEFS,card(8,8,352,144,color)]
        # Beveled isometric pedestal with a distinct symbol for each destination.
        s += [f'<path d="M27 93L58 78L89 93V105L58 121L27 105Z" fill="url(#edge)" stroke="{color}" stroke-opacity=".5"/>',
              f'<path d="M27 93L58 78L89 93L58 109Z" fill="url(#surface)" stroke="{color}"/>',
              f'<g stroke="{color}" stroke-width="2" stroke-linejoin="round">']
        if stem=='portfolio':
            s += ['<path d="M33 54L61 40L83 51V85L55 99L33 88Z" fill="#232e49"/>',
                  '<path d="M33 54L55 65L83 51M55 65V99" fill="none"/>',
                  '<path d="M61 61L75 54M61 72L75 65M61 83L70 78" fill="none"/>']
        elif stem=='blog':
            s += ['<path d="M31 55L54 65L80 52V86L54 99L31 89Z" fill="#193b46"/>',
                  '<path d="M54 65V99M36 65L48 71M36 74L48 80M61 70L74 63M61 79L74 72" fill="none"/>']
        else:
            s += ['<path d="M32 62L80 39V77L32 100Z" fill="#423326"/>',
                  '<path d="M32 62L56 70L80 39M32 100L49 76M80 77L63 67" fill="none"/>']
        s += ['</g>',text(110,63,label,30,'#f0f4fa','font-weight="700"'),
              text(110,97,address,18,'#a8bbd1'),text(110,130,'OPEN →',12,color,'class="mono" letter-spacing="2"')]
        write(f'contact-{stem}.svg',s)

def contact_links():
    links=['<p align="center">']
    for stem,label,address,url,color in CONTACTS:
        links.append(f'  <a href="{url}"><img src="./assets/contact-{stem}.svg" width="270" alt="{label} — {address}" /></a>')
    links.append('</p>')
    return '\n'.join(links)

def picture(stem,alt,motion=False):
    reduced=''
    if motion:
        reduced=f'''    <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="{asset(stem+'-mobile-static')}" />
    <source media="(prefers-reduced-motion: reduce)" srcset="{asset(stem+'-static')}" />
'''
    return f'''<p align="center">
  <picture>
{reduced}    <source media="(max-width: 600px)" srcset="{asset(stem+'-mobile')}" />
    <img src="{asset(stem)}" width="100%" alt="{escape(alt,quote=True)}" />
  </picture>
</p>'''

def readme():
    original=(ROOT/'README.md').read_text()
    header=original[:original.index('</p>')+4]
    body=[header,'',picture('architecture','Engineering identity: industrial control → connected software and structured data → AI-assisted human decisions. SL Corporation · Production Engineering Center / Automation Company · Software Developer. Major: Computer Science.',motion=True),'',contact_links(),'',picture('projects','Project archive: '+', '.join(p[0] for p in PROJECTS)+'.'),'', '''<details>
<summary>Text version & project links</summary>

**Identity:** Manufacturing software engineer — connecting industrial control, structured data, and AI-assisted decisions.<br/>
**Current:** SL Corporation · Production Engineering Center (Jul. 2025–Present).<br/>
**Previously:** Automation Company · Software Developer (Oct. 2020–Jun. 2023).<br/>
**Education:** Bachelor’s Degree · Computer Science (Mar. 2018–Feb. 2025).
''']
    for i,(name,summary,tag,url,color) in enumerate(PROJECTS):
        label=f'[{name}]({url})' if url else name
        if i==0:summary+=' In development; private repository.'
        if name=='G90 · GV90 Programs':summary='G90 · GV90 프로젝트 참여 — process engineering.'
        if name=='Water Treatment SCADA':summary+=' Joint project with [seonghyeon0312](https://github.com/seonghyeon0312).'
        if name=='Manufacturing Process Optimization':summary='제조 공정 최적화 기술 — feedback-driven process improvement.'
        body.append(f'- **{label}** — {summary}')
    body += ['', '**Core stack:** PLC · LabVIEW · Robotics · Vision / Python · C++ / Qt · React · Node.js · SQL / Local LLM · Tool calling · Rule-based validation.', '', '**Research interest:** Knowledge-guided manufacturing AI — process data and engineering constraints for human-centered decision support.', '', '</details>', '']
    (ROOT/'README.md').write_text('\n'.join(body))

if __name__=='__main__':
    for mobile in [False,True]:
        architecture(mobile);architecture(mobile,animated=False);projects(mobile)
    contacts()
    readme()
    # Keep only the four current identity variants after updating their links.
    keep=set(ASSETS.values())
    for path in (ROOT/'assets').glob('architecture*.svg'):
        if path.name not in keep:path.unlink()
