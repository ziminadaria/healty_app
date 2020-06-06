import os
from tkinter import *
from os.path import basename
import json
from bs4 import BeautifulSoup
import requests
import random


def take_data_from_database(file):
    database = {}
    try:
        with open(file, 'r') as file:
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
                database[name] = personal_data
    except FileNotFoundError:
        print('THE FILE DOES NOT EXIST. PLEASE CHECK THE INPUT')
        quit()
    return database


root = Tk()
root.geometry('500x500')
root.title('Healthy Lifestyle Application')


try:
    data = take_data_from_database('data base.txt')
except FileNotFoundError:
    data = {}
    print('There are no registered users or file is missed')

frame_start = Frame(root)

frame_start.pack()
text_start = Label(master=frame_start, text='Choose an action:')
Button_reg = Button(master=frame_start, text='Sign up', width='10', command=lambda: registration())
Button_log = Button(master=frame_start, text='Log in', width='10', command=lambda: login())
Button_quit = Button(master=frame_start, text='Quit', width='10', command=lambda: quit())
text_start.pack()
Button_reg.pack()
Button_log.pack()
Button_quit.pack()

frame_login = Frame(root)
text_login = Label(master=frame_login, text='Enter the system')
text_enter_login = Label(master=frame_login, text='Enter your username:')
enter_login = Entry(master=frame_login)
Button_enter = Button(master=frame_login, text='Enter', command=lambda: log_pass(data))
text_login.pack()
text_enter_login.pack()
enter_login.pack()
Button_enter.pack()

frame_reg = Frame(root)
text = Label(master=frame_reg, text='Please, fill in the registration form:')
text_log = Label(master=frame_reg, text='Enter your username:')
reg_login = Entry(master=frame_reg)
text_sex = Label(master=frame_reg, text='Enter your sex (male/female):')
reg_sex = Entry(master=frame_reg)
text_age = Label(master=frame_reg, text='Enter your age:')
reg_age = Entry(master=frame_reg)
text_weight = Label(master=frame_reg, text='Enter your weight:')
reg_weight = Entry(master=frame_reg)
text_height = Label(master=frame_reg, text='Enter your height:')
reg_height = Entry(master=frame_reg)
text_lifestyle = Label(master=frame_reg, text='Enter your lifestyle (active/not active):')
reg_lifestyle = Entry(master=frame_reg)
text_goal = Label(master=frame_reg, text='Enter your goal (lose weight/gain weight/keep in shape):')
reg_goal = Entry(master=frame_reg)
Button_reg = Button(master=frame_reg, text='Sign up', command=lambda: save(data, 'data base.txt'))
text.pack()
text_log.pack()
reg_login.pack()
text_sex.pack()
reg_sex.pack()
text_age.pack()
reg_age.pack()
text_weight.pack()
reg_weight.pack()
text_height.pack()
reg_height.pack()
text_lifestyle.pack()
reg_lifestyle.pack()
text_goal.pack()
reg_goal.pack()
Button_reg.pack()


def registration():
    frame_start.forget()
    frame_reg.pack()
    frame_login.forget()
    frame_menu.forget()


frame_menu = Frame(root)
title_menu = Label(master=frame_menu, text='Main menu:')
profile = Button(master=frame_menu, text='See my profile', width='15')
diet = Button(master=frame_menu, text='See my diet', width='15', command=lambda: diet(menu(data), data, collection))
trainings = Button(master=frame_menu, text='See my training plan', width='15', command=lambda: training_plan(menu(data),
                                                                                                             data))
ex = Button(master=frame_menu, text='Exit', width='15', command=lambda: quit())
title_menu.pack()
profile.pack()
diet.pack()
trainings.pack()
ex.pack()


frame_diet = Frame(root)


def menu(database):
    user_base = database[enter_login.get()]
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_trainings.forget()
    frame_menu.pack()
    return user_base


def login():
    frame_start.forget()
    frame_reg.forget()
    frame_login.pack()
    frame_menu.forget()


def diet(username, database, food):
    frame_menu.forget()
    frame_diet.pack()
    my_diet(username, database, food)


def save(database, file):
    while True:
        name = reg_login.get()
        if name in database.keys():
            message = Label(master=frame_reg, text='There is already a user with the same user name. Try again!')
            message.pack()
            registration()
        else:
            break
    while True:
        sex = reg_sex.get()
        if sex != 'male' and sex != 'female':
            message = Label(master=frame_reg, text='Not integer input in "sex" window. Try again!')
            message.pack()
            registration()
        else:
            break
    while True:
        age = reg_age.get()
        try:
            age = int(age)
            break
        except ValueError:
            message = Label(master=frame_reg, text='Not integer input in "sex" window. Try again!')
            message.pack()
            registration()
    while True:
        weight = reg_weight.get()
        try:
            weight = int(weight)
            break
        except ValueError:
            message = Label(master=frame_reg, text='Not integer input in "weight" window. Try again!')
            message.pack()
            registration()
    while True:
        height = reg_height.get()
        try:
            height = int(height)
            break
        except ValueError:
            message = Label(master=frame_reg, text='Not integer input in "height" window. Try again!')
            message.pack()
            registration()
    while True:
        lifestyle = reg_lifestyle.get()
        if lifestyle != 'active' and lifestyle != 'not active':
            message = Label(master=frame_reg, text='Not integer input in "lifestyle" window. Try again!')
            message.pack()
            registration()
        else:
            break
    while True:
        goal = reg_goal.get()
        if goal != 'lose weight' and goal != 'gain weight' and goal != 'keep in shape':
            message = Label(master=frame_reg, text='Not integer input in "goal" window. Try again!')
            message.pack()
            registration()
        else:
            break
    data_user = {"name": name, "sex": sex, "age": age, "weight": weight, "height": height, "lifestyle": lifestyle,
                 "goal": goal}
    database[name] = data_user
    add_to_data_base(data_user, file)
    login()
    return data_user


def add_to_data_base(database, file):
    with open(file, 'a') as file:
        file.write("\n")
        for key in database:
            file.write(str(database[key]) + ",")


def log_pass(database):
    name = enter_login.get()
    if name in database:
        print('You have logged in.')
        menu(database)
    else:
        # message = Label(text='Wrong username. Restart the application and try again!')
        # message.pack()
        text_pass = Label(master=frame_login, text='Username does not exist in data base. Please, try again!')
        text_pass.pack()
        enter_login.get()


def training_plan(username, dbase):
    frame_menu.forget()
    frame_trainings.pack()
    my_training_plan(username, dbase)


def my_training_plan(username, dbase):
    try:
        filename = username['goal'] + ' ' + username['sex'] + '.json'
        try:
            for item in os.scandir('trainings'):
                if basename(item) == filename:
                    with open(item) as file:
                        plan = json.load(file)
            trains(dbase, plan)
            return plan
        except FileNotFoundError:
            error_message = Label(master=frame_trainings, text='THE FILE DOES NOT EXIST. PLEASE CHECK THE INPUT')
            error_message.pack()
            Button_exit = Button(master=frame_trainings, text='Exit', command=lambda: quit())
            Button_exit.pack()
    except UnboundLocalError:
        error_message = Label(master=frame_trainings, text='THE FILE DOES NOT EXIST. PLEASE CHECK THE INPUT')
        error_message.pack()
        Button_exit = Button(master=frame_trainings, text='Exit', command=lambda: quit())
        Button_exit.pack()


def trains(dbase, personal_plan):
    for key, value in personal_plan.items():
        day_of_week = Label(master=frame_trainings, text=f'{key}:', fg='#f20c0c', font='Calluna')
        day_of_week.pack()
        for i in value:
            for key1, value1 in i.items():
                exercises = Label(master=frame_trainings, text=f'{key1} - {value1}', bg='azure')
                exercises.pack()
    message = Label(master=frame_trainings, text='HAVE A NICE TRAINING!', fg='#f20c0c')
    message.pack()
    back_to_menu = Button(master=frame_trainings, text='Back to main menu', command=lambda: menu(dbase))
    back_to_menu.pack()


def my_diet(username, dbase, food_collection):
    calories = Label(master=frame_diet, text=f'Daily calories sum = {counting_daily_calories(username)}')
    calories.pack()
    drinks = random.sample(sort_food_info(food_collection)['drinks and coffee'], 2)
    fruits = random.sample(sort_food_info(food_collection)['fruit'], 2)
    alcohol = random.sample(sort_food_info(food_collection)['alcohol'], 1)
    cereals = random.sample(sort_food_info(food_collection)['cereals'], 2)
    pasta = random.sample(sort_food_info(food_collection)['pasta'], 2)
    meat = random.sample(sort_food_info(food_collection)['meat'], 1)
    fish_and_seafood = random.sample(sort_food_info(food_collection)['fish and seafood'], 1)
    vegetables = random.sample(sort_food_info(food_collection)['vegetables'], 3)
    breakfast = Label(master=frame_diet, text='BREAKFAST:')
    breakfast.pack()
    sum = 0
    sum = calories_check(sum, fruits, counting_daily_calories(username))
    sum = calories_check(sum, cereals, counting_daily_calories(username))
    sum = calories_check(sum, drinks, counting_daily_calories(username))
    lunch = Label(master=frame_diet, text='LUNCH:')
    lunch.pack()
    sum = calories_check(sum, meat, counting_daily_calories(username))
    sum = calories_check(sum, vegetables, counting_daily_calories(username))
    sum = calories_check(sum, drinks, counting_daily_calories(username))
    dinner = Label(master=frame_diet, text='DINNER:')
    dinner.pack()
    sum = calories_check(sum, fish_and_seafood, counting_daily_calories(username))
    sum = calories_check(sum, pasta, counting_daily_calories(username))
    sum = calories_check(sum, alcohol, counting_daily_calories(username))


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
        product = Label(master=frame_diet, text=f'{key}')
        product.pack()
        for k, v in value.items():
            features = Label(master=frame_diet, text=f'{k} - {v}; ')
            features.pack()


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


write_html_file()
collection = collect_food_info(products_name(create_soup()), products_gramm(create_soup()),
                               products_calories(create_soup()))
frame_trainings = Frame(root)
title_trainings = Label(master=frame_trainings, text='My training plan:')
title_trainings.pack()
root.mainloop()
