from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

start = 1
end = 10
result = "Последовательность чисел Фибоначчи с " + str(start) + " элемента по " + str(end) + ": "

for i in range (start,end+1):
    x = F(i)
    result = result + str(x)
    if i<end:
        result = result + ", "
print(result)

