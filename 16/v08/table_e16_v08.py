elements = 6000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[1] = 1 # F(1) = 1
for i in range (2,elements):
    table[i] = i + table[i - 1]


result = table[2025] - table[1000]
print("Результат: ", result)

