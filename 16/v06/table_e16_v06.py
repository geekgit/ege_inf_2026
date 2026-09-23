elements = 6000 # максимальное количество элементов в массиве
table = [] # таблица значений, будет списком
for i in range (0, elements):
    table.insert(i,int(0)) # заполняем список нулями

table[1] = 1 # F(1) = 1
for i in range (2,elements):
    table[i] = i * table[i - 1]

numerator = table[3000] // 150 + table[2999]  # числитель, F(3000)/150 + F(2999)
denom = table[2998] # знаменатель, F(2998)

result = numerator // denom
assert numerator % denom == 0
print("Результат: ", result)

