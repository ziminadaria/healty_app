import os
from os.path import basename
import json
from bs4 import BeautifulSoup
import requests
import random


def take_data_from_database():
    data_base = {}
    try:
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
    except FileNotFoundError:
        print('THE FILE DOES NOT EXIST. PLEASE CHECK THE INPUT')
        quit()
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
    data = {"name": name, "sex": sex, "age": age, "weight": weight, "height": height, "lifestyle": lifestyle,
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


def main_menu(dictionary, username, dbase, food_collection):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        dictionary[choice1][1](username, dbase, food_collection)
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        main_menu(main_menu1, username, dbase, food_collection)


def my_profile(username, dbase, food_collection):
    for key, value in username.items():
        print(f'{key} - {value}')
    while True:
        action = input('If you want to change your profile, print "yes" or print "back": ').strip().lower()
        if action == 'yes':
            print("Choose what you want to change:")
            take_action(change_parameters, profile_parameters, dbase, food_collection)
            break
        elif action == 'back':
            main_menu(main_menu1, username, dbase, food_collection)
            break
        else:
            print('Incorrect input. Try again!')


def my_diet(username, dbase, food_collection):
    print(f'Daily calories sum = {counting_daily_calories(username)}')
    drinks = random.sample(sort_food_info(food_collection)['drinks and coffee'], 2)
    fruits = random.sample(sort_food_info(food_collection)['fruit'], 2)
    alcohol = random.sample(sort_food_info(food_collection)['alcohol'], 1)
    cereals = random.sample(sort_food_info(food_collection)['cereals'], 2)
    pasta = random.sample(sort_food_info(food_collection)['pasta'], 2)
    meat = random.sample(sort_food_info(food_collection)['meat'], 1)
    fish_and_seafood = random.sample(sort_food_info(food_collection)['fish and seafood'], 1)
    vegetables = random.sample(sort_food_info(food_collection)['vegetables'], 3)
    print('BREAKFAST:')
    sum = 0
    sum = calories_check(sum, fruits, counting_daily_calories(username))
    sum = calories_check(sum, cereals, counting_daily_calories(username))
    sum = calories_check(sum, drinks, counting_daily_calories(username))
    print('LUNCH:')
    sum = calories_check(sum, meat, counting_daily_calories(username))
    sum = calories_check(sum, vegetables, counting_daily_calories(username))
    sum = calories_check(sum, drinks, counting_daily_calories(username))
    print('DINNER:')
    sum = calories_check(sum, fish_and_seafood, counting_daily_calories(username))
    sum = calories_check(sum, pasta, counting_daily_calories(username))
    sum = calories_check(sum, alcohol, counting_daily_calories(username))
    main_menu(main_menu1, username, dbase, food_collection)


def calories_check(summary, product_name, daily_norm):
    count = 0
    for i in product_name:
        for value in i.values():
            if (summary + value['calories']) <= daily_norm:
                summary += value['calories']
                print_menu(product_name[count])
            count += 1
    return summary


def print_menu(data):
    for key, value in data.items():
        print(f'{key}: ', end='')
        for k, v in value.items():
            print(f'{k} - {v}; ', end='')
        print()


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
    return int(daily_calories)


def get_url():
    resp = requests.get("https://www.diet-weight-lose.com/calories/")
    return resp


def write_html_file():
    soup = BeautifulSoup(get_url().text, 'lxml')
    with open("goods.html", 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))


def create_soup():
    with open("goods.html", 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "lxml")
    return soup


def products_name(soup):
    product = []
    products = []
    for line in soup:
        product.append(str(soup.find_all('div', {'class': 'divtabletd'})).split('</div>, <div class="divtabletd">'))
    for name in product[0]:
        if "</strong>" in name or "</div>" in name:
            pass
        else:
            products.append(' '.join(name.split()))
    products[17] = '1 cookie light'
    return products


def products_gramm(soup):
    gramm = []
    grammovka = []
    gramms = []
    for line in soup:
        gramm.append(str(soup.find_all('div', {'class': 'divtabletd1'})).split('</div>, <div class="divtabletd1">'))

    for quantity in gramm[0]:
        if "Quantity" in quantity or "</div>" in quantity:
            pass
        else:
            grammovka.append(' '.join(quantity.split()))

    for string in grammovka:
        if string[0:7] == "portion" and string[18:20] != 'oz':
            gramms.append(int(string[16:19]))
        if string[0:7] == "portion" and string[18:20] == 'oz':
            gramms.append(int(string[23:26]))
        if string[3:5] == 'oz':
            gramms.append(int(string[7:10]))
        if string[:8] == 'baguette':
            gramms.append(int(string[24:27]))
        if string == '50 gr':
            gramms.append(50)
        if string[:5] == 'spoon':
            gramms.append(int(string[13:15]))
        if string[:8] == "2 spoons":
            gramms.append(int(string[16:18]))
        if string[:4] == 'unit' and string[16:18] != 'oz':
            gramms.append(50)
        if string[:4] == 'unit' and string[16:18] == 'oz':
            gramms.append(int(string[20:23]))
        if string[:7] == "2 units":
            gramms.append(int(string[23:26]))
        if string[-2:] == "cl":
            gramms.append(string)
    return gramms


def products_calories(soup):
    calori = []
    calories = []
    for line in soup:
        calori.append(str(soup.find_all('div', {'class': 'divtabletd2'})).split('</div>, <div class="divtabletd2">'))

    for quantity in calori[0]:
        if "Calories" in quantity or "</div>" in quantity:
            pass
        else:
            calories.append(int(' '.join(quantity.split())))
    return calories


def collect_food_info(name, gramm, calories):
    food_info = []
    gramm_and_calories_info = []
    gram_and_calories = list(zip(gramm, calories))
    for i in gram_and_calories:
        info = dict(gramms=i[0], calories=i[1])
        gramm_and_calories_info.append(info)
    food = list(zip(name, gramm_and_calories_info))
    for i in food:
        info = dict([(i[0], i[1])])
        food_info.append(info)
    return food_info


def sort_food_info(data):
    fast_food = data[0:6]
    drinks_and_coffee = data[6:14]
    bread_biscuits_and_sweets = data[14:21]
    fruit = data[21:31]
    alcohol = data[31:40]
    cereals = data[40:43]
    pasta = data[43:47]
    dried_fruits = data[47:52]
    meat = data[52:63]
    oils_and_fat = data[63:68]
    eggs = data[68:71]
    lacteals = data[71:78]
    cheese = data[78:88]
    fish_seafood = data[88:104]
    vegetables = data[104:]
    sorted_food = {'fast food': fast_food, 'drinks and coffee': drinks_and_coffee,
                   'bread biscuits and sweets': bread_biscuits_and_sweets, 'fruit': fruit,
                   'alcohol': alcohol, 'cereals': cereals, 'pasta': pasta, 'dried fruits': dried_fruits,
                   'meat': meat, 'oils and fat': oils_and_fat, 'eggs': eggs, 'lacteals': lacteals,
                   'cheese': cheese, 'fish and seafood': fish_seafood, 'vegetables': vegetables}
    return sorted_food


def my_training_plan(username, dbase, food_collection):
    try:
        filename = username['goal'] + ' ' + username['sex'] + '.json'
        try:
            for item in os.scandir('trainings'):
                if basename(item) == filename:
                    with open(item) as file:
                        plan = json.load(file)
            trains(username, dbase, plan)
            print('HAVE A NICE TRAINING!')
            main_menu(main_menu1, username, dbase, food_collection)
            return plan
        except FileNotFoundError:
            print('THE FILE DOES NOT EXIST. PLEASE CHECK THE INPUT')
            exit_programme(username, dbase, food_collection)
    except UnboundLocalError:
        print('THE FILE DOES NOT EXIST. PLEASE CHECK THE INPUT')
        exit_programme(username, dbase, food_collection)


def trains(username, dbase, personal_plan):
    for key, value in personal_plan.items():
        print(f'{key}:')
        for i in value:
            for key1, value1 in i.items():
                print(f'{key1} - {value1}')


def exit_programme(username, dbase, food_collection):
    quit()


def take_action(definition, dictionary, dbase, food_collection):
    for value in dictionary.values():
        print(value[0])
    choice1 = input("Choose an option: ")
    if choice1 in dictionary.keys():
        definition(dictionary[choice1][1], user, dbase, food_collection)
    else:
        print("WRONG INPUT. PLEASE CHOOSE ANOTHER OPTION.")
        take_action(change_parameters, profile_parameters, dbase, food_collection)


def change_parameters(key, username, dbase, food_collection):
    if type(username[key]) == int:
        while True:
            parameter = input(f'Please, choose another {key}: ')
            if parameter.isdigit():
                username[key] = int(parameter)
                dbase[username['name']] = username
                change_file(dbase, username)
                my_profile(username, dbase, food_collection)
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
                    change_file(dbase, username)
                    break
            my_profile(username, dbase, food_collection)
        elif key == 'lifestyle':
            while True:
                lifestyle = input("Enter your type of lifestyle (active/not active): ")
                if lifestyle != 'active' and lifestyle != 'not active':
                    print("Wrong input! Choose between two variants.")
                else:
                    username[key] = lifestyle
                    dbase[username['name']] = username
                    change_file(dbase, username)
                    break
            my_profile(username, dbase, food_collection)
        elif key == 'goal':
            while True:
                goal = input("Choose your new goal (lose weight/gain weight/keep in shape): ")
                if goal != 'lose weight' and goal != 'gain weight' and goal != 'keep in shape':
                    print("Wrong input! Choose between three variants.")
                else:
                    username[key] = goal
                    dbase[username['name']] = username
                    change_file(dbase, username)
                    break
            my_profile(username, dbase, food_collection)


def change_file(dbase, username):
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

profile_parameters = {'1': ("1)Sex", 'sex'),
                      '2': ("2)Age", 'age'),
                      '3': ("3)Weight", 'weight'),
                      '4': ("4)Height", 'height'),
                      '5': ("5)Lifestyle", 'lifestyle'),
                      '6': ("6)Goal", 'goal')
                      }
data_base = take_data_from_database()
write_html_file()
collection = collect_food_info(products_name(create_soup()), products_gramm(create_soup()),
                               products_calories(create_soup()))
print("Welcome to the Healthy lifestyle application!")
user = username_identification(data_base)
main_menu(main_menu1, user, data_base, collection)
