N = int(input())    # 시험 본 과목의 개수
score = list(map(int, input().split()))     # 현재 성적
M = max(score)      # 점수 중 최댓값

new_score =[]       # 조작한 점수

for i in score:
    new_score.append(i / M * 100)

print(sum(new_score)/N)

