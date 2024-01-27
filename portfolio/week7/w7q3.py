'''3. Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.'''

def main():
    country_capitals = {}  # Dictionary to store country-capital pairs

    while True:
        country_name = input("Enter the name of a country (or 'exit' to quit): ").strip().capitalize()

        if country_name.lower() == 'exit':
            print("Exiting the program.")
            break

        if country_name in country_capitals:
            print(f"The capital of {country_name} is {country_capitals[country_name]}.")
        else:
            capital_name = input(f"Enter the capital of {country_name}: ").strip().capitalize()
            country_capitals[country_name] = capital_name
            print(f"{country_name} and its capital {capital_name} added to the list.")

if __name__ == "__main__":
    main()
