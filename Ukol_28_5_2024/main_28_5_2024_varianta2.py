
#task 1 řešení 2
#zajímalo by mě zda by toto řešení vyhovovalo. Zde je ten zámek složitější a vlákna spouštítm ve funkci po generování čásel.
#Je vhodné vlákna spouštět ve funkci?

import threading
import random

def generate_random_numbers(count, min_val, max_val):
    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    return numbers

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_sum(numbers):
    return sum(numbers)

#proměnné
random_numbers = []
sum_result = None
average_result = None

def fill_numbers():
    global random_numbers
    random_numbers = generate_random_numbers(10,1,100)
    print(f"Generovaná čísla: {random_numbers}")

    sum_thread.start()
    average_thread.start()

def sum_numbers():
    global sum_result
    with lock:
        sum_result = calculate_sum(random_numbers)
    print(f"Součet čísel je {sum_result}")

def average_numbers():
    global average_result
    with lock:
        average_result = calculate_average(random_numbers)
    print(f"Průměr čísel je: {average_result}")


#tvorba vláken
fill_thread = threading.Thread(target=fill_numbers)
sum_thread = threading.Thread(target=sum_numbers)
average_thread = threading.Thread(target=average_numbers)

# zámek vláken
lock = threading.Lock()

#spustění vláken
fill_thread.start()

#čekání na dokončení vláken
fill_thread.join()
sum_thread.join()
average_thread.join()

print(f"Výseledek je průměr čísel: {average_result} , Součet čísel: {sum_result}")