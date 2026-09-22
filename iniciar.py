"""Servidor local de la enciclopedia. Ejecutar con Python 3."""
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit,unquote
import mimetypes
ROOT=Path(__file__).resolve().parent
mimetypes.add_type('application/javascript','.js');mimetypes.add_type('image/webp','.webp')
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(ROOT),**kwargs)
 def do_GET(self):
  requested=unquote(urlsplit(self.path).path)
  if not Path(requested).suffix:self.path='/index.html'
  super().do_GET()
 def end_headers(self):
  self.send_header('X-Content-Type-Options','nosniff')
  self.send_header('Cache-Control','no-cache')
  super().end_headers()
 def log_message(self,*args):pass
if __name__=='__main__':
 print('Enciclopedia disponible en http://127.0.0.1:8765/',flush=True)
 ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()
