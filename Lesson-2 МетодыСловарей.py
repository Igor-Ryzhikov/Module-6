small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}
big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)
name = input("Введите название товара: ")
if big_storage.get(name, None):
    print(big_storage[name])
else:
    print("Такого товара нет!")


incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
summ = 0
min_value = None
min_name = " "
for name, value in incomes.items():
    summ += value
    if min_value is None or min_value > value:
        min_value = value
        min_name = name
incomes.pop(min_name)
print("Общий доход за год составил:", summ)
print("Самый маленький доход у {0}. Он составляет {1} рублей".format(min_name, min_value))
print("Итоговый словарь:", incomes)


text = input("Введите текст: ").lower()
histogram = dict()

for symbol in text:
    if symbol in histogram:
        histogram[symbol] += 1
    else:
        histogram[symbol] = 1

for letter, freq in sorted(histogram.items()):
    print(letter, ":", freq)

print("Максимальная частота: ", max(histogram.values()))