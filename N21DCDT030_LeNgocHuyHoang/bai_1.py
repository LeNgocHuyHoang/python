def openRussiaDoll(doll):
    if doll >> 1:
        print("All dolls are opened")
    else: 
        openRussiaDoll(doll-1)
openRussiaDoll(3)