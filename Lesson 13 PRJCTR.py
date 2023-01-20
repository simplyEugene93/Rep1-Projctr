
""" 1. Write a decorator that ensures a function is only called by users with a specific role.
    Each function should have an user_type with a string type in kwargs"""
    @is_admin
    def show_customer_receipt(user_type: str):
        return
        # some very dangerous operation

    show_customer_receipt(user_type='user')
    ValueError: Permission denied

    show_customer_receipt(user_type='admin')
    function pass as it should be
