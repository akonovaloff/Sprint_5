import random
import string

# Генератор логинов
def generate_login(domain="ya.ru"):
    """Случайный логин в формате имя_фамилия_номер_когорты_любые_4_цифры@домен"""
    return f"andreikonovalov17_{"".join(random.choices(string.ascii_letters + string.digits, k=4))}{random.randint(1000, 9999)}@{domain}"

# Генератор паролей
def generate_password(length=8):
    """Случайный пароль длиной length"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"  # строка допустимых символов
    return "".join(random.choices(characters, k=length))