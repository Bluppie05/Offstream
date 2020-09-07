# Offstream
Local video streaming has never been so easy

Offstream is local self-hosted media server to play your favorite movies, clips and videos.

# Comparison
## Offstream
- Original video quality
- Elegant and convinient UI
- Cross-platform
- Free
- Opensource
- Low resource usage

## Plex
- Low or destorted video quality
- Elegant and convinient UI
- Cross-platform
- Free
- Closed source
- Extremely high / intesive resource usage

## Emby
- OK video quality
- Elegant but inconvinient UI
- Cross-platform
- Paid (very limited free version)
- Closed source
- OK resource usage

# Media Server Installation (Default Credentials = Username: `admin` Password:`admin`)

First follow theese steps to get an api key (free): https://developers.themoviedb.org/3/getting-started/introduction
## Linux(recommended)
1. Clone the repository locally using the command `git clone https://github.com/Bluppie05/Offstream.git`
2. Install [python3](https://python.org/)
3. Enter the preconfigured virtual environment using the command `source env/bin/activate`
4. Run the server using the command `python3 -m flask run -h 0.0.0.0`
5. Set your api key by using the command, replace {yourapikey} with your actual api key `setenv apikey {yourapikey}`
6. The server will now be running, connect using the Offstream client or go to your browser at http://{serverip}:5000/

## Windows
All commands below have to be ran in powershell, cmd will NOT work. Tutorial: https://youtu.be/Z4xijDAd2M8
1. Install [git-cli](https://git-scm.com/download/win)
2. Clone the repository locally using the command `git clone https://github.com/Bluppie05/Offstream.git`
3. Install [python3](https://python.org/)
4. Install virtualenv using the command `pip install virtualenv`
5. Create a virtualenv using the command `virtualenv env`
6. Activate your virtualenv using the command `env\Scripts\activate.bat`
7. Install requirements using the command `pip install -r requirements.txt`
8. Set your api key by using the command, replace {yourapikey} with your actual api key `set apikey={yourapikey}`
9. Run the server using the command `python -m flask run -h 0.0.0.0`
10. The server will now be running, connect using the Offstream client or go to your browser at http://{serverip}:5000/

## Mac
Coming soon, feel free to make a mac port, an official one will be coming soon.

## Unix / BSD(not yet tested)
1. Clone the repository locally using the command `git clone https://github.com/Bluppie05/Offstream.git`
2. Install [python3](https://python.org/)
3. Enter the preconfigured virtual environment using the command `source env/bin/activate`
4. Run the server using the command `python3 -m flask run -h 0.0.0.0`
5. The server will now be running, connect using the Offstream client or go to your browser at http://{serverip}:5000/

## Ubuntu Image(Offstream pre-installed)
Coming Soon.

# Client Installation
Install the offstream client to connect quickly to a offstream media server.

## Android app
Download from google play(coming soon) or from the [releases](https://github.com/Bluppie05/Offstream/releases) page

## Ios app(Iphone, Ipad)
There is no official app yet, but you can install a (web-based) app by adding your media server link to your homescreen.

1. Run the server and connect to the webpage by going to this adress in safari: http://{serverip}:5000/
2. Tap the share button.
3. Tap add to homescreen, and click on add.

## TV(Android tv, Amazon fire tv, NVIDIA Shield, Apple tv, Chromecast, Roku, LG smart tv, Samsung smart tv, PS4, Xbox One, Kodi)
Coming soon.



