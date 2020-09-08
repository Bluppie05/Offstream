from flask import Flask, render_template, request, send_from_directory, jsonify, Response, redirect, session
import subprocess
import platform
import os
import urllib.parse
import urllib.request
import platform
import socket
import json
from tmdbv3api import TMDb
from tmdbv3api import Movie
from flask_basicauth import BasicAuth
from readsettings import ReadSettings

data = ReadSettings("settings.json")
credentialdata = ReadSettings("credentials.json")


api = data["the_movie_database_apikey"]

usrname = credentialdata["Username"]
passwd = credentialdata["Password"]

tmdb = TMDb()
tmdb.api_key = str(api)
tmdb.language = 'en'
tmdb.debug = True

movie = Movie()


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
    ffmpeg = "ffmpeg\\"+system+"\\"+architecture+"\\ffmpeg.exe"
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


basic_auth = BasicAuth(app)
app.config['BASIC_AUTH_USERNAME'] = str(usrname)
app.config['BASIC_AUTH_PASSWORD'] = str(passwd)

def filter(fname):
        file_name = str(fname).casefold()
        file_name = str(file_name).replace(".mp4", "")
        file_name = str(file_name).replace(".mkv", "")
        file_name = str(file_name).replace(".webm", "")
        file_name = str(file_name).replace(".avi", "")
        file_name = str(file_name).replace(".", " ")
        file_name = str(file_name).replace("-", " ")
        file_name = str(file_name).replace("720p", "")
        file_name = str(file_name).replace("1080p", "")
        file_name = str(file_name).replace("480p", "")
        file_name = str(file_name).replace("144p", "")
        file_name = str(file_name).replace("720p", "")
        file_name = str(file_name).replace("torrent", "")
        file_name = str(file_name).replace("fullhd", "")
        file_name = str(file_name).replace("full", "")
        file_name = str(file_name).replace("hdts", "")
        file_name = str(file_name).replace("hd", "")
        file_name = str(file_name).replace("2019", "")
        file_name = str(file_name).replace("2020", "")
        file_name = str(file_name).replace("2018", "")
        file_name = str(file_name).replace("2017", "")
        file_name = str(file_name).replace("2016", "")
        file_name = str(file_name).replace("2015", "")
        file_name = str(file_name).replace("2014", "")
        file_name = str(file_name).replace("2013", "")
        file_name = str(file_name).replace("2012", "")
        file_name = str(file_name).replace("2011", "")
        file_name = str(file_name).replace("2010", "")
        file_name = str(file_name).replace("2009", "")
        file_name = str(file_name).replace("2008", "")
        file_name = str(file_name).replace("2007", "")
        file_name = str(file_name).replace("2006", "")
        file_name = str(file_name).replace("2005", "")
        file_name = str(file_name).replace("2004", "")
        file_name = str(file_name).replace("2003", "")
        file_name = str(file_name).replace("2002", "")
        file_name = str(file_name).replace("2001", "")
        file_name = str(file_name).replace("2000", "")
        file_name = str(file_name).replace("xvid", "")
        file_name = str(file_name).replace("etrg", "")

        return file_name

@app.route('/')
@basic_auth.required
def index():
    files = os.scandir("videos")

    html = ""
    html2 = ""
    info = ""
    for f in files:
        file_name = filter(f.name)
        endimg = ""
        try:
            search = movie.search(file_name)
            if not search:
                dsfswq23=D8asD
            postr = ""
            info = ""
            for res in search:
                postr = res.poster_path
                info = res.overview
            poster_img = 'https://image.tmdb.org/t/p/w500' + postr
            html2 += '<li><a href="player?v=' + str(f.name) + '" title="' + str(info) + '"><div class="responsive"><div class="gallery"><img src="' + str(poster_img) + '" width="600" height="400"><div class="desc">' + str(file_name) + '</div></div></div></a></li>'
        except:
            link = "http://127.0.0.1:5000/thumbnail?v=" + urllib.parse.quote(str(f.name))
            file_img = urllib.request.urlopen(link).read()
            file_img = file_img.decode("utf-8")
            html += '<li><a href="player?v=' + str(f.name) + '" title="' + str(file_name) + '"><div class="responsive"><div class="gallery"><img src="' + str(file_img) + '" style="width:100%;height:180px;"><div class="desc">' + str(file_name) + '</div></div></div></a></li>'
    #html = '<ul class="items">' + html + '</ul>'
    html = urllib.parse.quote(html)
    html2 = urllib.parse.quote(html2)

    return(render_template("index.html", videolist=html, movielist=html2, movinf=info))

@app.route('/lib')
def lib():
    files = os.scandir("videos")

    html = ""
    html2 = ""
    for f in files:
        file_name = filter(f.name)
        endimg = ""
        try:
            search = movie.search(file_name)
            if not search:
                dsfswq23=D8asD
            postr = ""
            for res in search:
                postr = res.poster_path
            poster_img = 'https://image.tmdb.org/t/p/w500' + postr
            html2 += '<li><a href="player?v=' + str(f.name) + '" title="' + str(file_name) + '"><div class="responsive"><div class="gallery"><img src="' + str(poster_img) + '" width="600" height="400"><div class="desc">' + str(file_name) + '</div></div></div></a></li>'
        except:
            link = "http://127.0.0.1:5000/thumbnail?v=" + urllib.parse.quote(str(f.name))
            file_img = urllib.request.urlopen(link).read()
            file_img = file_img.decode("utf-8")
            html += '<li><a href="player?v=' + str(f.name) + '" title="' + str(file_name) + '"><div class="responsive"><div class="gallery"><img src="' + str(file_img) + '" style="width:100%;height:180px;"><div class="desc">' + str(file_name) + '</div></div></div></a></li>'
    #html = '<ul class="items">' + html + '</ul>'
    html = urllib.parse.quote(html)
    html2 = urllib.parse.quote(html2)

    return(render_template("lib.html", videolist=html, movielist=html2))


@app.route('/settings')
def settings():
    pipver = platform.python_version()
    ver = 'v1'
    ipv4 = socket.gethostbyname(socket.gethostname()) + ":5000"
    libdir = "Offstream/videos"


    return(render_template("settings.html", pipver=pipver, ver=ver, ipv4=ipv4, libdir=libdir, username=usrname))

@app.route('/player')
def player():
    v = request.args.get("v")

    if ".mkv" in v:
        link = "http://127.0.0.1:5000/mkv?v=" + urllib.parse.quote(str(v))
        mp4 = urllib.request.urlopen(link).read()
        os.remove("videos/"+v)
        v = mp4.decode("utf-8")
        return redirect("/player?v="+v.replace("/videos/", ""))
    if ".avi" in v:
        link = "http://127.0.0.1:5000/avi?v=" + urllib.parse.quote(str(v))
        mp4 = urllib.request.urlopen(link).read()
        os.remove("videos/"+v)
        v = mp4.decode("utf-8")
        return redirect("/player?v="+v.replace("/videos/", ""))

    return(render_template("player.html", video=v))

@app.route('/thumbnail')
def thumbnail():
    video_input_path = 'videos/' + request.args.get("v")
    img_output_path = 'thumbnails/' + request.args.get("v") + ".jpg"
    subprocess.call([ffmpeg, '-n', '-i', video_input_path, '-ss', '00:00:00.000', '-vframes', '1', img_output_path])
    img_link = "/"+img_output_path
    return(render_template("thumbnail.html", img=img_link))

@app.route('/mkv')
def mkv():
    video_input_path = 'videos/' + request.args.get("v")
    img_output_path = 'videos/'+request.args.get("v").replace(".mkv", ".mp4")
    subprocess.call([ffmpeg, '-n', '-i', video_input_path, img_output_path])
    img_link = "/"+img_output_path
    return(render_template("thumbnail.html", img=img_link))

@app.route('/avi')
def avi():
    video_input_path = 'videos/' + request.args.get("v")
    img_output_path = 'videos/'+request.args.get("v").replace(".avi", ".mp4")
    subprocess.call([ffmpeg, '-n', '-i', video_input_path, img_output_path])
    img_link = "/"+img_output_path
    return(render_template("thumbnail.html", img=img_link))


@app.route('/account', methods=['post', 'get'])
@basic_auth.required
def login():
    message = ''
    if request.method == 'POST':
        json_object = ""
        json_object2 = ""
        username = request.form.get('username')  # access the data inside
        password = request.form.get('password')

        dictionary ={
            "Username" : str(username),
            "Password" : str(password)
        }

        # Serializing json
        json_object = json.dumps(dictionary, indent = 2)

        # Writing to sample.json
        with open("credentials.json", "w") as outfile:
            outfile.write(json_object)
            message = "Password updated! Restart the Offstream server to apply changes!"

    return render_template('account.html', message=message)




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

# serve static path img
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('fonts', path)
