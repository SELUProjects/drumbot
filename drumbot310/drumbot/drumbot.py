from flask import Flask, Blueprint, Response, request, json
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

drumbot = Blueprint('drumbot', __name__)

leftDS = 7
rightDS = 6
tamborine = 5

connection = SerialManager()
a = ArduinoApi(connection=connection)
a.pinMode(leftDS, a.OUTPUT)
a.pinMode(rightDS, a.OUTPUT)
a.pinMode(tamborine, a.OUTPUT)


@drumbot.route('/')
def drumbot():
    return 'Drumbot says "Beat it!"'


@drumbot.route('/play/<int:beat>')
def play(beat):
    striketime = .10
    fastbeat = .15 - striketime
    midbeat = .30
    slowbeat = .60 - striketime
    data = {'beat played': beat}

    beats = [
        [1, 0, 0, striketime, midbeat],
        [0, 1, 0, striketime, midbeat],
        [1, 0, 0, striketime, midbeat],
        [0, 0, 1, striketime, midbeat],
        [0, 0, 1, striketime, midbeat],
        [1, 0, 0, striketime, midbeat],
        [0, 1, 0, striketime, midbeat],
        [0, 0, 1, striketime, midbeat],
    ]

    if beat == 1:
        for line in beats:
            a.digitalWrite(leftDS,line[0])
            a.digitalWrite(rightDS,line[1])
            a.digitalWrite(tamborine,line[2])
            sleep(line[3])
            a.digitalWrite(leftDS, 0)
            a.digitalWrite(rightDS, 0)
            a.digitalWrite(tamborine, 0)
            sleep(line[4] - line[3])

        return Response(json.dumps(data), status=200, mimetype='application/json')
    
    if beat == 2:
        for i in range(2):
            for line in beats:
                a.digitalWrite(leftDS,line[0])
                a.digitalWrite(rightDS,line[1])
                a.digitalWrite(tamborine,line[2])
                sleep(line[3])
                a.digitalWrite(leftDS, 0)
                a.digitalWrite(rightDS, 0)
                a.digitalWrite(tamborine, 0)
                sleep(line[4] - line[3])

        return Response(json.dumps(data), status=200, mimetype='application/json')

    return 'You have no beat.'
