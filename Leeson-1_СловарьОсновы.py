# num = int(input("Введите целое число: "))
# number = dict()
#
# for i_num in range(1, num + 1):
#     number[i_num] = i_num ** 2
#
# print(number)
#
# student_str = input("Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки):")
# student_info = student_str.split()
#
# student = dict()
#
# student["Имя"] = student_info[0]
# student["фамилия"] = student_info[1]
# student["город"] = student_info[2]
# student["место учёбы"] = student_info[3]
# student["оценки"] = []
# for i_grade in student_info[4:]:
#     student["оценки"].append(int(i_grade))
# for i_info in student:
#     print(i_info, "-", student[i_info])

phone_book = dict()
while True:
    print("Текущие контакты на телефоне:")
    if phone_book:
        for name in phone_book:
            print(name, phone_book[name])
    else:
        print("Пусто")
    new_contact = input("Введите имя (для остановки введите пустую строку): ")
    new_teleph = int(input("Введите номер телефона: "))
    if new_contact in phone_book:
        print("Ошибка: такое имя уже существует.")
    else:
        phone_book[new_contact] = new_teleph