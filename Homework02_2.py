from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру і видаляємо пробіли
    s = s.lower().replace(' ', '')

    # Створюємо двосторонню чергу і додаємо до неї всі символи рядка
    d = deque(s) 

    while len(d) > 1:
        # Порівнюємо символи з обох кінців черги
        if d.popleft() != d.pop():
            return False
    return True

# Приклади використання функції
print(is_palindrome("О гомін німого "))
print(is_palindrome("Уже лисі ліси Лежу"))   
print(is_palindrome("8855588")) 

