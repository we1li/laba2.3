def check_sequence(words):
    for word in words:
        if 'жы' in word or 'шы' in word:
            print(f'Найдено слово с неправильным буквосочетанием: {word}')

# Пример использования
input_sequence = ['живот', 'шыть', 'пожить', 'широкий']
check_sequence(input_sequence)
