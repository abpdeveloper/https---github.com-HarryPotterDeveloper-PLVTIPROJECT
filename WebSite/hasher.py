import hashlib


def make_pssword(password):
    return hashlib.sha256(str.encode(password)).hexgigest()


def check_password(password, hash):
    if make_pssword(password) == hash:
        return True

    return False