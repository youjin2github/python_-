# 패키지 로딩
import pandas as pd
import numpy as np

# 파일 불러오기
exam = pd.read_csv('exam.csv')
print(exam)

# 앞부분 데이터 확인
# 0~5행까지 출력
print(exam.head())
# 0~특정 행까지 출력
print(exam.head(10))

# 뒷부분 데이터 확인
print(exam.tail())
print(exam.tail(10))

# 데이터의 행과 열을 확인
print(exam.shape)

# 변수의 속성을 확인
print(exam.info())

# 요약 통계량 구하기
print(exam.describe())

df_raw = pd.DataFrame({'var1' : [1,2,1],
'var2' : [2,3,2]})
print(df_raw)

# 데이터 프레임 복사본 만들기
df_new = df_raw.copy()
print(df_new)

# 프레임 내에 변수중 하나의 명칭을 변경하기
# var2 -> v2로 변경
df_new = df_new.rename(columns={'var2' : 'v2' })
print(df_new)

# 파생변수 만들기
df = pd.DataFrame({'var1' : [4,3,8], 
'var2' : [2,6,1]})
df['var_sum'] = df['var1'] + df['var2']
df['var_mean'] = (df['var1']+df['var2'])/2
print(df)

mpg = pd.read_csv('mpg.csv')
mpg['total'] = (mpg['cty'] + mpg['hwy'])/2
print(mpg.head())

# 조건문을 이용하여 파생변수 만들기
mpg['total'].describe()

# 그래프 만들기
mpg['total'].plot.hist()

# 조건에 따라 합격 판정 변수 만들기
mpg['test'] = np.where(mpg['total']>=20, 'pass', 'fail')
print(mpg.head())
# 빈도 확인하기 
print(mpg['test'].value_counts())
# 막대그래프로 빈도 표현하기
count_test = mpg['test'].value_counts()
# 축 이름 수평으로 만들기 rot = 0
count_test.plot.bar(rot = 0)
mpg['grade'] = np.where(mpg['total']>30, 'A',
np.where(mpg['total']>20,'B','C'))
print(mpg.head())
# 빈도표
count_grade = mpg['grade'].value_counts().sort_index()
count_grade.plot.bar(rot = 0)

# 여러가지 중 하나의 조건에 해당하는 변수를 따로 추출하기
mpg['size'] = np.where(mpg['category'].isin(['compact', 'subcompact', '2seater']), 'small', 'large')
print(mpg.head())

