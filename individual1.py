#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 8. Написать программу, которая считывает текст из файла и выводит на экран только цитаты,
# то есть предложения, заключенные в кавычки.

if __name__ == '__main__':
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    quote = []
    for i in range (0, len(text)):
        if text[i] == '"':
            quote += [i]
    ind = 0
    while ind < len(quote):
        print(text[quote[ind]:quote[ind+1]+1])
        ind += 2




