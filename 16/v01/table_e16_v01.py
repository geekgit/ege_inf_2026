elements = 3000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[1] = 2 # F(1) = 2
for i in range (2,elements):
    table[i] = 3 * table[i - 1] - i # F(n) = 3 * F(n-1) - i

numerator = table[2025] - table[2023] - 1 # числитель, F(2025) - F(2023) - 1
denom = pow(3,2022) # знаменатель, 3^2022

result = numerator // denom
assert numerator % denom == 0
print("Результат: ", result)

