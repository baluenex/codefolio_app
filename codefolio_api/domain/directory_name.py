import re


def validate(dir_name):
    result = re.fullmatch(r"[0-9a-zA-Z\\-\\_]{3,255}", dir_name)
    if result:
        return True
    else:
        return False

if __name__ == '__main__':
    validate("af4wress")