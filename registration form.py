def take_data_from_database():
    data_base = {}
    with open("data base.txt", 'r') as file:
        for line in file:
            name = line.split(',')[0]
            sex = line.split(',')[1]
            age = line.split(',')[2]
            weight = line.split(',')[3]
            height = line.split(',')[4]
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
        sex = input("Enter your sex (male/female): ")
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
        lifestyle = input("Enter your type of lifestyle (active/not active): ")
        if lifestyle != 'active' and lifestyle != 'not active':
            print("Wrong input! Choose between two variants.")
        else:
            break
    while True:
        goal = input("Choose your goal (lose weight/gain weight/keep in shape): ")
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
    existing_account = input("Do you have an account? (yes/no): ")
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
        username_identification(data_base)


def main_menu(dictionary, username):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        dictionary[choice1][1](username)
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        main_menu(main_menu1, user)


def my_profile(user):
    for key, value in user.items():
        print(f'{key} - {value}')
    while True:
        action = input('If you want to change your profile, print "yes" or print "back": ')
        if action == 'yes':
            print("Choose what you want to change:")
            take_action(change_parameters, profile_parameters)
            break
        elif action == 'back':
            main_menu(main_menu1, user)
            break
        else:
            print('Incorrect input. Try again!')


def my_diet(user):
    print(f'Daily calories sum = {counting_daily_calories(user)}')
    main_menu(main_menu1, user)


def counting_daily_calories(user):
    daily_calories = int(user['weight']) * 9.99 + int(user['height']) * 6.25 - int(user['age']) * 4.92
    if user['sex'] == 'male':
        daily_calories += 5
    elif user['sex'] == 'female':
        daily_calories -= 161
    if user['lifestyle'] == 'active':
        daily_calories *= 1.46
    elif user['lifestyle'] == 'not active':
        daily_calories *= 1.2
    if user['goal'] == 'lose weight':
        daily_calories = 0.9 * daily_calories
    elif user['goal'] == 'gain weight':
        daily_calories = 1.1 * daily_calories
    print(int(daily_calories))
    return int(daily_calories)


def my_training_plan(user):
    pass


def exit_programme(user):
    quit()


def lose_weight(user):
    main_menu(main_menu1, user)


def gain_weight(user):
    main_menu(main_menu1, user)


def keep_in_shape(user):
    main_menu(main_menu1, user)


def change_profile():
    main_menu(profile_parameters, user)


def take_action(definition, dictionary):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        definition(dictionary[choice1][1], user)
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        take_action(change_parameters, profile_parameters)


def change_parameters(key, username):
    username[key] = input(f'Please, choose another {key}: ')
    pass
    #подумать над типом переменным + над сортировкой (например, чтобы принималось только male&female и т.д.)


main_menu1 = {'1': ("1)See my profile", my_profile),
              '2': ("2)See my diet", my_diet),
              '3': ("3)See my training plan", my_training_plan),
              '4': ("4)Exit", exit_programme)
              }

goal = {'1': ("1)To lose weight", lose_weight),
        '2': ("2)To gain weight", gain_weight),
        '3': ("3)To keep in shape", keep_in_shape)
        }

profile_parameters = {'1': ("1)Username", 'name'),
                      '2': ("2)Sex", 'sex'),
                      '3': ("3)Age", 'age'),
                      '4': ("4)Weight", 'weight'),
                      '5': ("5)Height", 'height'),
                      '6': ("6)Lifestyle", 'lifestyle'),
                      '7': ("7)Goal", 'goal')
                      }

data_base = take_data_from_database()
print("Welcome to the Healthy lifestyle application!")
user = username_identification(data_base)
main_menu(main_menu1, user)
