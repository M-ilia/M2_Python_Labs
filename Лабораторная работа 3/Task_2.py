# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, sep=','):
    first_group = set(first_group.split(sep))
    second_group = set(second_group.split(sep))
    print(first_group, second_group)
    output = list(first_group.intersection(second_group))
    output.sort()
    return output

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой
