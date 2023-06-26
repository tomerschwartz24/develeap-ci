 #!flask/bin/python
from flask import Flask, request, request_started

app = Flask(__name__)
counter = 0
@app.route('/', methods=["POST", "GET"])
def index():
    global counter
    if request.method == "GET":
        counter+=1
        return "Hmm, Plus 1 please "
    else:
        return str(f"This pointless app have : {counter} visitors, hooray! ")
if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
