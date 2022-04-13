
# ! Classroom  1
# size_global_matryoshka = 10

# def two_matryoshka():
#    size_matryoshka_two = 5
#    def three_matryoshka():
#        size_matryoshka_three = 3
#        return size_matryoshka_three + size_matryoshka_two
#    return three_matryoshka() + size_global_matryoshka
# print(two_matryoshka())
# ! Classroom  2
# global_var = []
# def add(name):
# 	global global_var
# 	global_var += name
# def remove(inx):
# 	global global_var
# 	del global_var[inx]
# for _ in range(7):
#    add(input("Add  text to list: "))
# for _ in range(2):
#    remove(int(input("Remove text to list: ")))
# print(global_var)
# ! task 1
# def foo():
#     global var
#     var = 'переменная foo'
#     print('переменная в foo: ', var)

#     def bar():
#         global var
#         var = 'переменная bar'
#     bar()
# foo()
# print('переменная в foo: ', var)

#! task 2
# x = "Я глобальная переменная!"
# def my_func():
#     global x
#     print(x)
#     x = "Я могу изменяться"
# my_func()
# print(x)
# print(globals())
#! task 3
# num = 3
# def mul():
#     global num
#     num = num**2
# mul()
# mul()
# mul()
# print(num)
#! task 4

# balance = 0
# def get_salary(amount):
# 	global balance
# 	balance = amount
# def pay_bills(amount, log_name):
# 	global balance
# 	balance = balance - amount
# 	print(f"Вы заплатили {amount} сом за {log_name}")

# def get_balance():
# 	global balance
# 	print(f"У вас на счету {balance} сом")

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

#! task 5
# result = 0;
# def pow_first(x,y):
# 	global result
# 	result = x**y
# def pow_second(z):
# 	global result
# 	result = result % z


# pow_first(2, 3)
# pow_second(3)
# print(result)

#! task 6
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# for key,val in a.items():
# 	if val >= 17:
# 		print(f"{key}, Вы можете войти в клуб")
# 	else:
# 		print(f"{key}, извините, Вы не проходите по age-control")
#! task 7
# a = ['pipi', 'papa', 'mama']
# b = [i.capitalize() for i in a]
# print(b)

#! task 8
# vowels = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
# consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
#               'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
# v = 0
# c = 0
# o = 0

# def count_symbols(text):
#     global v
#     global c
#     global o
#     text = list(text.lower())
#     for i in range(len(text)):
#         if text[i] in vowels:
#             v += 1
#         elif text[i] in consonants:
#             c += 1
#         else:
#             o += 1

#     return f"Количество гласных: {v}, согласных: {c}, остальных символов: {o}"

# print(count_symbols('Мурат супер!'))

# Количество гласных: 4, согласных: 6, остальных символов: 2
#! task 9
# a = []
# for i in range(11):
#     a.append(i)
# print(a)
#! task 10
# b = []
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# for i in a:
#     if i < 7:
#         b.append(str(i))

# b = "".join(b)
# print(b)
