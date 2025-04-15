from flask import Flask, jsonify
import random

app = Flask(__name__)

# Define initial state
state = {
    "round": 1,
    "defender_budget": 5000,
    "attacker_budget": 5000,
    "defender_score": 0,
    "attacker_score": 0,
    "districts": [
        {"name": "Business", "lights_on": True},
        {"name": "Hospital", "lights_on": True},
        {"name": "Fire/Police", "lights_on": True},
        {"name": "Industrial", "lights_on": True},
        {"name": "University", "lights_on": True},
        {"name": "Housing", "lights_on": True},
        {"name": "Fort Sam", "lights_on": True},
        {"name": "Traffic Lights", "lights_on": True},
    ]
}

def roll_dice():
    return random.randint(1, 6)

@app.route('/defend/<district>', methods=['GET'])
def defend(district):
    # Check if game is over
    if state["round"] > 10:
        return jsonify({"message": "Game Over"}), 400

    # Defend district
    district_to_defend = next((d for d in state["districts"] if d["name"] == district), None)
    if not district_to_defend:
        return jsonify({"message": "Invalid district"}), 400

    if roll_dice() <= 3:
        district_to_defend["lights_on"] = True
        state["defender_score"] += 1
        state["defender_budget"] -= 1000
        return jsonify(state)
    else:
        return jsonify(state)

@app.route('/attack/<district>', methods=['GET'])
def attack(district):
    # Check if game is over
    if state["round"] > 10:
        return jsonify({"message": "Game Over"}), 400

    # Attack district
    district_to_attack = next((d for d in state["districts"] if d["name"] == district), None)
    if not district_to_attack:
        return jsonify({"message": "Invalid district"}), 400

    if roll_dice() <= 3:
        district_to_attack["lights_on"] = False
        state["attacker_score"] += 1
        state["attacker_budget"] -= 1000
        return jsonify(state)
    else:
        return jsonify(state)

@app.route('/next_turn', methods=['GET'])
def next_turn():
    if state["round"] > 10:
        return jsonify({"message": "Game Over"}), 400
    else:
        state["round"] += 1
        return jsonify(state)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(state)

if __name__ == "__main__":
    app.run(debug=True)
