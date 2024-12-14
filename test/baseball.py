# A는 3자리 숫자로 된 정답을 하나 정합니다.
# B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 합니다.
# B가 말한 숫자가 정답에 포함되어 있다면 1Ball입니다.
# B가 말한 숫자가 정답에 포함되어 있고, 자리도 동일하다면 1Strike입니다.

# 서로 다른 숫자로 이루어진 세자리수
# Strike와 Ball의 결과를 보고 가능한 숫자를 계산하는 프로그램을 작성해주세요.

#====================

# A가 정답으로 생각할 수 있는 모든 수를 넣어보기
# B가 도전한 내용에 맞는지 확인하기

n = int(input()) #4
hint = [list(map(int,input().split()))for _ in range(4)]
answer = 0

for a in range(1,10): #100의 자리 수
    for b in range(10): #10의 자리 수
        for c in range(10): #1의 자리 수

            if(a==b or b==c or c==a):
                continue

            cnt = 0

            for arr in hint:
                number = arr[0]
                ball = arr[1]
                strike = arr[2]
                
                hint_arr = [number//100,number%100//10,number%10]
                answer_arr = [a,b,c]

                ball_cnt = 0
                strike_cnt = 0
                #a,b,c 라는 숫자를 number 하고 비교해서 자리수를 나눠서, strike ball 을 측정                

                if(a == hint_arr[0]):
                    strike_cnt += 1
                if(b == hint_arr[1]):
                    strike_cnt += 1
                if(c == hint_arr[2]):
                    strike_cnt += 1

                for i in range(len(hint_arr)):
                    for j in range(len(answer_arr)):
                        if i != j and answer_arr[i] == hint_arr[j]:
                            ball_cnt += 1
                
                if ball == ball_cnt and strike == strike_cnt :
                    cnt += 1
            
            if cnt == n:
                answer += 1


print(answer)