from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roll', methods = ['GET', 'POST'])
def dice():
    count = int(request.args.get('count'))   # /roll?count=2
    side = int(request.args.get('sides'))    # /roll?sides=20

    if (not count): count = 1
    if (not side): side = 20

    results = []
    number_die = list(range(count))
    for d in number_die:
        results.append(random.choice(list(range(1, side + 1))))

    dic = {
        "sides": side,
        "count": count,
        "results": results
    }
    
    jsonData = jsonify(dic)

    print(jsonData)

    return jsonData

if __name__ == '__main__':
    app.run(host="0.0.0.0:5000")


# $ export FLASK_APP=hello
# $ flask run