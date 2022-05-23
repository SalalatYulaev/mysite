from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
	return "Hello!"


if __name__ == '__main__':
	app.run(debug=True, port=8080)