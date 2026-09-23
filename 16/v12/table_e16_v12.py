elements = 6000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[1] = 1 # F(1) = 1
table[2] = 2 # F(2) = 2
for i in range (3,elements):
    table[i] = i * (i - 1) + table[i - 1] - table[i - 2]


result = table[2024] + table[2020] - table[2019]
print("Результат: ", result)

