from flask import Flask, request, jsonify, json
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def myapp():
    return jsonify("Hello from Madhu Vemula")

@app.route('/companies', methods=['GET'])
def get_companies():
    companies = [{"id": 1, "name": "Madhu's Company One"}, {"id": 2, "name": "Madhu's Company Two"}, {"id": 3, "name": "Madhu's Company Three"}]
    return json.dumps(companies)

@app.route('/optimalweight', methods=['POST'])
def optimal_height():
    content=request.json
    print(content)
    height=content['height']
    return jsonify(height*10)

@app.route('/test', methods=['GET'])
def test():
    url = "http://dummy.restapiexample.com/api/v1/employees"
    r = requests.get(url)
    return r.json()
