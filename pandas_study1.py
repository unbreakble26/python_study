#사전 연습
import random
data = [random.randrange(1,100) for x in range (0,10)]
print(data)
#generator
print(type( random.randrange(1,100)  for x in range (0, 10) ) )

a = data[0:5]
b = data[5:10]
print(a)
print(b)

#pondas는 DataFrame같은 구조를 파이선에서 손쉽게 사용할수 있게 만들어줌.
#엑셀구조와 같다.
data = { '박대성':{ 'sex':'M', 'money':5000}
     , '백상훈':{'sex':'M', 'money':2000000} }
print(data)
print(type(data))
# 이런 구조를 따로 루프등을 할 필요없이 바로바로 계산 가능하다.

#pondas 시작
from pandas import Series, DataFrame
kb = Series([37500, 23333, 55555, 22222, 44444])
print(kb)
print(type(kb))

print('------------------------')
kb2 = Series([37500, 23333, 55555, 22222, 44444], index=['02-05', '02-06', '02-07', '02-08', '02-09' ])
print(kb2)
print('------------------------')
kb2.sort_index(ascending=0)
print(kb2)
print('------------------------')
kb2['02-05'] += 10000
print(kb2)
print('-------최대값 / 중간값 / 평균값등 쉽게 구할 수 있음. -----------------')
print( kb2.mean() )
print( kb2.max() )
