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
root.config(bg='DarkOliveGreen2')
root.geometry('820x500')
root.title('Healthy Lifestyle Application')

try:
    data = take_data_from_database('data base.txt')
except FileNotFoundError:
    data = {}
    print('There are no registered users or file is missed')

frame_start = Frame(root, padx=50, pady=50)
frame_start.pack(padx=100, pady=100)
frame_start.config(bg='DarkOliveGreen2')
hello_text = Label(master=frame_start, text='Welcome to Healthy Lifestyle Application!'
                                            '\nIt will help you to develop your own diet and training plan.')
text_start = Label(master=frame_start, text='Choose an action:')
Button_reg = Button(master=frame_start, text='Sign up', width='17', height='2', command=lambda: registration())
Button_log = Button(master=frame_start, text='Log in', width='17', height='2', command=lambda: login())
Button_quit = Button(master=frame_start, text='Quit', width='17', height='2', command=lambda: quit())
hello_text.configure(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 13, 'bold'))
text_start.configure(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
hello_text.pack()
text_start.pack()
Button_reg.pack()
Button_log.pack()
Button_quit.pack()

frame_login = Frame(root, padx=50, pady=50)
frame_login.config(bg='DarkOliveGreen2')
text_login = Label(master=frame_login, text='Enter the system')
text_login.configure(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
text_enter_login = Label(master=frame_login, text='Enter your username:')
text_enter_login.configure(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
enter_login = Entry(master=frame_login)
enter_login.configure(width='20')
Button_enter = Button(master=frame_login, text='Enter', command=lambda: log_pass(data), width='13', height='1')
text_login.pack()
text_enter_login.pack()
enter_login.pack()
Button_enter.pack()

frame_reg = Frame(root, padx=50, pady=50)
frame_reg.config(bg='DarkOliveGreen2')
text = Label(master=frame_reg, text='Please, fill in the registration form:')
text.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
text_log = Label(master=frame_reg, text='Enter your username:')
text_log.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
reg_login = Entry(master=frame_reg)
text_sex = Label(master=frame_reg, text='Enter your sex (male/female):')
text_sex.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
reg_sex = Entry(master=frame_reg)
text_age = Label(master=frame_reg, text='Enter your age:')
text_age.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
reg_age = Entry(master=frame_reg)
text_weight = Label(master=frame_reg, text='Enter your weight:')
text_weight.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
reg_weight = Entry(master=frame_reg)
text_height = Label(master=frame_reg, text='Enter your height:')
text_height.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
reg_height = Entry(master=frame_reg)
text_lifestyle = Label(master=frame_reg, text='Enter your lifestyle (active/not active):')
text_lifestyle.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
reg_lifestyle = Entry(master=frame_reg)
text_goal = Label(master=frame_reg, text='Enter your goal (lose weight/gain weight/keep in shape):')
text_goal.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
reg_goal = Entry(master=frame_reg)
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
Button_reg = Button(master=frame_reg, text='Sign up', width='13', height='1',
                    command=lambda: check_reg('name', reg_login.get(), 'sex', reg_sex.get(), 'lifestyle',
                                              reg_lifestyle.get(), 'goal',
                                              reg_goal.get(), 'age', reg_age.get(), 'weight', reg_weight.get(),
                                              'height', reg_height.get(), data))
Button_reg.pack()


def check_reg(key_login, par_login, key_sex, par_sex, key_lifestyle, par_lifestyle, key_goal, par_goal, key_age,
              par_age, key_weight,
              par_weight, key_height, par_height, dbase):
    if par_login in dbase.keys():
        error_message = Label(master=frame_reg, text=f'Name {key_login} already exists! Please, choose another one.')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
    elif par_sex != 'male' and par_sex != 'female':
        error_message = Label(master=frame_reg, text=f'Wrong {key_sex} input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
    elif par_lifestyle != 'active' and par_lifestyle != 'not active':
        error_message = Label(master=frame_reg, text=f'Wrong {key_lifestyle} input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
    elif par_goal != 'lose weight' and par_goal != 'gain weight' and par_goal != 'keep in shape':
        error_message = Label(master=frame_reg, text=f'Wrong {key_goal} input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
    else:
        check_age_reg(key_age, par_age, key_weight, par_weight, key_height, par_height, dbase)


def check_age_reg(key_age, par_age, key_weight, par_weight, key_height, par_height, dbase):
    try:
        par_age = int(par_age)
        check_weight_reg(key_weight, par_weight, key_height, par_height, dbase)
    except ValueError:
        error_message = Label(master=frame_reg, text=f'Wrong {key_age} input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()


def check_weight_reg(key_weight, par_weight, key_height, par_height, dbase):
    try:
        par_weight = int(par_weight)
        check_height_reg(key_height, par_height, dbase)
    except ValueError:
        error_message = Label(master=frame_reg, text=f'Wrong {key_weight} input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()


def check_height_reg(key_height, par_height, dbase):
    try:
        par_height = int(par_height)
        save(dbase, 'data base.txt')
    except ValueError:
        error_message = Label(master=frame_reg, text=f'Wrong {key_height} input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()


frame_menu = Frame(root, padx=50, pady=50)
frame_menu.config(bg='DarkOliveGreen2')
title_menu = Label(master=frame_menu, text='Main menu:')
title_menu.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 12, 'bold'))
profile = Button(master=frame_menu, text='See my profile', width='17', height='2',
                 command=lambda: profile(menu(data), data))
diet = Button(master=frame_menu, text='See my diet', width='17', height='2',
              command=lambda: diet(menu(data), data, collection))
trainings = Button(master=frame_menu, text='See my training plan', width='17', height='2',
                   command=lambda: training_plan(menu(data), data))
ex = Button(master=frame_menu, text='Exit', width='17', height='2', command=lambda: quit())
title_menu.pack()
profile.pack()
diet.pack()
trainings.pack()
ex.pack()

frame_diet = Frame(root, padx=20, pady=20)
frame_diet.config(bg='DarkOliveGreen2')

frame_trainings = Frame(root, padx=20, pady=20)
frame_trainings.config(bg='DarkOliveGreen2')
title_trainings = Label(master=frame_trainings, text='My training plan:')
title_trainings.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
title_trainings.pack()

frame_action = Frame(root, padx=50, pady=50)
frame_action.config(bg='DarkOliveGreen2')
title_action = Label(master=frame_action, text='What do you want to change?')
title_action.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
title_action.pack()
parameter_sex = Button(master=frame_action, text='Sex', width='15',
                       command=lambda: change_parameters('sex', menu(data), data))
parameter_age = Button(master=frame_action, text='Age', width='15', height='1',
                       command=lambda: change_parameters('age', menu(data), data))
parameter_weight = Button(master=frame_action, text='Weight', width='15', height='1',
                          command=lambda: change_parameters('weight', menu(data), data))
parameter_height = Button(master=frame_action, text='Height', width='15', height='1',
                          command=lambda: change_parameters('height', menu(data), data))
parameter_lifestyle = Button(master=frame_action, text='Lifestyle', width='15', height='1',
                             command=lambda: change_parameters('lifestyle', menu(data), data))
parameter_goal = Button(master=frame_action, text='Goal', width='15', height='1',
                        command=lambda: change_parameters('goal', menu(data), data))
parameter_sex.pack()
parameter_age.pack()
parameter_weight.pack()
parameter_height.pack()
parameter_lifestyle.pack()
parameter_goal.pack()

frame_profile = Frame(root, padx=50, pady=50)
frame_profile.config(bg='DarkOliveGreen2')

frame_change_parameter = Frame(root, padx=50, pady=50)
frame_change_parameter.config(bg='DarkOliveGreen2')


def registration():
    frame_start.forget()
    frame_login.forget()
    frame_profile.forget()
    frame_action.forget()
    frame_trainings.forget()
    frame_menu.forget()
    frame_diet.forget()
    frame_reg.pack(padx=100, pady=100)
    frame_change_parameter.forget()


def menu(database):
    user_base = database[enter_login.get()]
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_profile.forget()
    frame_action.forget()
    frame_trainings.forget()
    frame_menu.pack(padx=100, pady=100)
    frame_diet.forget()
    frame_change_parameter.forget()
    return user_base


def login():
    frame_start.forget()
    frame_reg.forget()
    frame_profile.forget()
    frame_action.forget()
    frame_trainings.forget()
    frame_menu.forget()
    frame_diet.forget()
    frame_login.pack(padx=100, pady=100)
    frame_change_parameter.forget()


def diet(username, database, food):
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_profile.forget()
    frame_action.forget()
    frame_trainings.forget()
    frame_menu.forget()
    frame_diet.pack(padx=100, pady=100)
    frame_change_parameter.forget()
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
        text_pass = Label(master=frame_login, text='Username does not exist in data base. Please, try again!')
        text_pass.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        text_pass.pack()
        enter_login.get()


def training_plan(username, dbase):
    frame_menu.forget()
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_profile.forget()
    frame_action.forget()
    frame_diet.forget()
    frame_trainings.pack(padx=50, pady=50)
    frame_change_parameter.forget()
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
            error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
            error_message.pack()
            Button_exit = Button(master=frame_trainings, text='Exit', command=lambda: quit())
            Button_exit.pack()
    except UnboundLocalError:
        error_message = Label(master=frame_trainings, text='THE FILE DOES NOT EXIST. PLEASE CHECK THE INPUT')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
        Button_exit = Button(master=frame_trainings, text='Exit', command=lambda: quit())
        Button_exit.pack()


def trains(dbase, personal_plan):
    for key, value in personal_plan.items():
        day_of_week = Label(master=frame_trainings, text=f'{key}:')
        day_of_week.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
        day_of_week.pack()
        for i in value:
            for key1, value1 in i.items():
                exercises = Label(master=frame_trainings, text=f'{key1} - {value1}')
                exercises.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
                exercises.pack()
    message = Label(master=frame_trainings, text='HAVE A NICE TRAINING!')
    message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    message.pack()
    back_to_menu = Button(master=frame_trainings, text='Back to main menu',
                          command=lambda: forget_widgets(dbase, frame_trainings))
    back_to_menu.pack()


def my_diet(username, dbase, food_collection):
    calories = Label(master=frame_diet, text=f'Daily calories sum = {counting_daily_calories(username)}')
    calories.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    calories.pack()
    drinks = random.sample(sort_food_info(food_collection)['drinks and coffee'], 1)
    fruits = random.sample(sort_food_info(food_collection)['fruit'], 2)
    alcohol = random.sample(sort_food_info(food_collection)['alcohol'], 1)
    cereals = random.sample(sort_food_info(food_collection)['cereals'], 1)
    pasta = random.sample(sort_food_info(food_collection)['pasta'], 1)
    meat = random.sample(sort_food_info(food_collection)['meat'], 1)
    fish_and_seafood = random.sample(sort_food_info(food_collection)['fish and seafood'], 2)
    vegetables = random.sample(sort_food_info(food_collection)['vegetables'], 3)
    breakfast = Label(master=frame_diet, text='BREAKFAST:')
    breakfast.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    breakfast.pack()
    sum = 0
    sum = calories_check(sum, fruits, counting_daily_calories(username))
    sum = calories_check(sum, cereals, counting_daily_calories(username))
    sum = calories_check(sum, drinks, counting_daily_calories(username))
    lunch = Label(master=frame_diet, text='LUNCH:')
    lunch.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    lunch.pack()
    sum = calories_check(sum, meat, counting_daily_calories(username))
    sum = calories_check(sum, vegetables, counting_daily_calories(username))
    sum = calories_check(sum, drinks, counting_daily_calories(username))
    dinner = Label(master=frame_diet, text='DINNER:')
    dinner.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    dinner.pack()
    sum = calories_check(sum, fish_and_seafood, counting_daily_calories(username))
    sum = calories_check(sum, pasta, counting_daily_calories(username))
    sum = calories_check(sum, alcohol, counting_daily_calories(username))
    back = Button(master=frame_diet, text='Back', command=lambda: forget_widgets(dbase, frame_diet))
    back.pack()


def forget_widgets(dbase, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    menu(dbase)


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
    count = 0
    for key, value in data.items():
        count += 1
        for k, v in value.items():
            if count == 1:
                features = Label(master=frame_diet, text=f'{key}: {k} - {v};')
                features.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
                features.pack()
                count = 0


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
        if "gr" in string:
            val = string.split()
            for elem in val:
                if elem == 'gr' or elem == 'gr)':
                    gramms.append(int(val[val.index(elem) - 1]))
        elif 'unit' in string:
            gramms.append(50)
        elif "cl" in string:
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


def profile(username, dbase):
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_action.forget()
    frame_trainings.forget()
    frame_menu.forget()
    frame_diet.forget()
    frame_profile.pack(padx=100, pady=100)
    frame_change_parameter.forget()
    my_profile(username, dbase)


def my_profile(username, dbase):
    title_profile = Label(master=frame_profile, text='My profile:')
    title_profile.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    title_profile.pack()
    for key, value in username.items():
        profile_attributes = Label(master=frame_profile, text=f'{key} - {value}', bg='azure')
        profile_attributes.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        profile_attributes.pack()
    profile_change = Label(master=frame_profile, text=f'Do you want to change your profile?')
    profile_change.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    profile_change.pack()
    yes_button = Button(master=frame_profile, text='Yes', command=lambda: take_action(username, dbase))
    yes_button.pack()
    no_button = Button(master=frame_profile, text='No', command=lambda: forget_widgets(dbase, frame_profile))
    no_button.pack()


def take_action(username, dbase):
    frame_menu.forget()
    frame_profile.forget()
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_profile.forget()
    frame_trainings.forget()
    frame_diet.forget()
    frame_action.pack(padx=100, pady=100)
    frame_change_parameter.forget()


def change_parameters(key, username, dbase):
    frame_menu.forget()
    frame_action.forget()
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_profile.forget()
    frame_action.forget()
    frame_trainings.forget()
    frame_diet.forget()
    frame_change_parameter.pack(padx=100, pady=100)
    parameters(key, username, dbase)


def parameters(key, username, dbase):
    text_messages = Label(master=frame_change_parameter, text=f'Please, choose another {key}:', font='Calluna')
    text_messages.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10, 'bold'))
    text_messages.pack()
    if key == 'sex':
        par = Entry(master=frame_change_parameter)
        par.pack()
        ok_button = Button(master=frame_change_parameter, text='ok', width='15',
                           command=lambda: change_sex_check(key, par.get(), username, dbase))
        ok_button.pack()
    elif key == 'age':
        par = Entry(master=frame_change_parameter)
        par.pack()
        ok_button = Button(master=frame_change_parameter, text='ok', width='15',
                           command=lambda: change_check(key, par.get(), username, dbase))
        ok_button.pack()
    elif key == 'weight':
        par = Entry(master=frame_change_parameter)
        par.pack()
        ok_button = Button(master=frame_change_parameter, text='ok', width='15',
                           command=lambda: change_check(key, par.get(), username, dbase))
        ok_button.pack()
    elif key == 'height':
        par = Entry(master=frame_change_parameter)
        par.pack()
        ok_button = Button(master=frame_change_parameter, text='ok', width='15',
                           command=lambda: change_check(key, par.get(), username, dbase))
        ok_button.pack()
    elif key == 'lifestyle':
        par = Entry(master=frame_change_parameter)
        par.pack()
        ok_button = Button(master=frame_change_parameter, text='ok', width='15',
                           command=lambda: change_lifestyle_check(key, par.get(), username, dbase))
        ok_button.pack()
    elif key == 'goal':
        par = Entry(master=frame_change_parameter)
        par.pack()
        ok_button = Button(master=frame_change_parameter, text='ok', width='15',
                           command=lambda: change_goal_check(key, par.get(), username, dbase))
        ok_button.pack()


def change_sex_check(key_sex, par, username, dbase):
    if par != 'male' and par != 'female':
        error_message = Label(master=frame_change_parameter, text=f'Wrong input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
    else:
        username[key_sex] = par
        dbase[username['name']] = username
        forget_widgets(dbase, frame_profile)
        forget_widgets(dbase, frame_change_parameter)
        change_file(dbase, username)


def change_lifestyle_check(key_lifestyle, par, username, dbase):
    if par != 'active' and par != 'not active':
        error_message = Label(master=frame_change_parameter, text=f'Wrong input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
    else:
        username[key_lifestyle] = par
        dbase[username['name']] = username
        forget_widgets(dbase, frame_profile)
        forget_widgets(dbase, frame_change_parameter)
        change_file(dbase, username)


def change_goal_check(key_goal, par, username, dbase):
    if par != 'lose weight' and par != 'gain weight' and par != 'keep in shape':
        error_message = Label(master=frame_change_parameter, text=f'Wrong input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()
    else:
        username[key_goal] = par
        dbase[username['name']] = username
        forget_widgets(dbase, frame_profile)
        forget_widgets(dbase, frame_change_parameter)
        change_file(dbase, username)


def change_check(key_par, par, username, dbase):
    try:
        par = int(par)
        username[key_par] = par
        dbase[username['name']] = username
        forget_widgets(dbase, frame_profile)
        forget_widgets(dbase, frame_change_parameter)
        change_file(dbase, username)
    except ValueError:
        error_message = Label(master=frame_change_parameter, text=f'Wrong input!')
        error_message.config(bg='DarkOliveGreen2', fg='gray11', font=('Verdana', 10))
        error_message.pack()


def change_file(dbase, username):
    count = len(dbase)
    with open('data base.txt', 'w') as f:
        for key in dbase:
            count -= 1
            for value in dbase[key].values():
                f.write(str(value) + ",")
            if count > 0:
                f.write('\n')
    frame_change_parameter.forget()
    profile(username, dbase)


root.mainloop()
