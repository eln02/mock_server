from flask import Flask, jsonify
import json

app = Flask(__name__)


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


@app.route('/offers', methods=['GET'])
def send_json():
    data = read_json_file('offers.json')
    return jsonify(data)


@app.route('/tickets_offers', methods=['GET'])
def send_json2():
    data = read_json_file('offers_tickets.json')
    return jsonify(data)


@app.route('/tickets', methods=['GET'])
def send_json3():
    data = read_json_file('tickets.json')
    return jsonify(data)


if __name__ == '__main__':
    app.run()
