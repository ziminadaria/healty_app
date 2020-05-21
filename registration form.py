def start_of_app():
    print("Welcome to the Healthy lifestyle application!")
    existing_account = input("Do you have an account? (yes/no): ")
    if existing_account == 'yes':
        name = input("Please, enter your name: ")
        #main_menu
    elif existing_account == 'no':
        add_to_data_base(registration_form())

def take_data_from_database():
    data_base = {}
    with open("data base.txt",'r') as file:
        for line in file:
            name = line.split(',')[0]
            sex = line.split(',')[1]
            age = line.split(',')[2]
            weight = line.split(',')[3]
            height = line.split(',')[4]
            lifestyle= line.split(',')[5]
            personal_data = dict( name = name, sex = sex, age = age, weight = weight,height = height,lifestyle = lifestyle)
            data_base[name] = personal_data
    return data_base

def registration_form():
    print(" Please, fill in the registration form: ")
    name = input("Enter your name: ")
    sex = input("Enter your sex (male/female): ")
    age = int(input("Enter your full age: "))
    weight = int(input("Enter your weight: "))
    height = int(input("Enter your height: "))
    lifestyle = input("Enter your type of lifestyle (active/not active): ")
    data = {}
    data["name"] = name
    data["sex"] = sex
    data["age"] = age
    data["weight"] = weight
    data["height"] = height
    data["lifestyle"] = lifestyle
    return data

def add_to_data_base(data):
    with open("data base.txt",'a') as file:
        file.write("\n")
        for key in data:
               file.write(str(data[key])+",")


start_of_app()


