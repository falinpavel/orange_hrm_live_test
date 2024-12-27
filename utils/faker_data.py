from faker import Faker

fake = Faker("en_US")


def fake_fio():
    first_name = fake.first_name()
    middle_name = fake.first_name()
    second_name = fake.last_name()
    return first_name, middle_name, second_name

