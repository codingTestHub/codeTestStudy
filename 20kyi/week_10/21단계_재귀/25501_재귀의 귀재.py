# ???
# 팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열

import sys

input = sys.stdin.readline

t = int(input())


def recursion(s, l, r):
    global cnt  # 함수 내 전역변수
    cnt += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def palindrome(s):
    return recursion(s, 0, len(s) - 1)

# 힌트 코드 삭제
# print('ABBA:', palindrome('ABBA'))
# print('ABC:', palindrome('ABC'))

for i in range(t):
    cnt = 0
    s = input().rstrip()    # rstrip() 써줘야 함...ㅠㅠ
    print(palindrome(s), cnt)
