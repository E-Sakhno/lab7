#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6 Для варианта задания определяемого по формуле , где - номер
# студента по списку преподавателя, лабораторной работы 6 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON. Необходимо проследить за
# тем, чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
# работы.


import sys
import json

if __name__ == '__main__':
    # Список полётов.
    flights = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'open':
            try:
                with open('result.json', 'r', encoding='utf-8') as f:
                    flights = json.load(f)
            except:
                print('Файл result.json не найден')

        elif command == 'save':
            with open("result.json", "w", encoding="utf-8") as f:
                json.dump(flights, f, ensure_ascii=False)
            print("Файл сохранен!")

        elif command == 'add':
            # Запросить данные о рейсах.
            destination = input("Пункт назначения? ")
            numb = input("Номер рейса? ")
            fl_type = input("Тип самолета? ")
            # Создать словарь.
            flight = {
                'destination': destination,
                'numb': numb,
                'fl_type': fl_type,
            }
            # Добавить словарь в список.
            flights.append(flight)
            # Отсортировать список в случае необходимости.
            if len(flights) > 1:
                flights.sort(key=lambda item: item.get('destination', ''))
        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 16
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^16} |'.format(
                    "№",
                    "Пункт назначения",
                    "Номер рейса",
                    "Тип самолета"
                )
            )
            print(line)
            # Вывести данные о всех рейсах.
            for idx, flight in enumerate(flights, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>16} |'.format(
                        idx,
                        flight.get('destination', ''),
                        flight.get('numb', ''),
                        flight.get('fl_type', 0)
                    )
                )
                print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            # Инициализировать счетчик.
            count = 0
            # Проверить сведения о рейсах из списка.
            for flight in flights:
                if flight.get('fl_type') == parts[1]:
                    count += 1
                    print(
                        '{:>4}: {}'.format(
                            count, flight.get('destination', ''))
                    )
            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Рейсы с заданным типом самолета не найдены")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <тип> - запросить рейсы с определенным типом самолета;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
