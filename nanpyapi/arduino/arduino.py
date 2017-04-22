from flask import Flask, Blueprint, Response, request, json
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

arduino = Blueprint('arduino', __name__)

leftDS = 7
rightDS = 6
tamborine = 5

connection = SerialManager()
a = ArduinoApi(connection=connection)
a.pinMode(leftDS, a.OUTPUT)
a.pinMode(rightDS, a.OUTPUT)
a.pinMode(tamborine, a.OUTPUT)


@arduino.route('/')
def drumbot():
    return 'Drumbot says "Beat it!"'


@arduino.route('/play/<int:beat>')
def play(beat):
    striketime = .15
    fastbeat = .15 - striketime
    midbeat = .30 - striketime
    slowbeat = .60 - striketime
    data = {'beat played': beat}

    if beat == 1:
        for i in range(3):
            a.digitalWrite(leftDS, a.HIGH)
            sleep(striketime)
            a.digitalWrite(leftDS, a.LOW)
            sleep(slowbeat)
            a.digitalWrite(rightDS, a.HIGH)
            sleep(striketime)
            a.digitalWrite(rightDS, a.LOW)
            sleep(slowbeat)
            a.digitalWrite(tamborine, a.HIGH)
            sleep(striketime)
            a.digitalWrite(tamborine, a.LOW)
            sleep(slowbeat)

        return Response(json.dumps(data), status=200, mimetype='application/json')
    
    if beat == 2:
        for i in range(3):
            a.digitalWrite(rightDS, a.HIGH)
            sleep(striketime)
            a.digitalWrite(rightDS, a.LOW)
            sleep(slowbeat)
            a.digitalWrite(tamborine, a.HIGH)
            sleep(striketime)
            a.digitalWrite(tamborine, a.LOW)
            sleep(slowbeat)
            a.digitalWrite(leftDS, a.HIGH)
            sleep(striketime)
            a.digitalWrite(leftDS, a.LOW)
            sleep(slowbeat)
            a.digitalWrite(tamborine, a.HIGH)
            sleep(striketime)
            a.digitalWrite(tamborine, a.LOW)
            sleep(slowbeat)
            a.digitalWrite(tamborine, a.HIGH)
            sleep(striketime)
            a.digitalWrite(tamborine, a.LOW)
            sleep(slowbeat)

        return Response(json.dumps(data), status=200, mimetype='application/json')

    return 'You have no beat.'
