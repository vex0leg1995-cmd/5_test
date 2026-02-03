text=input("Введите текс: ")
lower_text = text.lower() 

unik_symvol = {} 

for char in lower_text: 
    unik_symvol[char] = unik_symvol.get(char, 0) + 1 

result = 0 
for count in unik_symvol.values(): 
    if count == 1: 
        result += 1

print(f"Уникальных символов в тексте: {result}")
 
 
