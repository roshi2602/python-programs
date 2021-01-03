import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaabababab")
for match in matcher:
    count=count+1
    print("dd", match.start())
print("cod"count)
