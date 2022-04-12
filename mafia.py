# import random


# print("\t\tЭто игра мафия")
# number_of_players = int(input("Введите количества игроков: "))
# print("\t1.Мафия \t\t 2.Доктор \t\t 3.Коп \t\t 4.Мирный житель")
# user_choice = int(input("Кто вы хотите быть: "))
# result = {i for i in range(1, number_of_players+1) if i % 5 == 0}
# number_of_mafia = len(result)
# doctor = 1
# police = 1
# number_of_people = number_of_players - number_of_mafia - doctor - police
# people  = dict.fromkeys(range(1,number_of_people+1), None)
# list_ = {i for i in range(number_of_people)}
# for k,v in people.items():
#     n = random.sample(list_, list_)
#     people[k] = n
# print(people)
# # print(f"Количества: \t Мафия : {number_of_mafia}  Мирный житель: {number_of_people} \t Доктор:{doctor} \t Коп: {police}\t")
import random
try:
    amount_players = int(input("Сколько игроков в игре? "))
    if amount_players < 10:
        raise ValueError
except (ZeroDivisionError, ValueError, TypeError, NameError):
    print("Напишите только цифры от 10 - 30 у вас есть 1 попытка")
    amount_players = int(input("Сколько игроков в игре? "))
if amount_players <= 9:
    raise ValueError("Ошибка")
elif amount_players <= 10:
    count_victims = 1
elif amount_players <= 20:
    count_victims = 2
elif amount_players <= 30:
    count_victims = 3
else:
    print("Нельзя вводит больше у вас есть 1 попытка")
    amount_players = int(input("Сколько игроков в игре? "))
    if amount_players > 30:
        raise ValueError("Ошибка")
try:
    amount_mafia = int(input("Сколько мафий в игре? "))
    if amount_mafia > count_victims+count_victims:
        raise ValueError
except (ZeroDivisionError, ValueError, TypeError, NameError):
    print(f"Напишите только цифры от 1 - {count_victims+count_victims}")
    amount_mafia = int(input("Сколько мафий в игре? "))
    if amount_mafia > (count_victims+count_victims):
        raise ValueError("Ошибка")

print("\t1.Мафия \t\t 2.Доктор \t\t 3.Коп \t\t 4.Мирный житель")
try:
    user_choice = int(input("Кто вы хотите быть: "))
except (ValueError, ZeroDivisionError, NameError, TypeError):
    print("Введите только чисел и не ноль")
    user_choice = int(input("Кто вы хотите быть: "))

players = list(range(1, amount_players + 1))
random.shuffle(players)

mafia = [players.pop() for _ in range(amount_mafia)]
doctor = players.pop()
detective = players.pop()
inhabitants = players

if user_choice == 1:
    bul = 1
    Id_user = mafia[0]
    print(f"Вы мафия. Ваш id : {Id_user}")
    print("Мафией(ями) являются игроки:", sorted(mafia))
elif user_choice == 2:
    bul = 2
    Id_user = doctor
    print(f"Вы доктор. Ваш id : {Id_user}")
    print("Доктором является игрок:", doctor)
elif user_choice == 3:
    bul = 3
    Id_user = detective
    print(f"Вы детектив Ваш id : {Id_user}")
    print("Детективом является игрок:", detective)
elif user_choice == 4:
    bul = 4
    Id_user = inhabitants[0]
    print(f"Вы мирный житель Ваш id : {Id_user}")
inhabitants.append(detective)
inhabitants.append(doctor)
inhabitants = inhabitants + mafia
while True:
    if bul == 1:
        print("Мафией(ями) являются игроки:", sorted(mafia))
        print("\t", *sorted(inhabitants for inhabitants in inhabitants if not inhabitants in mafia))
        try:
            choosing_victims = input(
                f"Выберите {count_victims} жертву через пробел: ").split()
            if len(choosing_victims) > count_victims:
                raise ValueError()
        except (ValueError, ZeroDivisionError, NameError, TypeError):
            print(
                f"Введите только {count_victims} чисел c пробелами больше нелзя")
            choosing_victims = input(f"Выберите {count_victims} жертву через пробел: ").split()
				
        container = choosing_victims

        for i in container:
            doctor_choice = random.sample(inhabitants, 1)
            if doctor_choice != i:
                inhabitants.remove(int(i))
                doctor_failed = 1
            else:
                doctor_failed = 0

        detective_choice = random.sample(inhabitants, 1)
        inhabitants_choice = random.sample(inhabitants, 1)
        inhabitants.remove(int(*inhabitants_choice))
        if int(*inhabitants_choice) in mafia:
            inhabitants_find = True
            mafia.remove(int(*inhabitants_choice))
        else:
            inhabitants_find = False

        print(f"Мафия убил: {container}")
        if doctor_failed == 0:
            print(f"Доктор попал")
        else:
            print(f"Доктор не попал")

            print(f"Коп подозреваеть: {detective_choice}")
        if inhabitants_find == True:
            print(f"Жители убили: мафию{inhabitants_choice}")
        else:
            print(f"Жители убили: мирного жителя {inhabitants_choice}")
        if (len(inhabitants)-len(mafia)) <= len(mafia):
            print("Мафия победили")
            break
        if not mafia:
            print("Вас убили Жители победили")
            break
    elif bul == 2:
        inhabitants = inhabitants + mafia
        inhabitants.remove(doctor)
        print(sorted(inhabitants))
        choosing_patient = input("Какого номера вы хотите вылечить: ")
    elif bul == 3:
        inhabitants = inhabitants + mafia
        inhabitants.remove(detective)
        print(sorted(inhabitants))
        choosing_patient = input("Какого номера вы подозреваете: ")
