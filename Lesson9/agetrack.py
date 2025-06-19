def getage():
    userage = int(input("How old are you? "))

    if 0 <= userage <= 12:
        print("You are a child!")
    elif 13 <= userage <= 17:
        print("You are a teenager!")
    elif userage >= 18:
        print("You are an adult!")
    elif ValueError:
        print("")
        print("Please write down a number this time.")
        getage()       
    else:
        print("")
        print("Try again. Please input an appropriate age.")
        getage()

getage()