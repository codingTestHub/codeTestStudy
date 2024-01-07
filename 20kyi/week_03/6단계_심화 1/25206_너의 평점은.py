# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_grade = 0  # 학점 총합
total_score = 0  # 학점 * 과목평점

for _ in range(20):
    subject, credit, grade = input().split()  # 과목, 학점, 성적 입력
    credit = float(credit)

    if grade != "P":
        total_grade += credit
        total_score += credit * score_list[grade_list.index(grade)]  # grade_list에서 해당하는 등급을 가져옴

print('%.6f' % (total_score / total_grade))
