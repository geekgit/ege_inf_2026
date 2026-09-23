elements = 3000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[1] = 1 # F(1) = 1
for i in range (2,elements):
    table[i] = i * table[i - 1]

numerator = table[2025] // 25 + table[2024]  # числитель, F(2025)/25 + F(2024)
denom = table[2023] # знаменатель, F(2023)

result = numerator // denom
assert numerator % denom == 0
print("Результат: ", result)

