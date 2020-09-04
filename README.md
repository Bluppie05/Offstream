# Offstream
Local video streaming has never been so easy

Offstream is local self-hosted video network to play your favorite movies, clips and videos. Build your own netflix using Offstream.

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

# Installation
## Linux(reccommended)
1. Clone the repository locally using the command `git clone https://github.com/Bluppie05/Offstream.git`
2. Install [python3](https://python.org/)
3. Enter the preconfigured virtual environment using the command `source env/bin/activate`
4. Run the server using the command `python3 -m flask run -h 0.0.0.0`
5. The server will now be running, connect using the Offstream client or go to your browser at http://{serverip}:5000/

## Windows(Not yet tested)
1. Clone the repository locally using the command `git clone https://github.com/Bluppie05/Offstream.git`
2. Install [python3](https://python.org/)
3. Install virtualenv using the command `pip install virtualenv`
4. Create a virtualenv using the command `virtualenv env`
5. Activate your virtualenv using the command `env\Scripts\activate.bat`
6. Install requirements using the command `pip install -r requirements.txt`
7. Run the server using the command `python -m flask run -h 0.0.0.0`
8. The server will now be running, connect using the Offstream client or go to your browser at http://{serverip}:5000/

## Mac
Coming soon, feel free to make a mac port, an official one will be coming soon.

## Unix / BSD(not yet tested)
1. Clone the repository locally using the command `git clone https://github.com/Bluppie05/Offstream.git`
2. Install [python3](https://python.org/)
3. Enter the preconfigured virtual environment using the command `source env/bin/activate`
4. Run the server using the command `python3 -m flask run -h 0.0.0.0`
5. The server will now be running, connect using the Offstream client or go to your browser at http://{serverip}:5000/



