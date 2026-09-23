elements = 6000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[0] = 0 # F(0) = 0
table[1] = 1 # F(1) = 1
table[2] = 2 # F(2) = 2
for i in range (3,elements):
    if i % 2 == 0:
        table[i] = 2 * (i - 1) + table[i - 1] + 2
    else:
        table[i] = 2 * (i + 1) + table[i - 2] - 5

result = table[32]
print("Результат: ", result)

