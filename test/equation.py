# 문자 A, B, C, D, E, F가 주어집니다.
# 다음 연립방정식에서 x와 y값을 계산하는 프로그램을 작성해주세요.
# Ax + By = C
# Dx + Ey = F
# -범위 X와Y는 -100000이상 100000이하입니다.

# def getY(arr):
#     return ((arr[3]*arr[1])-(arr[0]*arr[4]))/((arr[3]*arr[2])-(arr[0]*arr[5]))
# def getX(arr, y):
#     return (arr[2]-(arr[1]*y)) / arr[0]


# arr = list(map(int,input().split()))

# y = getY(arr)
# x = getX(arr,y)
# print(x,y)


def getY(a, b, c, d, e, f):
    return ((d*c)-(a*f))/((d*b)-(a*e))
def getX(a, b, c, y):
    return (c-(b*y)) / a

a, b, c, d, e, f = map(int,input().split())

y = int(getY(a, b, c, d, e, f))
x = int(getX(a, b, c, y))
print(x,y)