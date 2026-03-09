try:
    mood = int(input("Rate your mood between (0-10):"))
    if mood< 0 or mood <=3:
        print("sad")
    elif mood>3 and mood<=6:
        print("normal")
    elif mood>6 and mood<=10:
        print("happy")
    else:
        print("rate between 0-10")
except ValueError:
    print("invalid input")
    
