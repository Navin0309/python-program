# Example

# s = '12:01:00PM'

# Return '12:01:00'.

# s = '12:01:00AM'

# Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in 24 hour format

# Returns

# string: the time in 24 hour format

# Input Format

# A single string s that represents a time in 12-hour clock format (i.e.:hh:mm:ssAM or hh:mm:ssPM).

# Constraints

# All input times are valid

a = '07:05:45AM'
n=[]
for char in a:
    if char == 'P' or char == 'M':
        n.append(char)
for i in n:
    if i == 'P':
            b=int(a[:2])+12
            m=a.replace(a[:2],str(b)).replace(a[-2:],'')
            print(m)
            break
    else:
         q=a.replace(a[-2:],'')
         print(q)

