# ???
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# 코드1의 수행 횟수는 등차 수열의 합 공식으로 구할 수 있다.

n = int(input())
print(int(n*(n-1)-(n-1)*n/2))
print(2)