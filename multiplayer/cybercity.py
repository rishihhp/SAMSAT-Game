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
            "Traffic Lights": {"light": "On"},
        }
        self.districts_effect = {
            "Business": {"effect": 0.0},
            "Hospital": {"effect": 0.0},
            "Fire/Police": {"effect": 0.0},
            "Industrial": {"effect": 0.0},
            "University": {"effect": 0.0},
            "Housing": {"effect": 0.0},
            "Fort Sam": {"effect": 0.0},
            "Traffic Lights": {"effect": 0.0},
        }
    def applyEffect(self, district, effect):
        self.districts_effect[district]['effect'] = effect + self.districts_effect[district]['effect']
    
    def compromiseEffect(self, district, effect):
        self.districts_effect[district]['effect'] = self.districts_effect[district]['effect'] - effect

    def turnOnLight(self, district):
        self.districts[district]['light'] = "On"

    def turnOffLight(self, district):
        print("s")
        self.districts[district]['light'] = "Off"

    def getStatus(self, district):
        return self.districts[district]['light']
    
    def getEffect(self, district):
        return self.districts_effect[district]['effect']

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
            print(f"{district} lights are {'On' if status['light'] == 'On' else 'Off'}")

    def status(self):
        status_text = "Cybercity status:\n"
        for district, data in self.districts.items():
            status_text += f"{district}: {'Lights On' if data['light'] == 'On' else 'Lights Off'}\n"
        return status_text

    def hackSuccessful(self, probability):
        a = random.random()
        print(a)
        return a < probability

    def hack(self, probability):
        if self.hackSuccessful(probability):
            print("Hacking successful!")
            for district in self.districts:
                self.turnOffLight(district)
        else:
            print("Hacking failed!")