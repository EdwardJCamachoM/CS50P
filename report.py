
# Defines a dictionary and it values stored in a variable
def main():
    spacecraft = {"name" : "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01
    spacecraft.update({"distance": 0.02, "orbit": "Sun"})
    print(create_report(spacecraft))
    

# Returns the values of the variable using different methods
def create_report(spacecraft):
    return f"""
    =============== REPORT ===============
    
    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    
    ======================================
    """


main()