from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS

API_KEY = "122fb48ddec9be86c4b9bd451a2e5a0e"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City not provided"}), 400
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Weather API error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)