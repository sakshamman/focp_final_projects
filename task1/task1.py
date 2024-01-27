#checking if the user input is valid as the assignment 
def get_user_input(prompt, data_type= int):
    while True:
        try:
            user_input = data_type(input(prompt))
            if data_type == int and user_input <= 0:
                raise ValueError("Please enter a positive integer!")
            elif data_type == str and user_input.lower() not in ['y', 'n']:
                raise ValueError('Please answer "Y" or "N".')
            return user_input
        except ValueError as e:
            print(e)

#function to calcuate total pizza price
def calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app):
    #constants for pizza pricing, delivery cost, and discounts
    pizza_price = 12
    delivery_cost = 2.5
    app_discount = 0.25
    tuesday_discount = 0.5

    #calculation of total pizza price without discounts
    total_pizza_price = num_pizzas * pizza_price

    #giving the conditions to add the toal price 
    if is_tuesday:
        total_pizza_price *=0.5   # applying 50% discount on tuesday

    if is_delivery and num_pizzas < 5:
        total_pizza_price += delivery_cost    #adding delivery cost if required

    if used_app:
        total_pizza_price *= (1 - app_discount)    #applying 25% app discount 

    return round(total_pizza_price, 2)

#main functions to run the pizza price calculator
def main():
    print("BPP Pizza Price Calculator\n==========================\n")

    num_pizzas = get_user_input("How many pizzas ordered? ")
    is_delivery = get_user_input("Is delivery required? (Y/N) ", str).lower() == 'y'
    is_tuesday = get_user_input("Is it Tuesday? (Y/N) ", str).lower() == 'y'
    used_app = get_user_input("Did the customer use the app? (Y/N) ", str).lower() == 'y'

    total_price = calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()
