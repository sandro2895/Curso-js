import functools

user = {"username": 'jose', "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            print(f'No admin access. for {user["username"]}')
    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return '123'
    elif panel == 'billing':
        return 'super secure password'


print(get_password('billing'))

