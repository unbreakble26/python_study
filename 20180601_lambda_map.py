

#lambda 함수
def hap(x, y):
    return x + y
print(hap(10, 20))

#위와 같은 것이
print( (lambda x, y : x+y)(10, 20) )

#map() 함수 lambda 이용
# 기본 형태 : map(함수, 리스트)

print( list(map(lambda x: x**2, range(5)) ) )
