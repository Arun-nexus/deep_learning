n = int(input("Enter the number of strings: "))
strings = []

for i in range(n):
    strings.append(input("Enter string "))


common = strings[0]


for i in range(1, len(strings)):
    temp = ""
    for j in range(min(len(common), len(strings[i]))):
        if common[j] == strings[i][j]:
            temp += common[j]
        else:
            break
    common = temp 
    if not common:  
        break

if common:
    print("Common prefix:", common)
else:
    print("Nothing is common.")
