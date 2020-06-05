from tkinter import *


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
Button_reg = Button(master=frame_start, text='Sign up', command=lambda: registration())
Button_log = Button(master=frame_start, text='Log in', command=lambda: login())
Button_quit = Button(master=frame_start, text='Quit', command=lambda: quit())
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
profile = Button(master=frame_menu, text='See my profile')
diet = Button(master=frame_menu, text='See my diet', command=lambda: print(menu(data)))
trainings = Button(master=frame_menu, text='See my training plan')
ex = Button(master=frame_menu, text='Exit', command=lambda: quit())
title_menu.pack()
profile.pack()
diet.pack()
trainings.pack()
ex.pack()


def menu(database):
    user_base = database[enter_login.get()]
    frame_start.forget()
    frame_reg.forget()
    frame_login.forget()
    frame_menu.pack()
    return user_base


def login():
    frame_start.forget()
    frame_reg.forget()
    frame_login.pack()
    frame_menu.forget()


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
    data = {"name": name, "sex": sex, "age": age, "weight": weight, "height": height, "lifestyle": lifestyle,
            "goal": goal}
    database[name] = data
    add_to_data_base(data, file)
    login()
    return data


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


root.mainloop()
