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