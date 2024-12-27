from faker import Faker

fake = Faker("en_US")


def fake_fio():
    first_name = fake.first_name()
    middle_name = fake.first_name()
    second_name = fake.last_name()
    return first_name, middle_name, second_name


def fake_nickname():
    nickname = f"{fake.first_name()}{fake.last_name()}TEST"
    return nickname


def fake_admin():
    username_1 = f"{fake.first_name()}_admin"
    username_2 = f"{fake.last_name()}_admin"
    employee_name = f"{fake.administrative_unit()}TEST"
    return username_1, username_2, employee_name
