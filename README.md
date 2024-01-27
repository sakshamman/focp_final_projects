----TASK1:----
## Pizza Price Calculator
1.Run the Program:
python pizza_calculator.py

2.Follow the on-screen prompts to input the required information.

#Input Information:

Enter the number of pizzas you want to order.
Specify whether delivery is required (Y/N).
Indicate if it's Tuesday (Y/N).
Confirm if the customer used the app for the order (Y/N).
View Results:
The program will display the total price of the pizzas based on your inputs, considering any applicable discounts or delivery costs.

#Program Structure
The program consists of two main functions:

1.get_user_input: Responsible for getting valid user input, ensuring positive integers for the number of pizzas and valid responses for delivery, Tuesday, and app usage.

2.calculate_total_price: Performs the calculations for the total pizza price, considering pizza pricing, delivery costs, and discounts.


----TASK2:----
## Cat Logs
1.Run the Program:
python analyze_log.py path/to/cat_log_file.txt

2.Replace path/to/cat_log_file.txt with the actual path to your cat log file.

# View Analysis Results:
The program will display various statistics based on the provided log file, including the total number of cat visits, durations, and averages.

# Log File Format
The log file should be a text file where each line represents a cat visit entry in the following format:

# Copy code
cat_name,entry_time,departure_time
Ensure each entry is separated by commas, and the file should end with a line containing only the word 'END' to signal the end of the log.

# Program Output
The analysis results will include:

Total cat visits
Total visits by other cats
Total time cats spent in the house
Average visit length
Longest visit duration
Shortest visit duration


----TASK3:----
## User Management Utility for Password File

This Python repository provides a simple user management system for a password file, with four command-line programs: `adduser.py`, `deluser.py`, `passwd.py`, and `login.py`. The password file includes username, real name, and encrypted passwords, with encryption implemented using the ROT-13 algorithm.

### Scripts

1. **adduser.py**: Adds a new user to the password file, encrypting the password using ROT-13.
2. **deluser.py**: Removes a user from the password file based on the provided username and password.
3. **passwd.py**: Allows users to change their password, re-encrypting it using ROT-13.
4. **login.py**: Checks user credentials against the password file to grant or deny access.

### Utility Module

The `password_utils.py` module includes common functions such as hashing passwords and handling user input securely.

### Encryption

The passwords in the password file are "encrypted" using the ROT-13 algorithm, chosen for simplicity in this example.

### Usage

To execute any of the scripts, run them from the command line. Each script provides interactive prompts for necessary inputs.

### Important Note

ROT-13 encryption used here is not suitable for actual security. In real-world scenarios, a more robust hashing algorithm should be employed.


---- Portfolio file only contains the weekly practices of python ----

