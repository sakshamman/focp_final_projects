'''5. Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!
'''

import sys

def process_temperatures(temperatures):
    if not temperatures:
        print("No temperatures provided.")
        return

    try:
        temperatures = list(map(float, temperatures))
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)

        print(f"Maximum Temperature: {max_temp}")
        print(f"Minimum Temperature: {min_temp}")
        print(f"Mean Temperature: {mean_temp}")
    except ValueError:
        print("Invalid temperature value. Please provide numerical values.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_temperatures_cmd.py <temperature1> <temperature2> ...")
    else:
        temperature_values = sys.argv[1:]
        process_temperatures(temperature_values)
