text = input()

count = 0

for i in text.lower():
    if i in "aeiou":
        count+=1
        
print(count)      