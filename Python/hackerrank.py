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
