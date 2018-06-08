from pandas import DataFrame, Series

print('--------Data Frame 만들어 보기')
data = {
'name':['박대성', '백상훈', '이권수', '이우현'],
'money':[5000, 2000000, 5000000, 80000000],
'sex':['M', 'M', 'M', 'M']
}

print(data)
print('---------dict --> DataFrame 변경---')
df = DataFrame(data)
print(df)
print(type(df))
print('------------------')
df = DataFrame(data, columns=['money', 'sex', 'name' ])
print(df)
print(type(df))
print('---------iloc / loc ------')
print( df.iloc[0:2] )
print('-------------------------------------------')
print( df.loc[0] )



print('---열 추가 -----')
df['level'] = df['money'] > 5000
print(df)

print('---data 추출-----')
print( df[df.name == '박대성'] )
print( df[ (df.money > 10000) & (df.sex == 'M') ] )

print('----행 과 열 치환------')
print( df.transpose() )
