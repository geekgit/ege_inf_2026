elements = 6000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[1] = 3 # F(1) = 3
for i in range (2,elements):
    table[i] = 3 * i + 2 * table[i - 1]


result = table[2024] - 4 * table[2022]
print("Результат: ", result)

