import re
count=0
matcher =re.finditer("[^a-zA-Z0-9]","a@bklm7")
for m in matcher:
    print(m.start(),"---", m.group())
    
