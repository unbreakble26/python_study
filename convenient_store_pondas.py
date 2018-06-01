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

#조건 값 주고 Group 화하기
print('-'*45)

def more_than_6000(x):
    if x >= 6000:
        return 'A Group'
    else:
        return 'B Group'

data['more_than_6000_2'] = data.hourly_wage.map( lambda x : more_than_6000(x) )
print( data.head(4) )
print( type( data['more_than_6000_2']) )

#전국 데이터에서 구 정보 / 시급 데이터만을 추출 하여 시급 기준 내림차순으로 정렬 해보겠습니다.
data2 = data[data.more_than_6000 == True][ ['area1', 'hourly_wage'] ]
data2 = data2.sort_values(by='hourly_wage', ascending=0)
print(data2)

#csv파일로 추출하기 --> 깨짐
data.to_csv('data_changing.csv', index=False)

#그래프로 그리기
'''bins = 10 : 구간을 10구간으로 설정.'''
#data['hourly_wage'].hist(bins=10)
#matplotlib.pyplot.show()

#boxplot
#data.boxplot(column='hourly_wage', return_type = 'dict')
#matplotlib.pyplot.show()

# boxplot 중 name으로 여러개 측정
# data.boxplot(column='hourly_wage', by='name')
# matplotlib.pyplot.show()

# boxplot 중 구별로
# data.boxplot(column='hourly_wage', by='area1')
# matplotlib.pyplot.show()

# x/y축 변경 y축 폰트 추가
data.boxplot(column='hourly_wage', by='area1', vert=False)
matplotlib.pyplot.yticks(fontsize=9) #폰트 사이즈 설정
matplotlib.pyplot.show()
