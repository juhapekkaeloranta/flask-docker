from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized with live changes'

@app.route('/api/availability/station/<int:stationId>/time/<dateAndHour>', methods=['GET'])
def availability(stationId, dateAndHour):
    return jsonify(avlbikes=5,
                   date=dateAndHour,
                   stationId=stationId), 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
