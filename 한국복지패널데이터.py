import numpy as np
import pandas as pd
import seaborn as sns

# 데이터 불러오기
raw_welfare = pd.read_spss('Koweps_hpwc14_2019_beta2.sav')
# 데이터 복사본 만들기
welfare = raw_welfare.copy()

# 데이터 검토하기
welfare.head()
welfare.tail()
# 행과 열을 확인하는 shape은 ()을 붙이지 않는다
welfare.shape
welfare.info()
welfare.describe()
# 변수 이름을 변경
welfare = welfare.rename(
    columns = {'h14_g3' : 'sex', 
    'h14_g4' : 'birth',
    'h14_g10' : 'marriage_type',
    'h14_g11' : 'religion',
    'p1402_8aq1' : 'income',
    'h14_eco9' : 'code_job',
    'h14_reg7' : 'code_region'})

# 월급의 차이가 존재 확인
# 변수의 타입을 확인
welfare['sex'].dtypes
# 변수의 빈도를 확인
welfare['sex'].value_counts()
welfare['sex'].isna().sum()
# 변수의 결측값이나 이상값이 존재하지 않고 1과 2로만 이루어져있어 전처리 과정은 필요없음
# 변수가 1이면 남자 2이면 여자를 나타내기에 값의 변수명을 1->male, 2->female로 변경
welfare['sex'] = np.where(welfare['sex']==1,'male','female')
welfare['sex'].value_counts()
# 그래프로 표현
sns.countplot(data=welfare,x = 'sex')
# 월별 변수 검토 및 전처리하기
welfare['income'].dtypes
welfare['income'].describe()
# 0~1892 값을 가지는 것을 알 수 있음
sns.histplot(data = welfare, x = 'income')
# 데이터 결측치를 확인
welfare['income'].isna().sum()
# 성별 월급 월급표를 만들기
sex_income = welfare.dropna(subset=['income']).groupby('sex', as_index=False).agg(mean_income = ('income', 'mean'))

# 나이와 월급의 관계
welfare['birth'].dtypes
welfare['birth'].describe()
welfare['birth'].value_counts()
welfare['birth'].isna().sum()
# 전처리할 나이 데이터 없음 
# 태어난 연도를 이용하여 나이라는 파생변수를 생성 2022-연도+1 을 진행
welfare = welfare.assign(age = 2022 - welfare['birth'] + 1)
welfare['age'].describe()
# 나이별 평균 월급을 만들기 
age_income = welfare.dropna(subset=['income']).groupby('age').agg(mean_income = ('income','mean'))
# 연령대별 나이의 범주라는 파생변수 만들기 
welfare = welfare.assign(ageg = np.where(welfare['age']< 40, 'young',
np.where(welfare['age'] <= 60, 'middle','old')))
welfare['ageg'].value_counts()

# 직업별 월급의 차이
welfare['code_job'].dtypes
welfare['code_job'].value_counts()
# 여기서 직업은 숫자로 나와있음 이거를 글자로 대체를 하기위해 직업 분류 표를 불러와서 대체를 진행 
list_job = pd.read_excel('Koweps_Codebook_2019.xlsx', sheet_name='직종코드')
list_job.head()
list_job.shape
welfare = welfare.merge(list_job, how='left', on ='code_job')
welfare.dropna(subset=['code_job'])[['code_job','job']].head()
