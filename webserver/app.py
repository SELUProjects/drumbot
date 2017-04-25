import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

pins = {
	23: {'name': 'Red LED', 'state': GPIO.LOW},
	24: {'name': 'Green LED', 'state': GPIO.LOW}
}

notblinking = 1

for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)


@app.route("/")
def main():
	for pin in pins:
		pins[pin]['state'] = GPIO.input(pin)

	templateData = { 'pins': pins, 'notblinking': notblinking	}
	return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
	changePin = int(changePin)
	deviceName = pins[changePin]['name']

	if action == "on":
		GPIO.output(changePin, GPIO.HIGH)
		message = "Turned " + deviceName + " on."
	if action == "off":
		GPIO.output(changePin, GPIO.LOW)
		message = "Turned " + deviceName + " off."

	for pin in pins:
		pins[pin]['state'] = GPIO.input(pin)

	templateData = { 'pins': pins, 'notblinking': notblinking }

	return render_template('main.html', **templateData)

@app.route("/blink/<notblinking>")
def blink(notblinking):
	notblinking = int(notblinking)
	if notblinking:
		notblinking = 0
		for i in range(5):
			GPIO.output(23, GPIO.HIGH)
			GPIO.output(24, GPIO.LOW)
			time.sleep(3)
			GPIO.output(23, GPIO.LOW)
			GPIO.output(24, GPIO.HIGH)
			time.sleep(3)
	else:
		notblinking = 1
	templateData = { 'pins': pins, 'notblinking': notblinking }
	return render_template('main.html', **templateData)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
