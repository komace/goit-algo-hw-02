import queue
import random
import time


# Створюємо чергу заявок
request_queue = queue.Queue()

# Функція для генерації нової заявки
def generate_request(request_id):
    request = {"id": request_id, "data": random.randint(1, 100)}
    request_queue.put(request)
    print(f"Створено заявку: {request}")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється заявка: {request}")    
        # Імітація обробки заявки
        time.sleep(2)
        print(f"Заявка {request['id']} оброблена")
    else:
        print("Черга пуста")    

# Головний цикл програми
def main():
    request_id = 0
    try:
        while True:
            # Генерація нової заявки
            generate_request(request_id)
            request_id += 1

            # Обробка заявки
            process_request()

            # Імітація часу між генерацією заявок
            time.sleep(1)
    except KeyboardInterrupt:
        print("Програма завершена")        

if __name__ == "__main__":
    main()


