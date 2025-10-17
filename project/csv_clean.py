import pandas as pd

# 1. CSV 파일 불러오기
df = pd.read_csv('total.csv', encoding='cp949')

# 2. 날짜 형식 통일 (문자열 -> datetime 형식으로)
df['날짜1'] = pd.to_datetime(df.iloc[:, 0], format='%Y.%m.%d', errors='coerce')
df['날짜2'] = pd.to_datetime(df.iloc[:, 3], format='%Y-%m-%d', errors='coerce')

# 3. 날짜가 모두 존재하는 행만 남기기 (결측 제거)
df = df.dropna(subset=['날짜1', '날짜2'])

# 4. 날짜1 ≠ 날짜2인 경우 → 해당 행 제거
df_matched = df[df['날짜1'] == df['날짜2']].copy()

# 5. 필요한 열만 남기기 (A-B-D-E 열만)
result = df_matched.iloc[:, [0, 1, 3, 4]]  # A-B-D-E 열 기준

# 6. 결과 저장
result.to_csv('정리된_파일.csv', index=False)

print("불일치 날짜 제거 완료. 결과 저장됨.")