order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

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
for fruit_name in order:
    cost = incomes.get(fruit_name, 0) * order[fruit_name]
    summ += cost
print('Итоговая стоимость товаров из заказа составляет:', summ)


players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
status_dict = {
    "Rest": "отдыхают",
    "Training": "тренируются",
    "Travel": "путешествуют"
}
command = ["A", "B", "C"]
index = 0
for state in status_dict:
    print(f"Все члены команды {command[index]}, которые {status_dict[state]}:")
    for _, player in players_dict.items():
        if player["status"] == state and player["team"] == command[index]:
            print(player["name"])
    index += 1

