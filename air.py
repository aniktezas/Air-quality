def interpret(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    else:
        return "Unhealthy"
print(interpret(30))  # Output: Good
print(interpret(75))  # Output: Moderate
print(interpret(150)) # Output: Unhealthy       