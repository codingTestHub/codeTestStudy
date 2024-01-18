n, k = map(int, input().split())        # 응시자 수, 상을 받는 사람 수
x = list(map(int, input().split()))     # 점수 입력
x.sort(reverse=True)                    # 내림차순 정렬
print(x[k-1])