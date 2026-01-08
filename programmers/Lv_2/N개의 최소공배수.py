def solution(arr):
    from math import gcd
    ans = arr[0]

    for c in arr:
        ans = ans * c // gcd(ans, c)

    return ans

#-----------------------------------------#
def solution(arr):
    # 최대공약수(GCD) (유클리드 호제법)
    def get_gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    # 최소공배수(LCM)
    def get_lcm(a, b):
        return (a * b) // get_gcd(a, b)

    # 배열의 첫 번째 요소부터 시작해서 연쇄적으로 LCM을 구함
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = get_lcm(answer, arr[i])

    return answer