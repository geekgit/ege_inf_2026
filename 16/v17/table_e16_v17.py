elements = 6000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[0] = 1 # F(0) = 1
table[1] = 1 # F(1) = 1
for i in range (2,elements):
    if i % 2 == 0:
        table[i] = 3 * table[i - 1]
    else:
        table[i] = 5 * i + table[i - 1] + table[2]

result = table[23]
print("Результат: ", result)

