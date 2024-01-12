# #땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

A, B, V = map(int, input().split())

# 총 올라가야 할 거리 = V - B
# 하루에 올라갈 수 있는 거리 = A - B

result = (V - B) // (A - B)

if (V - B) % (A - B) == 0:      # 낮에 다 올라가는 경우
    print(result)
else:                           # 밤에 미끄러지는 경우 하루 더 증가
    print(result + 1)
