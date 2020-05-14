import re
with open('tabacaria.txt') as _file:
    text = _file.read()

olha = re.search(r'Olha', text)
print(olha)

print(text[3467:3471])
