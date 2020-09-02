from flask import Flask, render_template, request, send_from_directory, jsonify, Response
import subprocess
import platform

if(platform.system() == "Linux"):
    system = "linux"
    if(platform.architecture()[0] == "64bit" or platform.architecture()[0] == "32bit"):
        architecture = "amd64"
    elif(platform.architecture()[0] == "arm64"):
        architecture = "arm64"
    else:
        architecture = "amd64"
    ffmpeg = "./ffmpeg/"+system+"/"+architecture+"/ffmpeg"
elif(platform.system() == "Windows"):
    system = "windows"
    if(platform.architecture()[0] == "64bit"):
        architecture = "win64"
    elif(platform.architecture()[0] == "32bit"):
        architecture = "win32"
    else:
        architecture = "win64"
    ffmpeg = "ffmpeg/"+system+"/"+architecture+"/ffmpeg.exe"
else:
    system = "linux"
    if(platform.architecture()[0] == "64bit" or platform.architecture()[0] == "32bit"):
        architecture = "amd64"
    elif(platform.architecture()[0] == "arm64"):
        architecture = "arm64"
    else:
        architecture = "amd64"
    ffmpeg = "./ffmpeg/"+system+"/"+architecture+"/ffmpeg"

app = Flask(__name__.split('.')[0], static_url_path="")

@app.route('/')
def index():
    f = request.args.get("f")
    return(render_template("index.html", file=f))

@app.route('/player')
def player():
    v = request.args.get("v")
    return(render_template("player.html", video=v))

@app.route('/thumbnail')
def thumbnail():
    video_input_path = 'videos/' + request.args.get("v")
    img_output_path = 'thumbnails/' + request.args.get("v") + ".jpg"
    subprocess.call([ffmpeg, '-n', '-i', video_input_path, '-ss', '00:00:00.000', '-vframes', '1', img_output_path])
    img_link = "/"+img_output_path
    return(render_template("thumbnail.html", img=img_link))


# serve static path vidjs
@app.route('/videojs/<path:path>')
def send_config(path):
    return send_from_directory('videojs', path)

# serve static path vidjs
@app.route('/videos/<path:path>')
def send_videos(path):
    return send_from_directory('videos', path)

# serve static path css
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

# serve static path thumbnails
@app.route('/thumbnails/<path:path>')
def send_thumbnails(path):
    return send_from_directory('thumbnails', path)