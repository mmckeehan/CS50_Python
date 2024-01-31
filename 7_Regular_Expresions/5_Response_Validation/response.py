from validator_collection import validators, checkers, errors

email = input("What's your email address? ")

try:
    if email.isalnum == False:
        email = None
    email = validators.email(email)
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")
else:
    print("Valid")
