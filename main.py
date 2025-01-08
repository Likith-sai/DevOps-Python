import random

# Password generator function
def generate_password(passlen):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    if passlen <= 0:
        return ""
    if passlen > len(s):
        return "Password length exceeds character set size."
    return "".join(random.sample(s, passlen))