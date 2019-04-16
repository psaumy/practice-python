'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
# Write your code here
string = input()
sol = []
for i in range(len(string)-7):
    current_change = []
    if 'b' != string[i]:
        current_change.append(i+1)
    if 'a' != string[i+1]:
        current_change.append(i+2)
    if 'r' != string[i+2]:
        current_change.append(i+3)
    if 'c' != string[i+3]:
        current_change.append(i+4)
    if 'l' != string[i+4]:
        current_change.append(i+5)
    if 'a' != string[i+5]:
        current_change.append(i+6)
    if 'y' != string[i+6]:
        current_change.append(i+7)
    if 's' != string[i+7]:
        current_change.append(i+8)
    sol.append([len(current_change), current_change])
    print(current_change)
print(sol)


sol.sort()
print(sol)
print(sol[0][0])
for index in sol[0][1]:
    print(index, end=' ')
print()
    
