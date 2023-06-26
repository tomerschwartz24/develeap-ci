 #!flask/bin/python
from flask import Flask, request, request_started

app = Flask(__name__)
counter = 0
@app.route('/', methods=["POST", "GET"])
def index():
    global counter
    if request.method == "GET":
        counter+=1
        return f"<h1>This pointless app has received a total of {counter} HTTP GET requests, Hooray! 🎉</h1>"

    else:
        return f"<h1>Our counter is: {counter} 😄</h1>"
if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
