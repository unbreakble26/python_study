#리스트
a = ['Life', 'is' , 'too', 'short', 'you', 'need', 'python']

print(a[4] + ' ' + a[2])

print(' '.join(a))

a = [1, 2, 3]
print(len(a))
a.append([4,5])
print(a)
a = [1, 2, 3]
a.extend([4, 5])
print(a)
a = [1, 2, 3]
print(a + [4, 5])

num = [1, 3, 5, 4, 2]
num.sort()
num.reverse()
print(num)

num2 = [1, 2, 3, 4, 5]
num2.pop(3)
num2.pop(1)
print(num2)

#튜플
tuple1 = (3,)
tuple2 = (3, 4)
print(tuple1)
print(tuple2)

a = (1, 2, 3)
a = a + (4,)
print(a)

#딕셔너리
grade = {'pey' : 10, 'julliet' : 99}
print(grade['pey'])

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

print(dic['birth'])

print(dic.keys())
print(dic.values())

print(dic.items())

print('-'*60)
print('딕셔너리 연습문제')
print('-'*60)
print('문제1')
mun1 = {'name': '홍길동', 'birth' : '1128',  'age' : '30', }
print(mun1)
print(mun1.items())
print('문제3')
a = {'A':90, 'B':80, 'C':70}
a.pop('B')
print(a.items())
print('문제4')
a = {'A':90, 'B':80}
print( a.get('C', 70) )
print('문제5')
a = {'A':90, 'B':80, 'C':70}
print( min(a.values()) )
print('문제6')
a = {'A':90, 'B':80, 'C':70}
b = list(a.items())
print( type(b) )
print( type(b[0]) )
