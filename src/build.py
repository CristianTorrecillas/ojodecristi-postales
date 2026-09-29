"""Arma ../index.html (un solo archivo, todo embebido) a partir de postales.template.html."""
import base64, os
H = os.path.dirname(os.path.abspath(__file__))
def b64(p): return base64.b64encode(open(os.path.join(H, p), 'rb').read()).decode()
rep = {
 'JBM400': b64('fonts/jetbrains-mono-latin-400-normal.woff2'),
 'JBM500': b64('fonts/jetbrains-mono-latin-500-normal.woff2'),
 'FIRA400': b64('fonts/fira-sans-latin-400-normal.woff2'),
 'FIRA500': b64('fonts/fira-sans-latin-500-normal.woff2'),
 'CAVEAT400': b64('fonts/caveat-latin-400-normal.woff2'),
 'CAVEAT600': b64('fonts/caveat-latin-600-normal.woff2'),
 'CAVEAT700': b64('fonts/caveat-latin-700-normal.woff2'),
 'PAPER': b64('assets/paper.jpg'), 'STAMP': b64('assets/stamp560.png'),
 'TAPE': b64('assets/tape.png'), 'CLIP': b64('assets/clip.png'),
 'P1': b64('sample/p1.jpg'), 'P2': b64('sample/p2.jpg'), 'P3': b64('sample/p3.jpg'), 'P4': b64('sample/p4.jpg'),
}
s = open(os.path.join(H, 'postales.template.html')).read()
for k, v in rep.items(): s = s.replace('{{' + k + '}}', v)
assert '{{' not in s, [l[:120] for l in s.split('\n') if '{{' in l][:3]
open(os.path.join(H, '..', 'index.html'), 'w').write(s)
print(round(len(s) / 1e6, 2), 'MB')
