
def form(name, surname, birthday, city, e_mail, phone):
    print(
        f"Имя - {name}, Фамилия - {surname}, Год рождения - {birthday}, Город проживания - {city}, e-mail - {e_mail}, № телефона - {phone}")


form(name=(str(input("Введите ваше имя: "))),
     surname=(str(input("Введите вашу фамилию: "))),
     birthday=(int(input("Введите год рождения: "))),
     city=(str(input("Введите город проживания: "))),
     e_mail=(str(input("Введите вашу электронную почту: "))),
     phone=(int(input("Ввведите ваш номер телефона: "))))
