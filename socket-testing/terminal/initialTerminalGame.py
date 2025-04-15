import random  # Import random module for generating random numbers

# Initialize game state with districts, their compromise levels and light status
districts = {
    "Business": {"compromise": 0, "light": "On", "actions": []},
    "Hospital": {"compromise": 0, "light": "On", "actions": []},
    "Fire/Police": {"compromise": 0, "light": "On", "actions": []},
    "Industrial": {"compromise": 0, "light": "On", "actions": []},
    "University": {"compromise": 0, "light": "On", "actions": []},
    "Housing": {"compromise": 0, "light": "On", "actions": []},
    "Fort Sam": {"compromise": 0, "light": "On", "actions": []},
    "Traffic Lights": {"compromise": 0, "light": "On", "actions": []}
}

# Initialize budgets for defender and attacker
budget = {
    "defender": 50000,
    "attacker": 50000
}

# Define protection actions and their effect percentages
protection_actions = {
    "Firewall": 0.30,
    "Virus Protection": 0.15,
    "Intrusion Detection System": 0.25,
    "User Training": 0.20,
    "Turn Off Lights": 0
}

# Define hacking actions and their effect percentages
hacking_actions = {
    "Phishing": 0.35,
    "Virus": 0.25,
    "Malware": 0.20,
    "Skip Turn": 0
}

# Function to validate the input against a set of valid inputs
def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print(f"Invalid input! Please enter one of the following: {', '.join(valid_inputs)}")

# Main game loop
for i in range(10):
    print(f"\n--- Round {i+1} ---")

    # Defender's turn
    print("\nDefender's turn!")
    print(f"Budget: {budget['defender']}")

    # Ask defender how many locations they want to protect or turn off lights
    # If the defender presses Enter, they will skip their turn
    n_locations = input("How many locations do you want to protect or turn off lights (1-8, press Enter to skip turn): ")
    if n_locations.strip() != "":
        for _ in range(int(n_locations.strip())):
            # Defender selects protection action
            action = validate_input("Choose your action (Firewall, Virus Protection, Intrusion Detection System, User Training, Turn Off Lights): ", protection_actions.keys())
            # Defender selects district
            district = validate_input("Choose a district: ", districts.keys())

            # Calculate cost of action based on percentage of budget
            cost = int(budget['defender'] * protection_actions[action])
            # Subtract cost from budget
            budget['defender'] -= cost

            # Apply protection action to selected district
            if action != "Turn Off Lights":
                districts[district]['compromise'] -= cost * protection_actions[action]
                if districts[district]['compromise'] < 0.5:
                    districts[district]['light'] = "On"
            else:
                districts[district]['light'] = "Off"

            # Record the action taken
            districts[district]['actions'].append((i+1, 'defender', action))

    # Attacker's turn
    print("\nAttacker's turn!")
    print(f"Budget: {budget['attacker']}")

    # Ask attacker how many locations they want to hack
    # If the attacker presses Enter, they will skip their turn
    n_locations = input("How many locations do you want to hack (1-8, press Enter to skip turn): ")
    if n_locations.strip() != "":
        for _ in range(int(n_locations.strip())):
            # Attacker selects hacking action
            action = validate_input("Choose your action (Phishing, Virus, Malware, Skip Turn): ", hacking_actions.keys())
            # Attacker selects district
            district = validate_input("Choose a district: ", districts.keys())

            # Calculate cost of action based on percentage of budget
            cost = int(budget['attacker'] * hacking_actions[action])
            # Subtract cost from budget
            budget['attacker'] -= cost

            # Apply hacking action to selected district
            if action != "Skip Turn":
                districts[district]['compromise'] += cost * hacking_actions[action]
                if districts[district]['compromise'] > 0.5:
                    districts[district]['light'] = "Off"

            # Record the action taken
            districts[district]['actions'].append((i+1, 'attacker', action))

    # Show status after each turn
    print("\nAfter turn:")
    for district, status in districts.items():
        print(f"{district} lights are {status['light']}")

# End of game, show final actions taken
print("\n--- End of game ---")
for district, status in districts.items():
    print(f"\n{district} actions:")
    for action in status['actions']:
        print(f"Round {action[0]}: {action[1]} - {action[2]}")
