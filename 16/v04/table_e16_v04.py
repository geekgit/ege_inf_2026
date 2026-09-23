elements = 3000 # максимальное количество положительных элементов в массиве
min = -100 # минимальный отрицательный элемент
table = [] # таблица значений, будет списком
for i in range (min, elements):
    table.insert(i,int(0)) # заполняем список нулями

for i in range (min, 10):
    table[i] = i

for i in range (10,elements):
    table[i] = pow(i,3) + table[i-11] # F(n) = n^3+F(n-11)

result = table[900] - table[856] # числитель, F(900) - F(856)

print("Результат: ", result)

