# Goal is to replace all occurances of a course with $
import re

data_path = "input1.txt"
f2 = open("input3.txt", "w")

with open(data_path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
for line in lines:
	print(line)
	line = re.sub('[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}', '$', line)
	x = 0
	while x < 100:
		f2.write(line)
		f2.write("\n")
		x+=1
        
f.close()
f2.close()