money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0   # Количество месяцов

while True:
    delta = spend - salary

    if money_capital < delta:
        break

    money_capital -= delta
    spend += spend * increase
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
