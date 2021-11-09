# author is Alyona Koryagina
# 10-11-2021
# python basics course
# lesson 3, exercise 6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    """Make first letter of word in uppercase"""
    n = 0
    for letter in word:
        if n == 0:
            new_word = letter.upper()
            n += 1
        else:
            new_word += letter
    return new_word


word_str = input('Print string of words: ')
new_str = ''
for one_word in word_str.split():
    new_str += f'{int_func(one_word)} '
print(new_str)
