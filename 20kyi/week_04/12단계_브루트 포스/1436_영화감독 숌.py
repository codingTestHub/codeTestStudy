# ???
n = int(input())
cnt = 0             # 종말번호를 업데이트 시킬 카운트값
result = 666        # 종말번호

while 1:
    if '666' in str(result):    # 만약 종말번호안에 666이 포함되어 있으면
        cnt += 1
    if cnt == n:                # 그 카운트값이 입력값과 같다면
        break
    result += 1                 # 종말번호를 계속해서 1씩 증가
print(result)                   # 입력한 n번째의 종말번호 출력

# if n == 1:
#     print(666)
# else:
#     print(n - 1, 666, sep="")
#     if "6" in n:
#         print(n - 1, 66)
