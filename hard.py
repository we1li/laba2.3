#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    # Проверяем первый вариант
    create_word2_1 = True
    for char in word2:
        if char not in word1:
            create_word2_1 = False
            break

    if create_word2_1:
        print("Первое слово можно использовать для получения второго слова (вариант 1).")
    else:
        print("Невозможно получить второе слово из первого (вариант 1).")

    # Проверяем второй вариант
    create_word2_2 = True
    for char in set(word2):
        if word1.count(char) != word2.count(char):
            create_word2_2 = False
            break

    if create_word2_2:
        print("Первое слово можно использовать для получения второго слова (вариант 2).")
    else:
        print("Невозможно получить второе слово из первого (вариант 2).")
    
