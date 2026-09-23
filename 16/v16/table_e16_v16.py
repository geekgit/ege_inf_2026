elements = 6000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[0] = 1 # F(0) = 1
table[1] = 1 # F(1) = 1
table[2] = 1 # F(2) = 1
for i in range (3,elements):
    if i % 2 == 0:
        sum = 0
        for j in range(1,i):
            sum += table[j]
        table[i] = sum
    else:
        table[i] = table[i - 1] - table[i - 2]

result = table[39]
print("Результат: ", result)

