def check_pin(pin):
    # check if the pin is 4 digits
    if len(pin) != 4:
        return False

    # check if the pin is numeric
    if not pin.isdigit():
        return False

    return True

while True:
    pin = input("Please enter your 4-digit pin: ")
    if check_pin(pin):
        print("Correct pin!")
        break
    else:
        print("Error: Invalid pin. Please try again.")


'''----------
while True:
    try:
        in_v = int(input("pin: "))
        print("pin sucessful")
        break
    except:
        print("pin must be integer!")'''
