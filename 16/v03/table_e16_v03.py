elements = 3000 # максимальное количество положительных элементов в массиве
min = -100 # минимальный отрицательный элемент
table = [] # таблица значений, будет списком
for i in range (min, elements):
    table.insert(i,int(0)) # заполняем список нулями

for i in range (min, 10):
    table[i] = i

for i in range (10, elements):
    table[i] = pow(i,3) + table[i-15] # F(n) = n^3+F(n-15)

result = table[1000] - table[940] # числитель, F(1000) - F(940)

print("Результат: ", result)

