# validators.py

import re
from django import forms
from functools import wraps

def regex_validator(pattern, error_message):
    def decorator(func):
        @wraps(func)
        def wrapper(self):
            value = func(self)

            if not re.match(pattern, value):
                raise forms.ValidationError(error_message)

            return value
        return wrapper
    return decorator