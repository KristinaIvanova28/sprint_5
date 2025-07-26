from faker import Faker

faker = Faker()

def generate_registration_data(): # генерируем кортеж(name, email, password) для рана теста успешной регистрации нового нового пользователя
    name = faker.name()
    email = faker.email()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password

def generate_registration_data_short_password(): # Генерируем кортеж с невалидным паролем
    name = faker.name()
    email = faker.email()
    password = faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password