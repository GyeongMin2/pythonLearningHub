# 내 풀이
# def checkPrime (num) :
#     for i in range(2,num) :
#         if num % i == 0:
#             if i >= 1000000 :
#                 return "YES"
#             return "NO"
#         elif num == i :
#             return "YES"

# count = int(input())
# answer = []
# for i in range(count) :
#     answer.append(checkPrime(int(input())))

# print(*answer)

# 강사님 풀이
TC = int(input())
for _ in range(TC):
    number = int(input())

    for i in range(2,1_000_001):
        if number%i == 0 : # 100만 이하의 약수가 존재함
            print("NO")
            break
        if i == 1_000_000: # 100만 이하의 약수가 존재하지 않음
            print("YES")
