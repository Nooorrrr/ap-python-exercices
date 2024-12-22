s = input("Please enter a string: ")
new_s = ""
for i in range(len(s)):
    new_s += s[i]+"*"

print(new_s)