#1) 이름분석
data = '이의덕,이재명,권종수,이재수,박철호,강동희,이재수,김지석,최승만,이성만,박영희,박수호,전경식,송우환,김재식,이유정'

''',를 기점으로 이름을 통째로 배열 안에 넣어준다.'''
names = data.split(",")
print(names)
print(names[1])
park = 0
kim = 0

for name in names:
    print(name)

for name in names:
    if name.startswith('박'):
        park += 1
    elif name.startswith('김'):
        kim += 1
#a)김씨 / 박씨 명수
print("김씨 : %d 명, 박씨 : %d 명"  %(kim, park))
#b)이재수는 몇명?
print("이재수 : %d명" %names.count('이재수'))

# set : 집합 자료형 - 순서가 없고, 중복 없음(집합 같음)
names2 = list(set(names))
print(names)
print(set(names))
#c) 중복제거 이름
print(names2)
#d) 중복제거 오름차순
print(sorted(names2))

#2) 제곱의 합 / 합의 제곱
sum1 = 0
sum2 = 0

for i in range(1, 100+1):
    sum1 = sum1 + i**2
    sum2 = sum2 + i
sum2 = sum2 ** 2
print("제곱의 합 : %d" %sum1)
print("합의 제곱 : %d" %sum2)

print("두 합의 차 : %d" %(sum2-sum1))

#3)1부터 100까지의 각 숫자의 갯수 구하기
'''
10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5
'''
#defaultdict : dict형 자료형 중 키값을 자동으로 생성.
from collections import defaultdict

d = defaultdict(int)
for number in range(1, 100+1):
    for c in str(number):
        d[c] += 1

print(dict(d))

#4) DashInsert
'''
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 
문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 
짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3)
'''
data = "4546793"

''' int라는 함수는 string형을 숫자로 바꿔줌. 
    map(int, data) 에서 map은 data의 라는 리스트를 하나하나 쪼개서 int로 바꿔주는 행위
    모두 쪼갠 뒤 numbers에 하나하나 리스트로 넣어준다.
'''
numbers = list( map(int, data) )
result = []

for i, num in enumerate(numbers):
    result.append(str(num)) # 문자로 바꾸어 하나하나 추가해 준다.
    if i < len(numbers)-1: # 마지막 수 전까지라면

        is_odd = num % 2 == 1 #현재 수 홀수
        is_next_odd = numbers[i+1] % 2 == 1 #다음 수 홀수

        if is_odd and is_next_odd: # 둘 다 연속 홀수라면
            result.append("-")
        elif not is_odd and not is_next_odd: # 둘 다 연속짝수라면
            result.append("+")


print(result)
# join : 리스트에서 문자열로!
print("".join(result))

#5) 문자열 압축
'''
입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
'''

def compress_string(s):
    _c = ""
    cnt = 0
    result = ""

    for c in s:
        if c != _c:
            _c = c
            if cnt: result = result + str(cnt)
            result = result + c
            cnt = 1
        else:
            cnt = cnt + 1

    if cnt: result += str(cnt)
    return result

print( compress_string("aaabbcccccca") )

