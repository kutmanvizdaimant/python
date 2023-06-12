import random

number = round(random.random(), 2) # значение от 0.0 до 1.0
print(number)
number = round(random.random() * 100, 2)  # значение от 0.0 до 100.0
print(number)

number = random.randint(20, 35)  # значение от 20 до 35
print(number)


number = random.randrange(250)  # значение от 0 до 10 не включая
print(number)
number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9
print(number)

number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8
print(number)

numbers = ["Kutman", "Ainazik", "Aidai", "Islam", "Roma", "Syimyk", "Chynara"]
random.shuffle(numbers)
# print(numbers)
random_number = random.choice(numbers)
print(random_number)