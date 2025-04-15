# 🛡️ Battle for Cyber City

**An educational cybersecurity game that teaches real-world digital defense through strategy, simulation, and fun.**

---

## 🌟 Overview

Welcome to **Battle for Cyber City**, an interactive turn-based game designed to teach **underprivileged students** the fundamentals of **cybersecurity**. Set in a vibrant cityscape, players take on the role of either a **defender** protecting key infrastructure or a **hacker** trying to compromise it. Each round is a battle of budget, brains, and dice-based luck as players choose how to spend their resources to outwit the opponent.

This project is part of a broader initiative to make cybersecurity education accessible, engaging, and fun for all.

---

## 🎯 Game Objective

- Defenders aim to **protect Cyber City's districts** using tools like Firewalls and User Training.
- Attackers try to **compromise those districts** using methods like Phishing and Malware.
- Each side starts with a limited **budget** and must make strategic decisions across **10 rounds**.

---

## 🗺️ Districts of Cyber City

- Business  
- Hospital  
- Fire/Police  
- Industrial  
- University  
- Housing  
- Fort Sam  
- Traffic Lights  

Each district represents real-world infrastructure and is visually represented by **lights on/off** to show compromise status.

---

## 🛡️ Defender Actions

| Protection Type         | Effectiveness |
|-------------------------|---------------|
| Firewall                | 30%           |
| Virus Protection        | 15%           |
| Intrusion Detection     | 25%           |
| User Training           | 20%           |

---

## 🐍 Hacker Actions

| Hack Type      | Success Rate |
|----------------|--------------|
| Phishing       | 35%          |
| Virus          | 25%          |
| Malware        | 20%          |

---

## 🔁 Game Mechanics

- 🔟 **Rounds**: 10 rounds per game
- 💰 **Budgets**: Each player starts with $5,000
- 🎲 **Dice Rolls** determine success or failure of actions
- 💡 **Lights On/Off** visually indicate control over districts
- 🎮 **Turn Order**: Defender starts each round, attacker follows

---

## 🧠 Educational Value

This project teaches:
- Cybersecurity fundamentals (phishing, firewalls, malware, etc.)
- Critical thinking and budget management
- The real-world impact of cyber attacks on public infrastructure
- Team-based decision making and resilience

---

## 🛠️ Technologies Used

- **Python (Terminal Version)**: Core game logic
- **Flask (Web App Version)**: REST API for gameplay in a browser
- **Random module**: Dice roll simulations
- **GET Endpoints** for simple HTTP-based gameplay

---

## 🚀 How to Play (Web Version)

### ▶️ Start the Flask App

```bash
python app.py
