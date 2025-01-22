import time
start = time.time()
result = ""
for i in range(1, 10001):
    result += str(i)
    print("+= Time:", time.time() - start)

start = time.time()
result = "".join(str(i)for i in range(1, 10001))
print("Using Join Method:", time.time() - start)