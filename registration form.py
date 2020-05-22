def start_of_app():
    print("Welcome to the Healthy lifestyle application!")
    existing_account = input("Do you have an account? (yes/no): ")
    if existing_account == 'yes':
        main_menu(main_menu1)
    elif existing_account == 'no':
        add_to_data_base(registration_form())
        print('Choose your goal: ')
        main_menu(goal)


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
            personal_data = dict(name=name, sex=sex, age=age, weight=weight, height=height, lifestyle=lifestyle)
            data_base[name] = personal_data
    return data_base


def registration_form():
    data_base = take_data_from_database()
    print(" Please, fill in the registration form: ")
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
    data = {"username": name, "sex": sex, "age": age, "weight": weight, "height": height, "lifestyle": lifestyle}
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
    data_base = take_data_from_database()
    for key in data_base.keys():
        if key == name:
            print(data_base[key])


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


main_menu1 = {'1': ("1)See my profile", my_profile),
              '2': ("2)See my diet", my_diet),
              '3': ("3)See my training plan", my_training_plan),
              '4': ("4)Exit", exit_programme)
              }

goal = {'1': ("1)To lose weight", lose_weight),
        '2': ("2)To gain weight", gain_weight),
        '3': ("3)To keep in shape", keep_in_shape)
        }

start_of_app()
