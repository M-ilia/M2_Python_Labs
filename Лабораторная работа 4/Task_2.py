# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"



def task(file, out) -> None:

    with open(file) as f:  # TODO считать содержимое csv файла
        list_ = [i for i in csv.DictReader(f)]

    with open(out, 'w', encoding='utf8') as f_out:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(list_, f_out, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
