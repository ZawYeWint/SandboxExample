"""
Description: Simple Password Checker
Name : Patrick
"""


def is_valid_password(text):
    """Check whether a given text has the correct password format"""
    return 8 <= len(text) <= 20


def main():
    new_password = "helloworld"
    print(f"{new_password} is a valid password? {is_valid_password(new_password)}")


if __name__ == '__main__':
    main()
