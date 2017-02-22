import re

# regex to match words ending with ous
regex = r"[a-z]+ous\b"
text = "The marvellous mouse ran into the enormous house."

print(re.findall(regex, text))
