# your code goes here
dp = [[0 for _ in range(5001)], [0 for _ in range(5001)]]

def main():
    l = int(input())
    string = input()

    for i in range(l-1, -1, -1):
        for j in range(i+1, l):
            if string[i]==string[j]:
                dp[i%2][j] = dp[(i+1)%2][j-1]
            else:
                dp[i%2][j] = 1+min(dp[i%2][j-1], dp[(i+1)%2][j])

    print(dp[0][l-1])
        
main()








