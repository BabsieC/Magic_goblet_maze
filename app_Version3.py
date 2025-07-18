from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def analyze_symptoms(symptoms):
    recommendations = []
    if 'tired' in symptoms.lower():
        recommendations.append("Increase intake of iron-rich foods like spinach and lentils.")
    if 'headache' in symptoms.lower():
        recommendations.append("Drink more water and reduce caffeine.")
    if not recommendations:
        recommendations.append("Eat a balanced diet with plenty of vegetables, fruits, and whole grains.")
    return recommendations

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    recommendations = analyze_symptoms(message)
    return jsonify({
        "response": "Based on your symptoms, here are some dietary recommendations:",
        "recommendations": recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)