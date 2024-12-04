
def checkPrime (num) :
    for i in range(2,num) :
        if num % i == 0:
            if i >= 1000000 :
                return "YES"
            return "NO"
        elif num == i :
            return "YES"

count = int(input())
answer = []
for i in range(count) :
    answer.append(checkPrime(int(input())))

print(*answer)

