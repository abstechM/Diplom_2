from faker import Faker

fake = Faker()



def create_random_email():
    email = fake.free_email()
    return email


def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_username():
    username = fake.name()
    return username