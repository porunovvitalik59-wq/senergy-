
number = int(input("Введите пятизначное целое число: "))

# Извлекаем цифры по разрядам
units = number % 10                         # единицы
tens = (number // 10) % 10                # десятки
hundreds = (number // 100) % 10           # сотни
thousands = (number // 1000) % 10         # тысячи
tens_of_thousands = number // 10000       # десятки тысяч

# Выполняем вычисления по условию
step_1 = tens ** units                    # возводим десятки в степень единиц
step_2 = step_1 * hundreds                # умножаем на количество сотен
denominator = tens_of_thousands - thousands  # разность десятков тысяч и тысяч
result = step_2 / denominator             # делим (результат — вещественное число)

print(result)