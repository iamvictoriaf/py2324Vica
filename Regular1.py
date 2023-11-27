import re
stroka = "Privet, mena zovut Vica, moi telefon 89112346578, a pochta pisma4vica@gmail.com, rabochiy telefon 8923456789"

result = re.match(r"Privet, mena zovut Vica", stroka)

print(result)
print(result.group(0))
print(result.start())
print(result.end())
########
result = re.search(r'telefon', stroka)
print(result)
print(result.group(0))

result = re.split(r'moi',stroka)
print(result)

#result = re.findall(r'telefon',stroka)
#print(result)

phones = re.findall(r'\b\d\d\d\d\d\d\d\b',stroka)
print(phones)
emails = re.findall(r'\w+@\w+\.\w+',stroka)
print(emails)