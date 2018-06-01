import pandas
import matplotlib

data = pandas.read_csv('C:/Users/J/Desktop/RStudy/Data-master/convenient_store.csv')
data.head(8)

print('-'*45)
data.info()

print('-'*45)
print(data.describe())

print('-'*45)
print(data.area.describe())

print('-'*45)
high_wage = data[data.hourly_wage >= 6000]
print( high_wage.head(8) )

print('-'*45)
print( high_wage.sort_values(by='hourly_wage', ascending=0 ).head(10) )

print('-'*45)
b = data[(data.hourly_wage >= 6000) & (data.area1=='마포구')]
print(b)
# CU 편의점 골라보기
print('-'*45)
cu = data[data.company.str.contains('CU')]
print(cu)

print('-'*45)
cu = data[data.name=='CU']
print(cu)
#PC방 업종 알아보기
pc_room_data = data[data.company.str.upper().str.contains('PC')]
print(pc_room_data)

#칼럼 추가
print('-'*45)
data['seoul'] = 'in seoul'
print(data.head())

#조건 값으로 column값 채우기
print('-'*45)
data['more_than_6000'] = data['hourly_wage']>=6000
print(data.head())

print('-'*45)
print(data[data.more_than_6000 == True].describe())
