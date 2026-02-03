from collections import Counter # импортируем счетчик символов


with open('text.txt', 'r', encoding='utf-8') as f: # Читаем текст
    text = f.read()


letters = [ch.lower() for ch in text if 'a' <= ch.lower() <= 'z'] # Оставляем только английские буквы и приводим к нижнему регистру
total = len(letters) # получаем число элементов в объекте, чтобы расчитать потом долю.
counter = Counter(letters) # Считаем сколько какждая буква встречается раз в тексте
freq = [(letter, count / total) for letter, count in counter.items()] # создается Кортедж из буква, ее доля ( делим общее числ она частоту повторения)
freq.sort(key=lambda x: (-x[1], x[0])) # Сортировка по убыванию долей + по алфафиту если доли одинаковые

with open('analysis.txt', 'w', encoding='utf-8') as f: # создаем файл с нужным именем и записываем в него
    for letter, share in freq: # цикл каждая буква записывается и ее частота .3ф - окргуление до 3 символов
        f.write(f"{letter} {share:.3f}\n") #  /n преход на новую строку для следующей буквы