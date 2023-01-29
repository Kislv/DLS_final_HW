#!/root/miniconda3/bin/python
from wsgiref.simple_server import make_server
import os, io
import daemon
from pyramid.response import Response
from pyramid.config import Configurator
from pyramid.response import Response
import random
import subprocess
from PIL import Image

python_path = '/home/viktor/anaconda3/envs/openmmlab/bin/python3'
script_path = '/home/viktor/Projects/Courses/DLS/HWs/FinalProject/MyProject/detection/back-end/detection_script.py'

def upload(request):

    fileObj = request.POST.get('filename')
    names_set = {0}
    length = len(names_set)
    while (1):
        sid = str(random.randint(1111, 9999))
        names_set.add(sid)
        if length == len(names_set) - 1:
            break
        if length == 8888:
            exit(1)

    prb = request.POST.get('prb')
    filename = '{}.png'.format(sid)
    file_path = os.path.join('upload', filename )

    image_file = io.BytesIO(fileObj.file.read())
    try:
        im = Image.open(image_file)
        im.save(file_path)
        im.close()
    except:
        return Response('{"error":"image"}', headers={'Content-Type': 'application/json', 
    "Access-Control-Allow-Origin": "*", 
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"})

    subprocess.Popen([python_path, script_path, sid, prb])
    print('id', sid)
    return Response('{"success":"Ok", "id": "%s"}' % sid, headers={'Content-Type': 'application/json', 
    "Access-Control-Allow-Origin": "*", 
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"})

def testHandler(request):
    return Response('{"error":"HELLO, WORLD!"}', headers={'Content-Type': 'application/json'})

if __name__ == '__main__':
    with Configurator() as config:

        config.add_route('upload', '/upload')
        config.add_view(upload, route_name='upload')

        config.add_route('test', '/test')
        config.add_view(testHandler, route_name='test')
        app = config.make_wsgi_app()

    logfile = 'logs/server.log'

    context = daemon.DaemonContext(
        working_directory='.',
        umask=0o002,
        stdout=open(logfile, "a"),
        stderr=open(logfile, "a"),
        detach_process=True
    )
    context.stdout.write("Now the file has more content!")
    with context:
        server = make_server('127.0.0.1', 8081, app)
        server.serve_forever()
