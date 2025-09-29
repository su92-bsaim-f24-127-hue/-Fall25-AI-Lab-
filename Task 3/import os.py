import os
class ReflexAgent:
    def __init__(self, Temp, file = "memory.txt"):
        self.Temp = Temp
        self.file = file
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                f.write("Temperature,Action\n")
                
    def check_memory(self, current_temperature):
        with open(self.file, "r") as f:
            lines = f.readlines()[1:] 
            for line in lines:
                temp, action = line.strip().split(",")
                
                if int(temp) == current_temperature:
                    return action  
        return None
    def update_history(self, current_temperature, action):
        with open(self.file,"a") as f:
            f.write(f"{current_temperature},{action}\n")
    
    def act(self, current_temperature):
        action = self.check_memory(current_temperature)
        if action:
            return f"(From Memory) {action}"
        if current_temperature < self.Temp:
            action = "Turn off AC"
        else:
            action = "Turn on AC"
        self.update_history(current_temperature, action)
        return f"(Calculated) {action}"

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 25,
    "Garage": 21
}

Temp = 20
agent = ReflexAgent(Temp)
for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C.{action}.")
