def user_registration(user_id):
    with open ('users.env' , 'r') as file:
        user_list = file.readlines()
    if user_id in user_list:
        return 'Вы уже зарегистрированы! Если Вы хотите изменить Ваши данные, то воспользуйтесь кнопкой "Сменить данные ⚙️".'
    else:
        if user_list == []:
            with open('users.env', 'w') as file:
                file.write(user_id)
        else:
            with open('users.env', 'a') as file:
                file.writelines(f'\n{user_id}')
        return 'Вы были успешно зарегистрированы!'      