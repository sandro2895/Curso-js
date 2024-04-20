user = {"username": 'jose', "access_level": "admin"}


def get_admin_password():
    return '123'


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func
        else:
            print('No admin access.')
    return secure_function()


get_admin_password = make_secure(get_admin_password())

print(get_admin_password)

