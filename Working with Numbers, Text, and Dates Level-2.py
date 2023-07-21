'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Working with Numbers, Text, and Dates

'''Calculating Numbers with Functions
A function in Python is similar to a function on a calculator, in that you pass something into the function, and the function passes something back. For example, 
most calculators and programming languages have a square root function: You 
give them a number, and they give back the square root of that number.

Python functions generally have the syntax:
variablename = functioname(param[,param])
Because most functions return some value, you typically start by defining a variable to store what the function returns. Follow that with the = sign and the function name, followed by a pair of parentheses. Inside the parentheses you may pass 
one or more values (called parameters) to the function.
For example, the abs() function accepts one number and returns the absolute 
value of that number. If youre not a math nerd, this just means if you pass it a 
negative number, it returns that same number as a positive number. If you pass it 
a positive number, it returns the same number you passed it. In other words, the 
abs() function simply converts negative numbers to positive numbers.'''

x=-4.1324
y=abs(x)
z=round(x,2)
print(x)
print(y)

'''
Some Built-In Python Functions for Numbers
Built-In Function Purpose

abs(x) Returns the absolute value of number x (converts negative numbers to positive).

bin(x) Returns a string representing the value of x converted to binary.

float(x) Converts a string or number x to the float data type.

format(x, y) Returns x formatted according to the a pattern specified in y. This older syntax has 

been replaced with f-strings in current Python versions.

hex(x) Returns a string containing x converted to hexadecimal, prefixed with 0x.

int(x) Converts x to the integer data type by truncating (not rounding) the decimal 

portion and any digits after it.

max(x, y, z, ...) Takes any number of numeric arguments and returns whichever is the largest.

min(x, y, z, ...) Takes any number of numeric arguments and returns whichever is the smallest.

oct(x) Converts x to an octal number, prefixed with 0o to indicate octal.

round(x, y) Rounds the number x to y number of decimal places.

str(x) Converts the number x to the string data type.

type(x) Returns a string indicating the data type of x.

'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Still More Math Functions
In addition to the built-in functions you’ve learned about so far, still others you 
can import from the math module. If you need them in an app, put import math
near the top of the .py file or Jupyter cell to make those functions available to the 
rest of the code. Or to use them at the command prompt, first enter the import 
math command.
One of the functions in the math module is the sqrt() function, which gets the 
square root of a number. Because it’s part of the math module, you can’t use it 
without importing the module first. For example, if you enter the following, you’ll 
get an error because sqrt() isn’t a built-in function:
'''

import math
print(math.sqrt(81))

'''
Some Functions from the Python Math Module
Built-In Function Purpose

math.acos(x) Returns the arccosine of x in radians

math.atan(x) Returns the arctangent of x, in radians

math.atan2(y, x) Converts rectangular coordinates (x, y) to polar coordinates (r, theta)

math.ceil(x) Returns the ceiling of x, the smallest integer greater than or equal to x

math.cos(x) Returns the cosine of x radians

math.degrees(x) Converts angle x from radians to degrees

math.e Returns the mathematical constant e (2.718281 . . .)

math.exp(x) Returns e raised to the power x, where e is the base of natural logarithms

math.factorial(x) Returns the factorial of x

math.floor() Returns the floor of x, the largest integer less than or equal to x

math.isnan(x) Returns True if x is not a number; otherwise returns False

math.log(x, y) Returns the logarithm of x to base y

math.log2(x) Returns the base-2 logarithm of x

math.pi Returns the mathematical constant pi (3.141592 . . .)

math.pow(x, y) Returns x raised to the power y

math.radians(x) Converts angle x from degrees to radians

math.sin(x) Returns the sine of x, in radians

math.sqrt(x) Returns the square root of x

math.tan(x) Returns the tangent of x radians

math.tau() Returns the mathematical constant tau (6.283185 . . .)

'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Formatting Numbers

'''Formatting with f-strings
Format strings, or f-strings, are the easiest way to format data in Python. All you 
need is a lowercase f or uppercase F followed immediately by some text or expressions enclosed in quotation marks. Here is an example:
f"Hello {username}"'''

username="anya"
print(f"Hello {username}")

unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}")

'''
The .2f means “two decimal places, fixed” (never any more or less than two 
decimal places). The following code will display the number with commas and 
two decimal places:

'''

print(f"Subtotal: ${quantity * unit_price:,.2f}")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")

#Formatting percent numbers

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")
print(f"Sales Tax Rate {sales_tax_rate:.2%}")

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Making multiline format strings

'''» Use /n: You can use a single-line format string with \n any place you want a 
line break. Just make sure you put the \n in the literal portion of the format 
string, not inside curly braces. For example:'''

user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
output=f"{user1} \n{user2} \n{user3}"
print(output)
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Formatting width and alignment

'''You can also control the width of your output (and the alignment of content within 
that width) by following the colon in your f-string with < (for left aligned), ^ (for 
centered), or > (for right aligned). Put any of these characters right after the colon 
in your format string. For example, the following will make the output 20 characters wide, with the content right aligned:
:>20'''

unit=6.545
quan=22
tax=0.3
subtot=quan*unit
saletax=tax*subtot
total=subtot+tax
out1=f""" sub: ${subtot:,.2f}
tax: ${tax:,.2f}
total: ${total:,.2f}"""
out=f""" sub: ${subtot:>9,.2f}
tax: ${tax:>9,.2f}
total: ${total:9>,.2f}"""
print(out)
print(out1)

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''System           Also Called          Digits                         Used Symbol Function
Base 2                Binary                0,1                                0b         bin()
Base 8                Octal               0,1,2,3,4,5,6,7                       0o        oct()
Base 16           Hexadecimal or hex    0,1,2,3,4,5,6,7,8,9, A,B,C,D,E,F        0x        hex()
'''
x=225
print(bin(x))
print(oct(x))
print(hex(x))


#Complex numbers

'''Anyway, if your application requires working with complex numbers, you can use 
the complex() function to generate an imaginary number, using the following 
syntax:

complex(real,imaginary)

Replace real with the real part of the complex number, and replace imaginary
with the imaginary number. For example, in code or the command prompt, try 
this:

z = complex(2,-3)
'''
z = complex(2,-3)
print(z)
print(z.imag)
print(z.real)

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Manipulating Strings

#Concatenating strings
'''You can join strings by using a + sign. The process of doing so is called string 
concatenation in nerd-o-rama world. One thing that catches beginners off-guard 
is the fact that a computer doesn’t know a word from a bologna sandwich. So 
when you join strings, the computer doesn’t automatically put spaces where you’d 
expect them. For example, in the following code, full_name is a concatenation of 
the first three strings.'''

first_name = "Alan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name+middle_init + last_name
print(full_name)

'''Nothing is wrong with this output, per se, except that we usually put spaces 
between words and the parts of a person’s name.
Because Python won’t automatically put in spaces where you think they should 
go, you have to put them in yourself. The easiest way to represent a single space is 
by using a pair of quotation marks with one space between them, like this:

" "

If you forget to put the space between the quotation marks, like the following, you 
won’t get a space in your string because there’s no space between the quotation 
marks:

""

'''
first_name = "Alan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + " " + middle_init + ". " + last_name
print(full_name)

#Getting the length of a string

'''To determine how many characters are in a string, you use the built-in len()
function (short for length). The length includes spaces because spaces are characters, each one having a length of one. An empty string — that is, a string with 
nothing in it, not even a space — has a length of zero'''

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))

#Working with common string operators
'''
Operator               Purpose
x in s                Returns True if x exists somewhere in string s.
x not in s            Returns True if x is not contained in string s.
s * n or n * s        Repeats string s n times.
s[i]                  The ith item of string s where the first character is 0.
s[i:j]                A slice from string x beginning with the character at position i through to the 
                        character at position j.
s[i:j:k]              A slice of s from i to j with step k.
min(s)                The smallest (lowest) character of string s.
max(s)                The largest (highest) character of string s.
s.index(x[, i[, j]])  The numeric position of the first occurrence of x in string s. The optional i and 
                           j limit the search to the characters from i to j.
s.count(x)            The number of times string x appears in larger string s.
'''

s="Abracadabra Hocus Pocus you're a turtle dove" 

# Is there a Lowercase Letter t is contained in S?
print("t" in s)

# Is there an uppercase Letter t is contained in S? 
print("1" in s)

# Is there no uppercase T in s?S
print("T" not in s) 

#Print 15 hyphens in a row
print("_"*15)

# Print first character in string X
print(s[0])

# Print characters 33 - 39 from string x 
print(s[33:39])

#Print every third character in s starting at zero 
print(s[0:44:3])

#Print Lowest character is s (a space is lower than the Letter a) 
print(min(s))

#Print the highest character is s 
print(max(s)) 

#Where is the first uppercase P
print(s.index("P"))

#Where is the first Lowercase & in the latter half of string s 
#Note that the returned value still starts counting from zero 
print(s.index("o",22,44))

#How many Lowercase Letters a are in string s?
print(s.count("a"))


'''
Below are the ASCII values of printable characters (33, 126):,
Character	Character Name	ASCII code
!	Exclamation point	33
“	Double quotation	34
#	Number sign	35
$	Dollar sign	36
%	Percent sign	37
&	ampersand	38
‘	apostrophe	39
(	Left parenthesis	40
)	Right parenthesis	41
*	asterisk	42
+	Plus sign	43
,	comma	44
–	hyphen	45
.	period	46
/	slash	47
0	zero	48
1	one	49
2	two	50
3	three	51
4	four	52
5	five	53
6	six	54
7	seven	55
8	eight	56
9	nine	57
:	colon	58
;	semi-colon	59
<	Less-than sign	60
=	Equals sign	61
>	Greater-than sign	62
?	Question mark	63
@	At sign	64
Character	Character Name	ASCII code
A	Uppercase a	65
B	Uppercase b	66
C	Uppercase c	67
D	Uppercase d	68
E	Uppercase e	69
F	Uppercase f	70
G	Uppercase g	71
H	Uppercase h	72
I	Uppercase i	73
J	Uppercase j	74
K	Uppercase k	75
L	Uppercase l	76
M	Uppercase m	77
N	Uppercase n	78
O	Uppercase o	79
P	Uppercase p	80
Q	Uppercase q	81
R	Uppercase r	82
S	uppercases	83
T	Uppercase t	84
U	Uppercase u	85
V	Uppercase v	86
W	Uppercase w	87
X	Uppercase x	88
Y	Uppercase y	89
Z	Uppercase z	90
[	Left square bracket	91
\	backslash	92
]	Right square bracket	93
^	caret	94
_	underscore	95
`	Grave accent	96
Character	Character Name	ASCII code
a	Lowercase a	97
b	Lowercase b	98
c	Lowercase c	99
d	Lowercase d	100
e	Lowercase e	101
f	Lowercase f	102
g	Lowercase g	103
h	Lowercase h	104
i	Lowercase i	105
j	Lowercase j	106
k	Lowercase k	107
l	Lowercase l	108
m	Lowercase m	109
n	Lowercase n	110
o	Lowercase o	111
p	Lowercase p	112
q	Lowercase q	113
r	Lowercase r	114
s	Lowercase s	115
t	Lowercase t	116
u	Lowercase u	117
v	Lowercase v	118
w	Lowercase w	119
x	Lowercase x	120
y	Lowercase y	121
z	Lowercase z	122
{	Left curly brace	123
|	Vertical bar	124
}	Right curly brace	125
~	tilde	126
'''
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#Manipulating strings with methods
'''
Method                                     Purpose
s.capitalize()                        Returns a string with the first letter capitalized and the rest lowercase.

s.count(x, [y, z])                    Returns the number of times string x appears in string s. Optionally, you can add y
                                        as a starting point and z as an ending point to search a portion of the string.

s.find(x, [y, z])                     Returns a number indicating the first position at which string x can be found in 
                                        string s. Optional y and z parameters allow you to limit the search to a portion of the string. Returns –1 if none found.

s.index(x, [y, z])                    Similar to find but returns a “substring not found” error if string x can’t be found in string y.

s.isalpha()                           Returns True if s is at least one character long and contains only letters (A-Z or a-z).

s.isdecimal()                         Returns True if s is at least one character long and contains only numeric characters (0-9).

s.islower()                           Returns True if s contains letters and all those letters are lowercase.

s.isnumeric()                         Returns True if s is at least one character long and contains only numeric characters (0-9).

s.isprintable()                       Returns True if string s contains only printable characters.

s.istitle()                           Returns True if string s contains letters and the first letter of each word is uppercase followed by lowercase letters.

s.isupper()                           Returns True if all letters in the string are uppercase.

s.lower()                             Returns s with all letters converted to lowercase.

s.lstrip()                            Returns s with any leading spaces removed.

s.replace(x, y)                       Returns a copy of string s with all characters x replaced by character y.

s.rfind(x, [y, z])                    Similar to s.find but searches backward from the start of the string. If y and z
                                           are provided, searches backward from position z to position y. Returns –1 if string x not found

s.rindex()                             Same as s.rfind but returns an error if the substring isn’t found.

s.rstrip()                             Returns string x with any trailing spaces removed.

s.strip()                              Returns string x with leading and trailing spaces removed.

s.swapcase()                           Returns string s with uppercase letters converted to lowercase and lowercase 
                                            letters converted to uppercase.

s.title()                              Returns string s with the first letter of every word capitalized and all other letters 
                                               lowercase.

s.upper()                              Returns string s with all letters converted to uppercase.

'''

s1 = "There is no such word as schmeedledorp"

s2 ="  a b c  "

s3="ABC"

#Captialize first letter, the rest Lowercase
print(s3.capitalize()) 

# Count the number of spaces in s1
print (s1.count(" ")) 

# Find the dot in $4
print(s3.find("."))

#Is s2 all Lowercase Letters?
print(s2.islower())

# Convert s3 to all Lowercase
print (s3.lower())

#String Leading characters from 52 
print (s2.lstrip())

# String Leading and trailing characters from s2 
print (s2.strip())

#Swap the case of Letters in si
print(s1.swapcase())

#Show s1 in title case (initial caps)
print(s1.title()) 

# Show s1 uppercase
print(s1.upper())

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Uncovering Dates and Times

# Import the datetime module, nickname dt
import datetime as dt
# Store today's date in a variable named today.
today = dt.date.today()
# Store some other date in a variable called last_of_teens
last_of_teens = dt.date(2019, 12, 31)
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)

'''Directive           Description                            Example
%a                  Weekday, abbreviated                          Sun
%A                      Weekday, full                            Sunday
%w                  Weekday number 0-6, where 0 is Sunday          0
%d                      Number day of the month 01-31              31
%b                        Month name abbreviated                    Jan
%B                           Month name full                     January
%m                           Month number 01-12                       01
%y                          Year without century                      19
%Y                           Year with century                       2019
%H                                Hour 00-23                          23
%I                                 Hour 00-12                         11
%p                               AM/PM                                PM
%M                              Minute 00-59                           01
%S                             Second  00-59                           01
%f                              Microsecond 000000-999999              495846
%z                            UTC offset                                -0500
%Z                             Time zone                                EST
%j                          Day number of year 001-366                   300
%U                          Week number of year, Sunday as the first
                                 day of week, 00-53                        50
%W                          Week number of year,
                           Monday as the first day of week, 00-53          50
%c                          Local version of date and time                Tue Dec 31 23:59:59 2018
%x                             Local version of date                       12/31/18
%X                           Local version of time                         23:59:59
%%                              A % character                                   %

'''
print(f"{last_of_teens:%A, %B %d, %Y}")
todays_date = f"{today:%m/%d/%Y}"


'''
Format String                                 Example
%a, %b %d %Y                               Sat, Jun 01 2019
%x                                          06/01/19
%m-%d-%y                                  06-01-19
This %A %B %d                            This Saturday June 01
%A %B %d is day number %j of %Y        Saturday June 01 is day number 152 of 2019

'''
#variable = dt.time([hour,[minute,[second,[microsecond]]]])

midnight = dt.time()
print(midnight)

almost_midnight = dt.time(23, 59, 59, 999999)
print(almost_midnight)

'''
Format String                           Example
%I:%M %p                                 11:59 PM
%H:%M:%S and %f microseconds          23:59:59 and 999999 microseconds
%X                                         23:59:59

'''

import datetime as dt
right_now = dt.datetime.now()
print(right_now)

'''You can also define a datetime using any the following parameters. The month, 
day, and year are required. The rest are optional and set to 0 in the time if you 
omit them.

datetime(year, month, day, hour, [minute, [second, [microsecond]]])

Here is an example using 11:59 PM on December 31 2019:

'''

new_years_eve = dt.datetime(2019, 12, 31, 23, 59)
print(new_years_eve)


'''
Format String                                Example
%A, %B %d at %I:%M%p             Tuesday, December 31 at 11:59PM
%m/%d/%y at %H:%M%p                     12/31/19 at 23:59
%I:%M %p on %b %d                     11:59 PM on Dec 31
%x                                          12/31/19
%c                                 Tue Dec 31 23:59:00 2019
%m/%d/%y at %I:%M %p                  12/31/19 at 11:59 PM
%I:%M %p on %m/%d/%y                  1:59 PM on 12/31/2019

'''
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Calculating timespans

import datetime as dt
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day

'''The timedelta calculation happens automatically when you subtract one date 
from another to get the time between. You can also define any timedelta (duration) using this syntax:

datetime.timedelta(days=, seconds=, microseconds=, milliseconds=, minutes=, 
hours=, weeks=)'''

import datetime as dt
new_years_day = dt.date(2019, 1, 1)
duration = dt.timedelta(days=146)
print(new_years_day + duration)

import datetime as dt
memorial_day = dt.date(2019, 5, 27)
duration = dt.timedelta(days=146)
print(memorial_day - duration)

'Two, printing the type() of that data type tells us it’s a timedelta object (a duration), not an o’clock time'

import datetime as dt
start_time = dt.datetime(2019, 3, 31, 8, 0, 0)
finish_time = dt.datetime(2019, 3, 31, 14, 34, 45)
time_between = finish_time - start_time
print(time_between)
print(type(time_between))

import datetime as dt
now = dt.datetime.now()
birthdatetime = dt.datetime(1995, 3, 31, 8, 26)
age = now - birthdatetime
print(age)
print(type(age))


import datetime as dt
today = dt.date.today()
birthdate = dt.date(2000, 12, 31)
delta_age = (today - birthdate)
print(delta_age)

delta_age = (today - birthdate)
days_old = delta_age.days
print(days_old, type(days_old))

years_old = days_old // 365
print(years_old)

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Working with Time Zones


'''When you get the time from your computer’s system clock, it’s for your time zone, 
but you don’t have an indication of what that time zone is. But you can tell the 
difference between your time and UTC time by comparing .now() for your location to .utc_now()'''

here_now=dt.datetime.now() #computer time
utc_now=dt.datetime.utcnow() #UTC datetime right now
time_difference = (here_now - utc_now)
print(here_now)
print(utc_now)
print(time_difference)

'''If you want to work directly with time zone names, you’ll need to import some 
date utilities from Python’s dateutils package. In particular, you need gettz
(short for get timezone) from the tz class of dateutil. So in your code, right after 
the line where you import datetime, use from dateutil.tz import gettz like 
this'''

#import datetime as dateutil tz
import datetime as dt
from dateutil.tz import gettz
# July 4 Event, 7:00 Local time (no specific time zone). 
event =dt.datetime (2020,7,4,19,0,0) 

#Show Local date and time 
print("Local: "+f"{event:%D %I:%M %p %Z}" + "\n")

event_eastern = event.astimezone (gettz ("America/New_York"))
print (f"{event_eastern:XD XIM Xp XZ}")

event_central = event.astimezone (gettz ("America/Chicago")) 
print(f"{event_central:XD XI: Xp X2}")

event_mountain = event.astimezone (gettz ("America/Denver"))
print (f" {event_mountain:%D %I:%M %p %Z}")

event_pacific = event.astimezone (gettz ("America/Los_Angeles")) 
print (f" {event_pacific: %D %I:%M Xp XZ}")

event_utc =event.astimezone (gettz ("Etc/UTC"))
print (f"{event_utc:XD XI:%M %p %Z}")

'''We didn’t say anything about time zone in the date time, so the time will automatically be for our time zone. That datetime is stored in the event variable.
The following line of code (after the comment, which starts with #) shows the date 
and time, again local, because we didn’t say anything about time zone. We added 
"Local:" to the start of the text, and added a line break at the end (\n) to visually 
separate that word from the rest of the output.'''