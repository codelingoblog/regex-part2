import re

# regex to match Washington D.C phone numbers

regex = r"\b202\-\d{3}\-\d{4}"

file = open("phone_numbers.txt", "r")
phonenumbers = file.read()

print(re.findall(regex, phonenumbers))

