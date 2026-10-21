#!/usr/bin/env python3
"""Render the eight reviewed comparisons as an editable SVG, using only stdlib."""
import json
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'evaluation/v2/results.json'
OUT = ROOT / 'assets/evaluation.svg'
COLORS = {'research': '#12634C', 'native': '#A94631', 'tie': '#53685E'}
NAMES = {'research': 'Aperture preferred', 'native': 'Native preferred', 'tie': 'Tie'}
TASKS = {'H1': 'Measured air quality', 'H2': 'Release + advisory watcher', 'H3': 'Biodiversity map', 'H4': 'Research evidence digest'}

def render(data):
    pairs = data['pairs']
    expected = {f'H{task}-R{repeat}' for task in range(1, 5) for repeat in (1, 2)}
    if len(pairs) != 8 or {p['pair'] for p in pairs} != expected:
        raise ValueError('Expected all eight distinct frozen pairs; no missing/duplicate rows.')
    counts = {k: sum(p['winner'] == k for p in pairs) for k in COLORS}
    if counts != data['primary_preferences']:
        raise ValueError('Preference summary disagrees with actual pair decisions.')
    for p in pairs:
        if p['winner'] not in COLORS or p['strength'] not in ('tie', 'slight', 'material'):
            raise ValueError('Invalid preference category.')
        for arm in ('native', 'research'):
            s = p['scores'][arm]
            if len(s['dimensions']) != 6 or any(type(x) is not int or not 0 <= x <= 4 for x in s['dimensions']) or sum(s['dimensions']) != s['total']:
                raise ValueError('Invalid criterion scores or total.')
    def text(x, y, value, size=24, color='#192C27', weight='400', extra=''):
        return f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'
    b = ['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="850" viewBox="0 0 1440 850" role="img" aria-labelledby="title desc">', '<title id="title">Aperture real-world comparison</title>', f'<desc id="desc">Eight primary review preferences: Aperture preferred in {counts["research"]}, ties in {counts["tie"]}, native preferred in {counts["native"]}. Four live-source tasks, two repetitions each. Small same-family evaluation with a disclosed blinding leak and additional crosschecks; no universal superiority claim.</desc>', '<rect width="1440" height="850" rx="24" fill="#F7F5EF"/>']
    b += [text(64, 80, 'Useful differences, visible tradeoffs.', 46, weight='700'), text(65, 123, '4 live-source tasks × 2 independent repeats × 2 arms', 26, '#53685E')]
    for x, key in [(65, 'research'), (515, 'tie'), (965, 'native')]:
        b.append(f'<rect x="{x}" y="164" width="410" height="126" rx="12" fill="#FFFFFF" stroke="#D4DBD2"/>')
        b += [text(x+24, 226, counts[key], 56, COLORS[key], '700'), text(x+100, 221, NAMES[key], 24, COLORS[key], '700'), text(x+100, 257, 'Primary pairwise judgments', 19, '#53685E')]
    b += [text(65, 347, 'Task', 21, '#53685E', '700'), text(640, 347, 'Repeat 1', 21, '#53685E', '700'), text(1065, 347, 'Repeat 2', 21, '#53685E', '700')]
    by_pair = {p['pair']: p for p in pairs}
    for task in range(1, 5):
        y = 403 + (task-1)*84
        b += [text(65, y, f'H{task}', 19, '#53685E', '700'), text(120, y, TASKS[f'H{task}'], 25, weight='700')]
        for repeat, x in [(1, 620), (2, 1045)]:
            p = by_pair[f'H{task}-R{repeat}']
            label = 'Tie' if p['winner'] == 'tie' else ('Aperture' if p['winner'] == 'research' else 'Native') + ' · ' + p['strength']
            b.append(f'<circle cx="{x}" cy="{y-8}" r="7" fill="{COLORS[p["winner"]]}"/>')
            b.append(text(x+22, y, label, 23, COLORS[p['winner']], '700'))
        b.append(f'<path d="M65 {y+27}H1375" stroke="#D4DBD2"/>')
    b += [text(65, 757, 'A small comparison, not a population-wide ranking.', 23, weight='700'), text(65, 798, 'Read the source checks, native win, reviewer exposure and crosscheck differences alongside these counts.', 21, '#53685E'), '</svg>']
    return ''.join(b)

if __name__ == '__main__':
    OUT.write_text(render(json.loads(DATA.read_text())))
    print(OUT.name)
