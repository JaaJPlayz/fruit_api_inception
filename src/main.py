from flask import Flask
import flask_cors
import json
import requests

app = Flask(__name__)

# CORS
flask_cors.CORS(app)


# Routes
@app.route('/')
def get_root():
    return json.dumps({'message': 'Welcome to the Fruits API!'})


@app.route('/api/fruits')
def get_fruits():
    API_ENDPOINT = "https://www.fruityvice.com/api/fruit/all"
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        print("Success")
        return response.json()
    else:
        return json.dumps({'message': 'Error'})


@app.route('/api/fruit/<fruit_name>')
def get_fruit(fruit_name):
    API_ENDPOINT = f"https://www.fruityvice.com/api/fruit/{fruit_name}"
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        print("Success")
        return response.json()
    if response.status_code == 404:
        print("Fruit not found")
        return json.dumps({'message': 'Fruit not found'})
    else:
        print("Error")
        return json.dumps({'message': 'Error'})


@app.route("/api/fruit/<fruit_name>/<info>")
def get_fruit_info(fruit_name, info):
    API_ENDPOINT = f"https://www.fruityvice.com/api/fruit/{fruit_name}"
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        print("Success")
        return response.json()[info]
    if response.status_code == 404:
        print("Fruit not found")
        return json.dumps({'message': 'Fruit not found'})
    else:
        print("Error")
        return json.dumps({'message': 'Error'})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
