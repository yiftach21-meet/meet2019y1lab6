
result = []
for count in range (1,100):
    if count % 3 == 0:
        result.append("Fizz")
 
    if count % 5 == 0:
        result.append("Buzz")
    else:
        result.append(count)
print(result)
