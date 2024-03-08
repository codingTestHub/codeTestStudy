# ???
# 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.

import sys

input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [False for _ in range(n)]  # 1차원 방문 리스트 생성
min_value = sys.maxsize  # 최소값 변수


def backTracking(depth, idx):  # 깊이 변수, 인덱스 변수
    global min_value
    if depth == n // 2:  # n은 늘 짝수, 주어진 수의 절반이 한 팀으로 선택되었을 때 가지치기 시작
        p1, p2 = 0, 0   # p1->스타트, p2->링크
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:  # True값 가지는 팀 => 스타트 팀
                    p1 = p1 + graph[i][j]  # 스타트 팀의 능력치를 모두 p1에 더함
                elif not visit[i] and not visit[j]:  # 나머지 절반 False값을 가지는 팀 => 링크팀
                    p2 = p2 + graph[i][j]  # 링크 팀의 능력치를 모두 p2에 더함
        min_value = min(min_value, abs(p1 - p2))    # 2중 for문이 끝났을 때 그 둘의 차이의 절댓값(abs)이 변수보다 작으면 변수 갱신
        return

    for i in range(idx, n): # 스타트 팀을 완성 못했을 때 백트래킹 실시
        if not visit[i]:
            visit[i] = True
            backTracking(depth + 1, i + 1)  # 재귀호출
            visit[i] = False


backTracking(0, 0)
print(min_value)
