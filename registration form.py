import os
from os.path import basename
import json

def take_data_from_database():
    data_base = {}
    with open("data base.txt", 'r') as file:
        for line in file:
            name = line.split(',')[0]
            sex = line.split(',')[1]
            age = int(line.split(',')[2])
            weight = int(line.split(',')[3])
            height = int(line.split(',')[4])
            lifestyle = line.split(',')[5]
            goal = line.split(',')[6]
            personal_data = dict(name=name, sex=sex, age=age, weight=weight, height=height, lifestyle=lifestyle,
                                 goal=goal)
            data_base[name] = personal_data
        return data_base


def registration_form(dbase):
    print("Please, fill in the registration form: ")
    while True:
        name = input("Enter your username: ")
        if name in dbase.keys():
            print("USERNAME ALREADY EXISTS. PLEASE CHOOSE ANOTHER ONE")
        else:
            break
    while True:
        sex = input("Enter your sex (male/female): ").strip().lower()
        if sex != 'male' and sex != 'female':
            print("Wrong input! Choose between two variants.")
        else:
            break
    while True:
        try:
            age = int(input("Enter your full age: "))
            break
        except ValueError:
            print("Wrong input. Write only integer numbers!")
    while True:
        try:
            weight = int(input("Enter your weight: "))
            break
        except ValueError:
            print("Wrong input. Write only integer numbers!")
    while True:
        try:
            height = int(input("Enter your height: "))
            break
        except ValueError:
            print("Wrong input. Write only integer numbers!")
    while True:
        lifestyle = input("Enter your type of lifestyle (active/not active): ").lower()
        if lifestyle != 'active' and lifestyle != 'not active':
            print("Wrong input! Choose between two variants.")
        else:
            break
    while True:
        goal = input("Choose your goal (lose weight/gain weight/keep in shape): ").lower()
        if goal != 'lose weight' and goal != 'gain weight' and goal != 'keep in shape':
            print("Wrong input! Choose between three variants.")
        else:
            break
    data = {"username": name, "sex": sex, "age": age, "weight": weight, "height": height, "lifestyle": lifestyle,
            "goal": goal}
    dbase[name] = data
    return data


def add_to_data_base(data):
    with open("data base.txt", 'a') as file:
        file.write("\n")
        for key in data:
            file.write(str(data[key]) + ",")


def username_identification(data):
    existing_account = input("Do you have an account? (yes/no): ").strip().lower()
    if existing_account == 'yes':
        while True:
            name1 = input("Please, enter your name: ")
            if name1 in data:
                break
            else:
                print("Username does not exist in data base. Please, try again.")
        return data[name1]
    elif existing_account == 'no':
        add_to_data_base(registration_form(data_base))
        print("Please, log in:")
        while True:
            name2 = input("Please, enter your name: ")
            if name2 in data:
                break
            else:
                print("Username does not exist in data base. Please, try again.")
        return data[name2]
    else:
        print("Wrong input. Please, try once again!")
        username_identification(data)


def main_menu(dictionary, username, dbase):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        dictionary[choice1][1](username, dbase)
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        main_menu(main_menu1, username, dbase)


def my_profile(username, dbase):
    for key, value in username.items():
        print(f'{key} - {value}')
    while True:
        action = input('If you want to change your profile, print "yes" or print "back": ').strip().lower()
        if action == 'yes':
            print("Choose what you want to change:")
            take_action(change_parameters, profile_parameters, dbase)
            break
        elif action == 'back':
            main_menu(main_menu1, username, dbase)
            break
        else:
            print('Incorrect input. Try again!')


def my_diet(username, dbase):
    print(f'Daily calories sum = {counting_daily_calories(username)}')
    main_menu(main_menu1, username, dbase)


def counting_daily_calories(username):
    daily_calories = int(username['weight']) * 9.99 + int(username['height']) * 6.25 - int(username['age']) * 4.92
    if username['sex'] == 'male':
        daily_calories += 5
    elif username['sex'] == 'female':
        daily_calories -= 161
    if username['lifestyle'] == 'active':
        daily_calories *= 1.46
    elif username['lifestyle'] == 'not active':
        daily_calories *= 1.2
    if username['goal'] == 'lose weight':
        daily_calories = 0.9 * daily_calories
    elif username['goal'] == 'gain weight':
        daily_calories = 1.1 * daily_calories
    print(int(daily_calories))
    return int(daily_calories)


def my_training_plan(username, dbase):
    filename = username['goal'] + ' ' + username['sex'] + '.json'
    for item in os.scandir('trainings'):
        if basename(item) == filename:
            with open(item) as file:
                 plan = json.load(file)
    trains(username, dbase, plan)
    print('HAVE A NICE TRAINING!')
    main_menu(main_menu1, username, dbase)
    return plan


def trains(username, dbase, personal_plan):
    for key, value in personal_plan.items():
        print(f'{key}:')
        for i in value:
            for key1, value1 in i.items():
                print(f'{key1} - {value1}')



def exit_programme(username, dbase):
    quit()


def lose_weight(username, dbase):
    main_menu(main_menu1, username, dbase)


def gain_weight(username, dbase):
    main_menu(main_menu1, username, dbase)


def keep_in_shape(username, dbase):
    main_menu(main_menu1, username, dbase)


def take_action(definition, dictionary, dbase):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        definition(dictionary[choice1][1], user, dbase)
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        take_action(change_parameters, profile_parameters, dbase)


def change_parameters(key, username, dbase):
    if type(username[key]) == int:
        while True:
            parameter = input(f'Please, choose another {key}: ')
            if parameter.isdigit():
                username[key] = int(parameter)
                dbase[username['name']] = username
                change_file(dbase)
                my_profile(username, dbase)
                break
            else:
                print('INCORRECT INPUT! TRY AGAIN!')
    else:
        if key == 'sex':
            while True:
                sex = input("Enter your sex (male/female): ")
                if sex != 'male' and sex != 'female':
                    print("Wrong input! Choose between two variants.")
                else:
                    username[key] = sex
                    dbase[username['name']] = username
                    change_file(dbase)
                    break
            my_profile(username, dbase)
        elif key == 'lifestyle':
            while True:
                lifestyle = input("Enter your type of lifestyle (active/not active): ")
                if lifestyle != 'active' and lifestyle != 'not active':
                    print("Wrong input! Choose between two variants.")
                else:
                    username[key] = lifestyle
                    dbase[username['name']] = username
                    change_file(dbase)
                    break
            my_profile(username, dbase)
        elif key == 'goal':
            while True:
                goal = input("Choose your new goal (lose weight/gain weight/keep in shape): ")
                if goal != 'lose weight' and goal != 'gain weight' and goal != 'keep in shape':
                    print("Wrong input! Choose between three variants.")
                else:
                    username[key] = goal
                    dbase[username['name']] = username
                    change_file(dbase)
                    break
            my_profile(username, dbase)


def change_file(dbase):
    count = len(dbase)
    with open('data base.txt', 'w') as f:
        for key in dbase:
            count -= 1
            for value in data_base[key].values():
                f.write(str(value) + ",")
            if count > 0:
                f.write('\n')


main_menu1 = {'1': ("1)See my profile", my_profile),
              '2': ("2)See my diet", my_diet),
              '3': ("3)See my training plan", my_training_plan),
              '4': ("4)Exit", exit_programme)
              }

goal = {'1': ("1)To lose weight", lose_weight),
        '2': ("2)To gain weight", gain_weight),
        '3': ("3)To keep in shape", keep_in_shape)
        }

profile_parameters = {'1': ("1)Sex", 'sex'),
                      '2': ("2)Age", 'age'),
                      '3': ("3)Weight", 'weight'),
                      '4': ("4)Height", 'height'),
                      '5': ("5)Lifestyle", 'lifestyle'),
                      '6': ("6)Goal", 'goal')
                      }
data_base = take_data_from_database()
print("Welcome to the Healthy lifestyle application!")
user = username_identification(data_base)
main_menu(main_menu1, user, data_base)
