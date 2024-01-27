try:
    value = input("enter number")
    num = int(value)
    print ("that number squared is", num * num )
except ValueError:
    print("the value entered is not a number")