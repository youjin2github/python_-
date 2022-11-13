#  결측치 정재하기
import pandas as pd
import numpy as np

df = pd.DataFrame({'sex' : ['M', 'F', np.nan, 'M', 'F'],
'score' : [5,4,3,4,np.nan]})
# 결측치가 있는지 확인하기 
pd.isna(df)
# 열별 결측치 빈도 확인하기 
pd.isna(df).sum()

# 결측치가 있는 행 제거하기 
df.dropna(subset=['score'])
# 여러 변수에 결측치가 있는 행을 제거하기 
df.dropna(subset=['sex','score'])
# 결측치가 하나라도 있으면 제거하기
df_nomiss2 = df.dropna()

# 결측치 대체하기
exam = pd.read_csv('exam.csv')
exam.loc[[2,7,14], ['math']] = np.nan
print(exam)
# 평균값으로 대체하기
exam['math'].mean()
# df.fillna -> 결측치값을 다른 값으로 대체
exam['math'] = exam['math'].fillna(55)
# 마지막으로 결측치 빈도를 확인
exam['math'].isna().sum()

# 이상치 데이터 정재하기
df = pd.DataFrame({'sex' : [1,2,1,3,2,1],
'score' : [5,4,3,4,2,6]})
# 이상치 확인하기 value_counts()를 이용하여 빈도를 확인
df['sex'].value_counts().sort_index()
df['score'].value_counts().sort_index()
# 우선 이상치를 결측치로 변경
df['sex'] = np.where(df['sex'] == 3, np.nan, df['sex'])
df['score'] = np.where(df['score']>5, np.nan, df['score'])
# 결측치를 제거하고 분석을 진행
df.dropna(subset=['sex','score']).groupby('sex').agg(mean_score = ('score','mean'))

# 극단치 제거하기 
# 상자 그림 밖을 극단치라고 가정
mpg = pd.read_csv('mpg.csv')
import seaborn as sns
sns.boxplot(data=mpg, y = 'hwy')
# 1. 1사분위수, 3사분위수 구하기
pct25 = mpg['hwy'].quantile(0.25)
pct75 = mpg['hwy'].quantile(0.75)
# 2. IQR구하기
iqr = pct75 - pct25
# 3. 하한 그리고 상한 구하기
pct25 - 1.5*iqr
pct75 + 1.5*iqr
# 4. 극단치 결측값 처리하기 
mpg['hwy'] = np.where((mpg['hwy']<4.5)|(mpg['hwy']>40.5), np.nan, mpg['hwy'])
mpg['hwy'].isna().sum()
# 5. 결측치를 제거하고 분석하기
mpg.dropna(subset=['hwy']).groupby('drv').agg(mean_hwy = ('hwy','mean'))
