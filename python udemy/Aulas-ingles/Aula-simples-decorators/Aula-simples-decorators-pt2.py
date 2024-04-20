import functools

user = {"username": 'jose', "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            print(f'No admin access. for {user["username"]}')
    return secure_function


@make_secure
def get_admin_password():
    return '123'


print(get_admin_password.__name__)

