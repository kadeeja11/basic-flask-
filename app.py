from flask import Flask, request

app = Flask(__name__)

student = {
    "1" : {"id": 1, "name": "bala"},
    "2" : {"id": 2, "name": "rithivik"}
    }

@app.route("/")
def hello_world():
    return "<p>hello world</p>"

@app.route("/index")
def index():
    return "From index"

@app.route("/student/<id>/<classes>")
def view_student(id, classes):
    id = request.view_args["id"]
    return student[id]




if __name__=="__main__":
    app.run() 