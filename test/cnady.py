# 친구 A, B, C에게 사탕을 나누어 주려고 합니다.
# 조건은 아래와 같습니다.
#     1. 남는 사탕이 없어야합니다.
#     2. A는 B보다 2개이상 많은 사탕을 가져야 합니다.
#     3. 셋중 사탕을 못받는 사람이 있으면 안됩니다.
#     4. C가 받는 사탕은 짝수여야 합니다.
# 분배 가능한 경우의 수를 출력하는 프로그램을 작성해주세요

candy = int(input())
answer = 0
for a in range(0,candy+1):
    for b in range(0,candy+1):
        for c in range(0,candy+1):
            if a+b+c == candy :
                if a >= b+2 :
                    if c % 2 == 0:
                        if a != 0 & b != 0 & c != 0:
                            answer+=1
print(answer)