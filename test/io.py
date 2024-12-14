#input() == scanner

# Default input => 스트링타입, 문자열 타입으로 받아오도록 만들어짐 scanner.nextLine()

#case 1 : 단순 정수일때
print("숫자 입력")
number = int(input())
print("입력하신 수는 : ",number)

#case 2 : 수열
print("수열 입력")
first,second,third = map(int,input().split())

numArr = [first,second,third]
for i in numArr :
    print("입력한 수열은 : ",i)


#case 3 : 단순 문자열일때
print("문자 입력")
string = input()
print("입력한 문자열은 : ",string)

#case 4 : 문자열
print("문자열 입력")
first, second, third = map(str, input().split())
strArr = [first,second,third]
for i in strArr:
    print("입력한 문자열 : ",i)

#배열2

print("문자열 입력")
strArr = map(str, input().split(","))
print(*strArr)

