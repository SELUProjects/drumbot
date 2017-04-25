from flask import Flask, Blueprint, Response, request, json, jsonify, render_template
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
import os
import csv

arduino = Blueprint('arduino', __name__)

leftDS = 7
rightDS = 6
tamborine = 5

connection = SerialManager()
a = ArduinoApi(connection=connection)
a.pinMode(leftDS, a.OUTPUT)
a.pinMode(rightDS, a.OUTPUT)
a.pinMode(tamborine, a.OUTPUT)


@arduino.route('/play_song')
def play_song():
    filename = request.args.get('filename', 'sample_beat_1.csv', type=str)
    filepath = '/home/pi/nanpyapi/arduino/songs/' + filename

    beats = {}

    with open('/home/pi/nanpyapi/arduino/songs/sample_beat_1.csv', newline='') as c:
        song = csv.reader(c)
        counter = 0
        for row in song:
            beats[counter] = row
            counter += 1

    read_beats(beats)

    return jsonify(result=filename)


@arduino.route('/one_beat')
def one_beat():
    instruments = {
        0: ['no instrument'],
        1: ['left drum', leftDS],
        2: ['right drum', rightDS],
        3: ['tamborine', tamborine]
    }
    instrument = instruments[request.args.get('a', 0, type=int)]

    a.digitalWrite(instrument[1], a.HIGH)
    sleep(.15)
    a.digitalWrite(instrument[1], a.LOW)
    sleep(.2)

    return jsonify(result=instrument[0])


@arduino.route('/rhythm')
def play_rhythm():
    rhythm = {}
    strike = request.args.get('strike', 6, type=int)/60
    tempo = request.args.get('tempo', 6, type=int)
    loop = request.args.get('loop', 1, type=int)
    name = request.args.get('name', None, type=str)
    saved_name = name + '.csv'

    for i in range(8):
        beat = [0, 0, 0, strike, tempo]
        beat[request.args.get(str(i), 2, type=int)] = 1
        rhythm[i] = beat

    if name is not None:
        with open('/home/pi/nanpyapi/arduino/songs/' + saved_name, 'a', newline='') as c:
            writer=csv.writer(c)
            for i in rhythm:
                writer.writerow(rhythm[i])

        with open('/home/pi/nanpyapi/arduino/songs/list_beats.csv', 'a', newline='') as c:
            writer=csv.writer(c)
            writer.writerow([])
            writer.writerow([name,saved_name])
    for i in range(loop):
        read_beats(rhythm)

    return jsonify(result=rhythm)


@arduino.route('/list_beats')
def list_beats():
    beats = []
    with open('/home/pi/nanpyapi/arduino/songs/list_beats.csv', newline='') as c:
        beat_list = csv.reader(c)
        for row in beat_list:
            beats.append({'title': row[0], 'file': row[1]})

    templateData = {'beats': beats}
    return render_template('list.html', **templateData)


@arduino.route('/')
def index():
    return render_template('index.html')


def read_beats(beats):
    for i in range(len(beats)):
        a.digitalWrite(leftDS, int(beats[i][0]))
        a.digitalWrite(rightDS,int(beats[i][1]))
        a.digitalWrite(tamborine,int(beats[i][2]))
        sleep(float(beats[i][3]))
        a.digitalWrite(leftDS, 0)
        a.digitalWrite(rightDS, 0)
        a.digitalWrite(tamborine, 0)
        sleep((60/int(beats[i][4]) - float(beats[i][3])))
