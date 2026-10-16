# Day 02 — 문자열 인덱싱/슬라이싱 (학습자가 직접 제출한 코드)
question_code = "AIPOT-2026-0042"

exam_name = question_code[0:5]
year = question_code[6:10]
number = question_code[11:15]
last_number = question_code[14]

print(f"시험명: {exam_name}")
print(f"출제 연도: {year}")
print(f"문제 번호: {number}")
print(f"마지막 숫자: {last_number}")
