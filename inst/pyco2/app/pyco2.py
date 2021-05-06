#!/usr/bin/python3

import os,socket,jinja2

from flask import Flask, request, render_template, send_from_directory
from jinja2 import Template
from datetime import datetime

def readcounter():
    with open(counter_file) as f:
      first_line = f.readline().strip()
    return (int(first_line))

def writecounter (c):
     f = open(counter_file,"w+")
     f.write("%d" % c)
     f.close()

def colorizecontainer():
  templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
  templateEnv = jinja2.Environment(loader=templateLoader)
  TEMPLATE_FILE = "cc.svg.j2"
  template = templateEnv.get_template(TEMPLATE_FILE)

  outputText = template.render(rfill=crfill,cfill=ccfill)
  with open('static/cc.svg', 'w+') as f:
    f.write(outputText)

def envcolor(ccolor):
  f = open (color_file,'r')
  for line in f:
      if (line.split()[0] == ccolor):
         return (int(line.split()[1],16))
  return(0x478B22)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


  
#
# Initialization
#

app = Flask(__name__)

pyco_ver = '7.0'

start_t = datetime.now()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

image_name = 'cc.svg'
container_color = os.getenv('CCOLOR','green') ;

counter_file = 'state/counter.txt'
color_file = 'config/colors.txt'

hxcrfill=envcolor(container_color)

hxccfill=hxcrfill-0x4000

# Strip the 0x as we need # for the HTML/SVG colors

ccfill='{:x}'.format(hxccfill).zfill(6)
crfill='{:x}'.format(hxcrfill).zfill(6)

colorizecontainer()

#
# MAIN
#

@app.route("/")
def index():
    start_dt = start_t.strftime("%m/%d/%Y at %H:%M:%S")
    start_s = datetime.now() - start_t
    
    visitorAddr = ''
    hostname = socket.gethostname()

    visitorAddr = request.environ['REMOTE_ADDR']
    visitorCount = readcounter() + 1
    writecounter(visitorCount)

    return render_template("welcome.html.j2",image=image_name,color=container_color,visitor=visitorAddr,count=visitorCount,node=hostname,my_ip=get_ip(),startup_dt=start_dt,startup_s=start_s,pyco_version=pyco_ver)


if __name__=='__main__':
    app.debug = True
    app.run( host='0.0.0.0', port=8080 )
