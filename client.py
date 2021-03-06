#!/usr/bin/env python

# Borrowed from http://www.ugw.name/?page_id=157

import pyaudio
import socket


# Pyaudio Initialization
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)

# Socket Initialization
host = 'localhost'  # Change this to client's host
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Main Functionality
while True:
    data = stream.read(CHUNK)
    s.send(data)
    s.recv(size)

s.close()
stream.close()
p.terminate()
