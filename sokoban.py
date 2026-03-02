def main():

    history = []
    
    while True:
        action = input("Action: ")
        
        if action == "Undo" or action == "undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart" or action == "restart":
            history.clear()    
        else:
            history.append(action)
            print(history)

main()