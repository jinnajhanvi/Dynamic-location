from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/save-location', methods=['POST'])
def save_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f"Received coordinates: Latitude {latitude}, Longitude {longitude}")
    return jsonify({"status": "success", "latitude": latitude, "longitude": longitude})

if __name__ == '__main__':
    app.run(debug=True)
