# Automate Birthday Wishes Generator

![App Screenshot]()

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)

## Description
This program is designed to automate the process of sending birthday wishes via email 
to individuals whose birthdays are listed in a CSV file. The script reads the birthdays 
from the CSV file, matches them with the current date, and sends a personalized email 
if a birthday is found.

## Requirements
- Python 3.x
- `smtplib` library (standard library)
- An email account for sending notifications
- personalized csv file and template files

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/laurianerzb/automate_birthday_wisher.git
2. Navigate to the project directory:
   ```bash 
   cd automate_birthday_wisher
3. Replace "your@email.com" with your Gmail email address in the MY_EMAIL variable.
4. Provide your Gmail account password by replacing the empty string "" with your 
actual password provided by the two-factor authentication in the PASSWORD variable. 
Note: Storing passwords directly in your script is not recommended for security reasons. 
Consider using environment variables or a more secure method to store credentials.
5. Run the program
   ```bash
   python automate_wisher.py

## Usage

1. Ensure that the birthdays.csv file contains the list of birthdays with 
the following columns: name, email, month, and day. 
2. Ensure that you have a personalized wishing text

## Author
- [laurianerzb](https://github.com/laurianerzb)
