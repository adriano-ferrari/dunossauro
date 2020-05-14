import re
with open('tabacaria.txt') as _file:
    text = _file.read()

olha = re.findall('olha', text)

print(olha)
