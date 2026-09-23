elements = 50 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[0] = 0 # F(0) = 0
table[1] = 1 # F(1) = 1

for i in range (2,elements):
    table[i] = table[i - 1] + table [i -2]

start = 1
end = 10
result = "Последовательность чисел Фибоначчи с " + str(start) + " элемента по " + str(end) + ": "

for i in range (start,end+1):
    x = table[i]
    result = result + str(x)
    if i<end:
        result = result + ", "
print(result)

