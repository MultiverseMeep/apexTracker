import re

oldstring = "-19369.75.23708."

newstring = re.sub("\\.\\d\\d\\.", " ", oldstring)
print(newstring)