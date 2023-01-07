import pandas
import smtplib
from datetime import datetime
import random


# Check if today matches a birthday in the birthdays.csv
# Create a tuple from today's month and day using datetime
today = (datetime.now().month, datetime.now().day)

# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

my_email = "pythontestberry@gmail.com"
# password from app generator on gmail
password = "dluhzayjhamxzxbj"

# Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
# Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
# data_row is the name of the whole row of data...e.g. Daddy,macb12@msn.com,1958,1,7...the first part was breaking
# down by only month and day and calling iterrows to iterate over each row
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


# Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
# If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace
# the [NAME] with the person's actual name from birthdays.csv
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    random_letter = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_letter}.txt"
    # opening the letters and reading whole document to replace default NAME with the person's name with the
    # birthday today
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        # connect to smtp provider
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # start transport layer security to secure the connection to the email server
        connection.starttls()
        # login process
        connection.login(user=my_email, password=password)
        # sending the email from one address to the other with message...adding subject and /n to make
        # sure it doesn't go into spam box...passing in contents variable with the modified name of the
        # person's birthday
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")






