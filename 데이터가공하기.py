import pandas as pd
# 데이터 전처리
# query 행추출
# df[] 열[변수] 추출
# sort_values 정렬
# groupby 집단별로 나누기
# assign 변수 추가
# agg 통계치 구하기
# merge 데이터 합치기(열)
# concat 데이터 합치기(행)

# 조건에 맞는 데이터 추출하기 df.query
exam = pd.read_csv('exam.csv')
print(exam.head())
# 특정 행 추출
print(exam.query('nclass == 1'))
print(exam.query('nclass != 3'))
print(exam.query('math > 50'))
# & 그리고를 의미
print(exam.query("nclass ==1 & math >50"))
# | 또는을 의미
print(exam.query('nclass == 2 | english >= 90'))
# 여러 조건에 해당하는 변수 추출
print(exam.query('nclass in [1,3,5]'))
# 외부 변수를 이용해 추출하기
var = 3
print(exam.query('nclass == @var'))

# 변수 제거하기
print(exam.drop(columns='math'))

exam.query('nclass == 1')['english']

# 순서대로 정렬하기
print(exam.sort_values('math'))
print(exam.sort_values('math',ascending = False))
print(exam.sort_values(['nclass','math'],ascending = [True,False]))

# 파생변수 추가하기 데이터.assign(새 변수명 = 변수 만드는 공식)
exam.assign(total = exam['math'] + exam['english'] + exam["science"],
mean = (exam['math'] + exam['english'] + exam["science"])/3
)
print(exam.head())

# 집단별로 요약하기
exam.groupby('nclass').agg(mean_math = ('math','mean'))

# 데이터 합치기
# 가로로 합치기 pd.merge()
test1 = pd.DataFrame({'id':[1,2,3,4,5],
'midterm' : [60, 83, 65, 95, 80]})
test2 = pd.DataFrame({'id' : [1,2,3,4,5],
'final' : [70,83,78,80,90]})
total = pd.merge(test1, test2, how = 'left', on = 'id')
# 세로로 합치기 pd.concat()
group_a = pd.DataFrame({'id' : [1,2,3,4,5],
'test' : [60, 80, 90, 65, 90]})
group_b = pd.DataFrame({'id' : [6,7,8,9,10],
'test' : [89, 90, 98, 12, 45]})
group_all = pd.concat([group_a, group_b])
print(group_all)
# 세로로 합쳐야 하는데 변수명이 다른 경우 pd.rename()을 사용

# 인덱스 번호를 지정해 행을 추출하기
group_all.iloc[0]
group_all.iloc[[1,3]]
# x행 이상 y행 이하 추출 
group_all.loc[1:2]
# x행 이상 y행 미만 추출
group_all.iloc[1:2]
