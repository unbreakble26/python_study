def casar(word, n):
    result = ""
    alphabat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in word:
        index = alphabat.index(i)
        result += alphabat[ (index + n) %26]

    return result

print( casar("CAT", 5) )
print( casar("ZZZ", 5) )

print('"점프 투 파이썬" 문제를 풀어보자')
print('''Life is too short
You need Python''')

print(" "*24 + "PYTHON")

jumin = "881120-1068234"
yyyymmdd = jumin[:6]
num = jumin[7:]
print(yyyymmdd)
print(num)

word = "Life is too short, you need python"
index1 = word.index('short')
print(index1)

chi = "a:b:c:d"
print(chi.replace(':', '#'))

chi2 ="a:b:c:d"
chi2_1 = chi2.split(":")
print(chi2_1)
print(type(chi2_1))
chi2_2 = "#".join(chi2_1)
print(chi2_2)
