#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6 Для варианта задания определяемого по формуле , где - номер
# студента по списку преподавателя, лабораторной работы 8 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON. Необходимо проследить за
# тем, чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
# работы.

# Написать программу, которая считывает текст из файла и выводит на экран только
# предложения, не содержащие запятых.


import json

if __name__ == '__main__':
    result = []
    with open('text.json', 'r', encoding='utf-8') as f:
        text = json.load(f)

    d_items = text.values()
    for value in d_items:
        # Заменить символы конца предложения.
        value = value.replace("!", ".")
        value = value.replace("?", ".")

        # Удалить все многоточия.
        while ".." in value:
            value = value.replace("..", ".")

        # Разбить текст на предложения.
        sentences = value.split(".")
        # Вывод предложений с запятыми.
        for sentence in sentences:
            if "," not in sentence:
                result += [sentence]
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)


    
