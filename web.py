#!/root/miniconda3/bin/python
from wsgiref.simple_server import make_server
# from waitress import serve
import os, io
import uuid
import shutil
import daemon
from pyramid.response import Response
from pyramid.config import Configurator
from pyramid.response import Response
import random
import subprocess
from PIL import Image


def upload(request):

    fileObj = request.POST.get('filename')
    sid = str(random.randint(1111, 9999)) # TODO add map to remove collisions

    prb = request.POST.get('prb')

    filename = '{}.png'.format(sid)
    file_path = os.path.join('upload', filename )

    image_file = io.BytesIO(fileObj.file.read())
    try:
        im = Image.open(image_file)
        # print(im.size)
        # print(file_path)
        im.save(file_path)
        im.close()
    except:
        return Response('{"error":"image"}', headers={'Content-Type': 'application/json', 
    "Access-Control-Allow-Origin": "*", 
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"})

    # cwd ='/home/viktor/Tools/mmdetection'
    cwd ='.'
    # subprocess.Popen(["/bin/python", "/home/viktor/Projects/Courses/DLS/HWs/FinalProject/Examples/web_mmdetection/mmdetectionl.py", sid, prb], cwd=cwd)
    subprocess.Popen(["/home/viktor/anaconda3/envs/openmmlab/bin/python3", "/home/viktor/Projects/Courses/DLS/HWs/FinalProject/Examples/web_mmdetection/mmdetectionl.py", sid, prb])
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

        # config.add_route('hello', '/')
        # config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()

    # serve(app, host='0.0.0.0', port=8081)

    logfile = 'logs/web.log'
# pidfile = f'/tmp/det{sys.argv[1]}.pid'

    context = daemon.DaemonContext(
        working_directory='.',
        umask=0o002,
        # pidfile=PidFile(pidfile),
        stdout=open(logfile, "a"),
        stderr=open(logfile, "a"),
        detach_process=True
        # f = open("demofile2.txt", "a")

        # logfile=logfile
    )
    context.stdout.write("Now the file has more content!")
    with context:
        server = make_server('127.0.0.1', 8081, app)
        server.serve_forever()

