# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

sum_x = 0
for i in range (0, size):
    sum_x += x[i]*w[i]

print(round(sum_x/sum(w),1))