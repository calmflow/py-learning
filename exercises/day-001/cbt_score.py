question = 40
correct_answer = 27
wrong_answer = question - correct_answer

correct_ratio = correct_answer / question * 100

scaled_score = correct_answer * (100 / question)
score_to_pass = 70
lack_score = score_to_pass - scaled_score

print(f"전체 문항: {question}개")
print(f"정답 문항: {correct_answer}개")
print(f"오답 문항: {wrong_answer}개")
print(f"정답률: {correct_ratio:.1f}%")
print(f"환산 점수: {scaled_score:.1f}점")
print(f"합격까지 필요한 점수: {lack_score:.1f}점")
