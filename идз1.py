def print_letters(sentence):
    for letter in sentence:
        if letter.lower() == 'м' or letter.lower() == 'н':
            print(letter)

# Пример использования
input_sentence = "Дано предложение. Вывести все буквы м и н в нем."
print_letters(input_sentence)
