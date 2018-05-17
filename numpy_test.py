import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x)
print(type(x))

print(x+y)
print(x*y)
print(x/y)
print(x/2.0)
print(" ")
A = np.array([ [1, 2], [3, 4] ])
B = np.array( [ [3, 0],[0, 6] ] )
print(A)
print(A.shape)
print(A.dtype)

print(A+B)
print(A*B)

X = np.array([ [51, 55], [14, 19], [0, 4] ])
print(X)
print(X[0])
print(X[0][1])

#row단위로 반복문으로 출력
for row in X:
    print(row)
#1차원 배열로 평탄화
X = X.flatten()
print(type(X))
print(X)
#인덱스가 0,2,4 인 원소 얻기
print( X[np.array([0, 2, 4])] )

#특정 조건을 수행하는 원소만 얻기
print( X > 15 )
print( X[X > 15] )

#과제
# 연습문제
# Numpy의 난수를 발생시키는 random 모듈에서 N개의 난수를 발생시키는 rand() 함수를 활용하여 50개의 난수를 발생시켜보자.
# 이렇게 발생된 데이터를 Pandas의 시리즈형 데이터로 변환해보자.
# Pandas 시리즈형 데이터를 선형 그래프로 그려 보자.
# 동일한 데이터를 가지고 막대 그래프를 그려 보자.
#
# Solution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 문제 1)
list=np.random.rand(50)
#문제 2)
data=pd.Series(list)
plt.plot(data)
# 문제 3)
plt.show()
plt.hist(data)
#문제 4)
plt.show()
