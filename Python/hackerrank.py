#Say "Hello, World!" With Python
print("Hello, World!")

#Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)

#Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

#Loops 
if __name__ == '__main__':
    n = int(input())
    
    for i in range(0,n):
        print(i*i)

#Write a Function
def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    
    return leap

year = int(input())
print(is_leap(year))

#Print Function
if __name__ == '__main__':
    n = int(input())
    s = ""
    for i in range(1,n+1):
        s += str(i)
        
    print(s)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(set(list(arr)))
    print(arr[-2])

#Nested Lists
if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #print(name, score)
        result.append([ name, score ])
        
    # fetch all grades 
    grades = [student[1] for student in result]
    unique_grades = sorted(set(grades))
        
    if len(unique_grades) == 0:
        print("No Input in List")
    elif len(unique_grades) == 1:
        lowest_grade = unique_grades[0]
        names = [name[0] for name in result if name[1] == lowest_grade]
    else:
        lowest_grade = unique_grades[1]
        names = [name[0] for name in result if name[1] == lowest_grade]
        
    for name in sorted(names):
        print(name)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # list - containing marks value
    marks = student_marks[query_name]
    subjects = len(marks)
    avg = ( sum(marks) / subjects )
    
    print(f"{avg:.2f}")

#Lists
if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        part = input().split()
        cmd = part[0]
        args = list(map(int, part[1:]))
        
        if cmd == 'print':
            print(lst)
        else:
            getattr(lst, cmd)(*args)

#Tuple
no = int(input())
str_tup = str(input())
t = tuple(map(int, str_tup.split()))
#print(t)
print(hash(t))

#sWAP cASE
def swap_case(s):
    
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join
def split_and_join(line):
    # write your code here
    return line.replace(" ", "-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#String Validators
if __name__ == '__main__':
    s = input()
    
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))

#Text Wrap
import textwrap

def wrap(string, max_width):
    final_str = ''
    
    for i in range(0, len(string), max_width):
        final_str += f"{string[i:i+max_width]}\n"

    return final_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#String Formatting
def print_formatted(number):
    # your code goes here
    wid = len(bin(number)) - 2
    for i in range(1, number+1):
        print(f"{str(i).rjust(wid)} {oct(i)[2:].rjust(wid)} {hex(i)[2:].upper().rjust(wid)} {bin(i)[2:].rjust(wid)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#The Minion Game
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    stuart, kevin = 0, 0
    n = len(string)
    
    for i in range(n):
        if string[i] in vowels:
            kevin += n-i
        else:
            stuart += n-i
            
    if stuart == kevin:
        print("Draw")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print(f"Kevin {kevin}")

#Merge the tools 
def merge_the_tools(string, k):
    # your code goes here
    length = len(string)
    
    for i in range(0, length, k):
        a = string[i:i+k]
        
        print("".join(dict.fromkeys(a)))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#Sets
#Introduction to Sets
def average(array):
    # your code goes here
    temp_set = set(array)
    length = len(temp_set)
    
    return sum(temp_set) / length
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
count_m, count_n = map(int, (input().split(" ")))
array = list(map(int, input().split(" ")))
a = set(map(int, input().split(" ")))
b = set(map(int, input().split(" ")))

happy = 0

for num in array:
    if num in a:
        happy += 1
    elif num in b:
        happy -= 1
    
print(happy)

#Symmetric Difference
size_m = int(input())
m = set(map(str, input().split(" ")))

size_n = int(input())
n = set(map(str, input().split(" ")))

diff_m = m.difference(n) #all elements which exist in M not in N
diff_n = n.difference(m) #all elements which exist in N not in M

res = list(map(int, diff_m)) 
res.extend(map(int, diff_n))
res.sort()

for num in res:
    print(num)

#Set .union() Operation
count_eng = int(input())
eng_roll = set(map(int, input().split(" ")))
count_french = int(input())
french_roll = set(map(int, input().split(" ")))

union_paper = eng_roll | french_roll

print(len(union_paper))

#Set .intersection() Operation
count_eng = int(input())
eng_roll = set(map(int, input().split(" ")))
count_french = int(input())
french_roll = set(map(int, input().split(" ")))

intersection_of_paper = eng_roll & french_roll

print(len(intersection_of_paper))

#Set .difference() Operation
count_eng = int(input())
eng_roll = set(map(int, input().split(" ")))
count_french = int(input())
french_roll = set(map(int, input().split(" ")))

difference_in_eng = eng_roll - french_roll

print(len(difference_in_eng))

#Set .symmetric_difference() Operation
count_eng = int(input())
eng_roll = set(map(int, input().split(" ")))
count_french = int(input())
french_roll = set(map(int, input().split(" ")))

sym_diff = eng_roll ^ french_roll
print(len(sym_diff))

#Set .add()
count = int(input())
countries = set()

for i in range(0, count):
    countries.add(input())

print(len(countries))

#Set Mutations



