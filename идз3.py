def insert_letter(word, letter):
    index = word.find('и')
    if index != -1:
        new_word = word[:index+1] + letter + word[index+1:]
        return new_word
    else:
        return word

# Ввод слова и заданной буквы
input_word = input("Введите слово, оканчивающееся символом '.': ")
input_letter = input("Введите букву для вставки: ")

# Проверка наличия символа '.'
if input_word.endswith('.'):
    inserted_word = insert_letter(input_word, input_letter)
    print("Результат:", inserted_word)
else:
    print("Введенное слово не оканчивается символом '.'")
