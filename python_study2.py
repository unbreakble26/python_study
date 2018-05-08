# [풀이6] Duplicate Numbers
def chkDupNum(s):
    result = [ ]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum("0123456789")) # True 리턴
print(chkDupNum("01234")) # False 리턴
print(chkDupNum("01234567890")) # False 리턴
print(chkDupNum("6789012345")) # True 리턴
print(chkDupNum("012322456789")) # False 리턴

# 리스트 자료형을 이용하여 중복된 값이 있는지 먼저 조사한다. 중복된 값이 있을 경우는 False를 리턴한다. 최종적으로 중복된 값이 없을 경우 0~9까지의 숫자가 모두 사용되었는지 판단하기 위해 입력 문자열의 숫자값을 저장한 리스트 자료형의 총 개수가 10인지를 조사하여 10일 경우는 True, 아닐 경우는 False를 리턴한다.
#
# [풀이7] 모스 부호 해독
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
# 모스 부호 규칙 표를 딕셔너리로 작성한 후 입력에 해당되는 모스 부호 문자열을 먼저 단어(공백문자 2개)로 구분한다. 그 후 단어(공백문자 1개)를 문자로 구분하여 해당 모스 부호값을 딕셔너리에서 찾아서 그 결과값을 구한다.
#
# [풀이8] 정규식 1
# 보기 중 이 조건에 해당되는 것은 B이다.
#
# 다음은 위 문제의 정규식 매치 결과를 확인해 보는 파이썬 코드이다.

import re

p = re.compile("a[.]{3,}b")

print (p.match("acccb")) # None
print (p.match("a....b")) # 매치객체 출력
print (p.match("aaab")) # None
print (p.match("a.cccb")) # None

# [풀이9] 정규식 2
# 정규식 “[a-z]+”은 소문자로 이루어진 단어를 뜻하므로 “5 python”이라는 문자열에서 “python”과 매치될 것이다. 따라서 “python”이라는 문자열의 시작 인덱스(m.start())는 2이고 마지막 인덱스(m.end())는 8이므로 10이 출력된다.

import re

p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end()) # 10 출력
# [풀이10] 정규식 3
# 전화번호 패턴은 다음과 같이 작성할 수 있다.

pat = re.compile("\d{3}[-]\d{4}[-]\d{4}")
# 이 전화번호 패턴 중 뒤의 숫자 4개를 변경할 것이므로 필요한 앞부분을 다음과 같이 그룹핑한다.

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
# 컴파일된 객체 pat에 sub 함수를 이용하여 다음과 같이 문자열을 변경한다.

import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)

# [풀이11] 정규식 4
# .com과 .net에 해당되는 이메일 주소만을 매치하기 위해서 이메일 주소의 도메인 부분에 다음과 같은 긍정형 전방탐색 패턴을 적용한다.

pat = re.compile(".*[@].*[.](?:com$|net$).*$")
# 다음은 위 패턴을 적용한 파이썬 코드이다.

import re

pat = re.compile(".*[@].*[.](?:com$|net$).*$")

print (pat.match("pahkey@gmail.com"))
print (pat.match("kim@daum.net"))
print (pat.match("lee@myhome.co.kr"))
# [풀이12] XML 문서 작성과 저장
from xml.etree.ElementTree import Element, SubElement, ElementTree

blog = Element("blog")
blog.attrib["date"] = "20151231"

SubElement(blog, "subject").text = "Why python?"
SubElement(blog, "author").text = "Eric"
SubElement(blog, "content").text = "Life is too short, You need Python!"

ElementTree(blog).write("blog.xml")
# [풀이13] json 데이터
# json파일을 읽어 딕셔너리로 저장한 후 값을 변경하고 변경된 값을 다시 json파일에 저장한다.

import json

with open('myinfo.json') as f:
    data = json.load(f)  # json파일을 읽고 딕셔너리로 저장한다.

data['age'] = 40  # age 값을 40으로 변경

with open('myinfo.json', 'w') as f:
    json.dump(data, f, indent=4)  # 딕셔너리를 json 파일로 저장한다.
# [풀이14] 요소값으로 소트하기
# 다음은 operator모듈의 itemgetter함수를 이용하여 소트하는 방법이다. students의 아이템의 2번째 항목으로 소트해야 하기 때문에 sorted의 key함수로 itemgetter(1)을 사용한다.

from operator import itemgetter

students = [
    ("홍길동", 22),
    ("김철수", 32),
    ("박영희", 17),
]

students = sorted(students, key=itemgetter(1))

print(students)
