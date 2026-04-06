Safety_Levels = {
    75:"medium",
    77:"high",
    78:"high",
    91:"medium",
    92:"medium",
    93:"low",
    94:"medium",
    95:"medium",
}

def get_safety_level(departement):
    return Safety_Levels.get(departement, "Medium")