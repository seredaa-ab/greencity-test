# utils.py

# Тестові дані для реєстрації (негативні паролі)
INVALID_PASSWORDS = [
    "123",          # дуже короткий
    "abcdef",       # тільки літери нижнього регістру
    "PASSWORD",     # тільки літери верхнього регістру
    "12345678"      # тільки цифри
]

# Тестові дані для позитивної реєстрації
VALID_USERS = [
    {
        "email": "example1@gmail.com",
        "name": "Test User 1",
        "password": "Aa123456!"
    },
    {
        "email": "example2@gmail.com",
        "name": "Test User 2",
        "password": "Bb987654$"
    }
]
