#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    t = input("Введите букву: ")
    r = s.replace('и', 'и'+t, 1)
    print("Предложение после редактирования:", r)

