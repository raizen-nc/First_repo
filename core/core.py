# name = 'Jhon'
# age = 25
# height = 1.77
# is_student = True # False
# has_high_degree = None
from pydoc_data.topics import topics

from pyexpat.errors import messages

# print(name)
# print(age)
# print(height)
# print(is_student)
# print(has_high_degree)


# name = "Alice"
# age = 33

# message = f'My name is {name}. I am {30/2} years old'
# print(message)

# без f строки. f строка дозволяє звертатися до наших змінних. бо без зних код не спрацює
# ми можемо також підставити одразу всю інформацію в прінт
# message = 'My name is {name}. I am {30/2} years old'
# print(message)

# Метод з використанням .format утакому випадку {} ужки можуть бути порожніми
# name = "Alice"
# age = 33
# message = 'Test 2. My name is {}. I am {} years old'.format(name, age)
# print(message)

# Третій спосіб форматування з допомогою %s стрінг це строка та  %d діджит відповідає за цифри замість .format ми використовуємо %
# Важливо у випадку з %s ми можемо використовувати і з цифрами, а %d тільки з цифрами а з текстом буде помилка.
# name = "Alice"
# age = 33
# message = 'Test 3. My name is %s. I am %d years old' %(name, age)
# print(message)

# Четвертий випадок використання форматування розділяння через +
# name = "Alice"
# age = 33
# message = 'Test 4. My name is' + name + '. I am '+ str(age) + ' years old'
# print(message)

# Обрахунок площі
# width = 10
# height = 5
# area  = width * height
# Обрахунок периметру
# perimeter = 2 * (width + height)
# print("Area", area)
# print("Perimeter", perimeter)

# Перевірка типу змінних/даних використовуючи type
# age = 25
# weight = 25.5
# room = "25"
# print(type(age),type(weight),type(room))

# Зміна типу даних
age = str(25) #буде без змін оскільки тепер це строка це тепер як текст
weight = int(25.5) # прибере зі значення 25.5 плаваючу частку після коми
room = float(25) # Перетворить з цілого числа на число з плаваючою кнопкою
print(age, weight, room)
