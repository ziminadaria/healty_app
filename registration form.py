def start_of_app():
    print("Welcome to the Healthy lifestyle application!")
    existing_account = input("Do you have an account? (yes/no): ")
    if existing_account == 'yes':
        main_menu(main_menu1)
    elif existing_account == 'no':
        add_to_data_base(registration_form())
        main_menu(main_menu1)


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


def registration_form():
    print("Please, fill in the registration form: ")
    while True:
        name = input("Enter your username: ")
        if name in data_base.keys():
            print("USERNAME ALREADY EXISTS. PLEASE CHOOSE ANOTHER ONE")
        else:
            break
    sex = input("Enter your sex (male/female): ")
    age = int(input("Enter your full age: "))
    weight = int(input("Enter your weight: "))
    height = int(input("Enter your height: "))
    lifestyle = input("Enter your type of lifestyle (active/not active): ")
    goal = input("Choose your goal (lose weight/gain weight/keep in shape): ")
    data = {"username": name, "sex": sex, "age": age, "weight": weight, "height": height, "lifestyle": lifestyle,
            "goal": goal}
    data_base[name] = data
    return data


def add_to_data_base(data):
    with open("data base.txt", 'a') as file:
        file.write("\n")
        for key in data:
            file.write(str(data[key]) + ",")


def username_identification():
    name = input("Please, enter your name. It should be unique: ")
    return name


def main_menu(dictionary):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        dictionary[choice1][1]()
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        main_menu(main_menu1)


def my_profile():
    name = username_identification()
    if name in data_base:
        info = data_base[name]
        for key, value in info.items():
            print(f'{key} - {value}')
        action = input('If you want to change your profile, print "yes" or print "back": ')
        if action == 'yes':
            take_action(profile_parameters)
        elif action == 'back':
            main_menu(main_menu1)
        else:
            print('Incorrect input. Try again!')
    else:
        print('Incorrect username. Try again!')
        my_profile()


def my_diet():
    pass


def my_training_plan():
    pass


def exit_programme():
    quit()


def lose_weight():
    main_menu(main_menu1)


def gain_weight():
    main_menu(main_menu1)


def keep_in_shape():
    main_menu(main_menu1)


def change_profile():
    main_menu(profile_parameters)


def take_action(dictionary):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        change_parameters(dictionary[choice1][1])
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        main_menu(main_menu1)


def change_parameters(key):
    pass


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
start_of_app()
