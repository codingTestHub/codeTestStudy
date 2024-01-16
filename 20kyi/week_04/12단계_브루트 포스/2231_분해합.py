# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.

n = int(input())
for i in range(1, n+1):
    n_list = list(map(int, str(i)))     # 1~n 까지의 숫자 리스트
    result = sum(n_list) + i            # i와 i의 각 자릿수의 합 => 분해합 공식
    if result == n:                     # 생성자일 경우
        print(i)
        break
else:
    print(0)