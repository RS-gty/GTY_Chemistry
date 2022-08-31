import re

a = ')15'
b = re.findall('[0-9]+', a)[0]
print(int(b))
