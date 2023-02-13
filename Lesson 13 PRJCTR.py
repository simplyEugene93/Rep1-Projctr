# 1. Write a decorator that ensures a function is only called by users with a specific role.
# Each function should have an user_type with a string type in kwargs

def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs["user_type"] != "admin":
            raise Exception("Permission denied")
        else:
            func(*args, **kwargs)
    return wrapper
@is_admin
def receive_check(user_type: str):
    order_a = 25
    order_b = 75
    check = order_a + order_b
    print(check)

receive_check(user_type='admin')
receive_check(user_type='user')

# 2. Write a decorator that wraps a function in a try-except block
# and print an error if error has happened

def find_errors(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError:
            print(f"Found 1 error during execution of your function: There is no such 'key' as foo")
    return wrapper
@find_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'key': 'bar'})
(some_function_with_risky_operation({'foo': 'bar'}))


