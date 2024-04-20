import functools



def make_secure(acess_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user1["access_level"] or user2["access_level"] == acess_level:
                return func(*args, **kwargs), f'{acess_level}'
            else:
                print(f'No {acess_level}. for {["username"]}')
        return secure_function
    return decorator

@make_secure('admin')
def get_admin_password():
    return f'ADMIN'


@make_secure('user')
def get_dashboard_password():
    return f'GUEST '


user1 = {"username": 'jose', "access_level": "guest"}
user2 = {"username": 'anna', "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
