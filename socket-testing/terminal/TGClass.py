import random

class Cybercity:
    def __init__(self):
        self.districts = {
            "Business": {"light": "On"},
            "Hospital": {"light": "On"},
            "Fire/Police": {"light": "On"},
            "Industrial": {"light": "On"},
            "University": {"light": "On"},
            "Housing": {"light": "On"},
            "Fort Sam": {"light": "On"},
            "Traffic Lights": {"light": "On"}
        }

    def turnOnLight(self, district):
        self.districts[district]['light'] = "On"

    def turnOffLight(self, district):
        self.districts[district]['light'] = "Off"

    def getStatus(self, district):
        return self.districts[district]['light']

    def on(self):
        for district in self.districts:
            self.turnOnLight(district)

    def off(self):
        for district in self.districts:
            self.turnOffLight(district)

    def allRelaysOn(self):
        pass

    def allRelaysOff(self):
        pass

    def allPiRelaysOn(self, PiIP):
        pass

    def allPiRelaysOff(self, PiIP):
        pass

    def relayOn(self, PiIP, relayNo):
        pass

    def relayOff(self, PiIP, relayNo):
        pass

    def refresh(self):
        for district, status in self.districts.items():
            print(f"{district} lights are {status['light']}")

    def hackSuccessful(self, probability):
        return random.random() < probability

cybercity = Cybercity()

budget = {
    "defender": 50000,
    "attacker": 50000
}

protection_actions = {
    "Firewall": {"effect": 0.30, "probability": 0.7},
    "Virus Protection": {"effect": 0.15, "probability": 0.8},
    "Intrusion Detection System": {"effect": 0.25, "probability": 0.9},
    "User Training": {"effect": 0.20, "probability": 1.0},
    "Turn Off Lights": {"effect": 0, "probability": 1.0}
}

hacking_actions = {
    "Phishing": {"effect": 0.35, "probability": 0.7},
    "Virus": {"effect": 0.25, "probability": 0.8},
    "Malware": {"effect": 0.20, "probability": 0.9},
    "Skip Turn": {"effect": 0, "probability": 1.0}
}

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print(f"Invalid input! Please enter one of the following: {', '.join(valid_inputs)}")

for i in range(10):
    print(f"\n--- Round {i+1} ---")

    print("\nDefender's turn!")
    print(f"Budget: {budget['defender']}")

    n_locations = input("How many locations do you want to protect or turn off lights (1-8, press Enter to skip turn): ")
    if n_locations.strip() != "":
        for _ in range(int(n_locations.strip())):

            action = validate_input("Choose your action (Firewall, Virus Protection, Intrusion Detection System, User Training, Turn Off Lights): ", protection_actions.keys())

            district = validate_input("Choose a district: ", cybercity.districts.keys())

            cost = int(budget['defender'] * protection_actions[action]["probability"])

            budget['defender'] -= cost

            if action != "Turn Off Lights":
                cybercity.turnOnLight(district)
            else:
                cybercity.turnOffLight(district)


    print("\nAttacker's turn!")
    print(f"Budget: {budget['attacker']}")

    n_locations = input("How many locations do you want to hack (1-8, press Enter to skip turn): ")
    if n_locations.strip() != "":
        for _ in range(int(n_locations.strip())):

            action = validate_input("Choose your action (Phishing, Virus, Malware, Skip Turn): ", hacking_actions.keys())

            district = validate_input("Choose a district: ", cybercity.districts.keys())

            cost = int(budget['attacker'] * hacking_actions[action]["probability"])

            budget['attacker'] -= cost

            if action != "Skip Turn":
                if cybercity.hackSuccessful(hacking_actions[action]["probability"]):
                    cybercity.turnOffLight(district)

    print("\nAfter turn:")
    cybercity.refresh()

print("\n--- End of Game ---")
