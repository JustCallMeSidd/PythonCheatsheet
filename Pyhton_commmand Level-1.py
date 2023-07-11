#SOME PYTHON FUNCTION FOR NUMBER 
pi=3.14159265358979
x=128
y=-345.67890987
z=-999.9999
print(abs(z)) #RETURN ABSOLUTE VALUE (- TO + AND + TO +)
print(int(z)) #RETURN VALUE TO INT VALUE ( 4.34 TO 4 )
print(round(pi,4)) #RETURN VALUE TO ROUND OF 4TH VALUE
print(bin(x)) #RETURN VALUE TO BINARY FORM (3.1416 TO 0b10000000)
print(hex(x)) #RETURN VALUE TO HEXA DECIMAL VALUE
print(oct(x)) #RETURN VALUE TO OCTAL DECIAML VALUE
print (max(pi,x,y,z)) #RETURN VALUE OF MAX OF ANY 4 OF VARIABLE
print(min(pi,x,y,z)) #RETURN VALUE OF MIN OF ANY 4 OF VARIABLE
print(type(pi)) #RETURN VALUE TYPE 
print(type(x)) #RETURN VALUE TYPE 
print(type(str(y))) #RETURN VALUE TYPE 

print("------------------------------------------------------------------------------------------------------------------------")

#F-STRING FORMMATING
name="sidd"
print(f"name-: {name}")
price=44
Qnt=34
print(f"subtotal: ${price * Qnt}")
print(f"subtotal: ${price * Qnt:,}") #put colon after thousand 
print(f"subtotal: ${price * Qnt:,.2f}") #put colo after thousand and 2 decimal place
saletax=0.024
print(f"Sale tax rate: ${saletax:.2%}") #If you want to format the number 0.065 as a percentage with 2 decimal places, you can use the following code: "{:.2%}".format(0.065). This will return the string '6.50%'.
print(f"Sale tax rate: ${saletax:.5%}")

print("------------------------------------------------------------------------------------------------------------------------")

#SOME PYTHON MATH MODULE
import math
pi =math.pi
e= math.e
tau = math.tau
X = 81
y = 7
Z=-23234.5454
p=0.1
print(pi) #RETURN VALE OF pi  CONSTANT(3.17) WE DON'T NEED TO DO ( math.PI ) as it written above line 24
print(e) #RETURN VALE OF e CONSTANT(2.71 ) WE DON'T NEED TO DO ( math.e ) as it written above line 25
print(tau) #RETURN VALE OF TAU CONSTANT(6.2831) WE DON'T NEED TO DO ( math.tau ) as it written above line 26
print(math.sqrt(x)) #RETURN VALUE ( math.sqrt )  is a method that returns the square root of a number
print(math.factorial(y)) #RETURN FACTORIAL OF Y (factorial = n!)
print(math.floor(z)) #RETURN  Math.floor() method rounds a number DOWN to the nearest integer. (4.124 = 4 , -23.23 = -23 , 0.60 = 0 , -5.2 = -6)
print(math.ceil(x)) #The Math.ceil() method rounds a number rounded UP to the nearest integer. (0.60 = 1 , 0.30 = 1 , -5.1 = -5 , 5.1 = 6)
print(math.degrees (y)) #Return angle y from radian to degrees.
print(math.radians (y)) #Return angle y from degrees to radian.
print(math.acos(p)) #Return arc cosine of x in radian range is [-1,1]
print(math.atan(x)) #Return arc tangent of x in radian
print(math.atan2(y,x)) #Return arc tangent of (y/x) in radian
print(math.sin(x)) #return the sine of x radian 
print(math.tan(x)) #return the tangent of x radian 
print(math.cos(x)) #Return the cos of x radian
print(math.exp(x)) #Return e raised to the power of x , where e is base of natural log
print(math.isnan(x)) #Return value true is x not numebr otherwise false
print(math.pow(x,y)) #Reurn vlaue of x power to y
print(math.log(x,y)) #Return the natural logarithm of x to base y.
print(math.log2(x)) #Return the base-2 log of x

print("------------------------------------------------------------------------------------------------------------------------")

#MAKING MULTIPLE FORMAT STRING
a="a"
b="b"
c="c"
d="d"
out=f"{a} \n{b} \n{c} \n{d}"
print(out)

a=566
b=54
c=78
d=562
out=f"${a:>2,.2f} \n${b:>6,.2f} \n${c:>7,.2f} \n${d:>9,.2f}" # ( :>2 ) it cotrol width of output
print(out)
print("\n")
#Make doolar sighn with width control
fi="$"+f"{a:.2f}"
se="$"+f"{b:.9f}"
print(f"{se:>2}")
print(f"{fi:>9}")

print("------------------------------------------------------------------------------------------------------------------------")

#Grappling with weirder number
#Complex Number complex(real,imaginary)
z=complex(3,-3)
print(z) 
print(z.imag)
print(z.real)

print("------------------------------------------------------------------------------------------------------------------------")

#Manupulation of String
#concatination of String
a="hi"
b=" i am "
c="Akira"
print(a+b+c)

print("sry"+" "+"hi") # ( " " ) #in python u need ot space if u forget there will be no space like in below example
print("sry"+""+"hi") # ( "" )

#length of string
out1=""
out2=" "
out3="hi"
print(len(out1))
print(len(out2))
print(len(out3))

s="Abracadabra Hocus Pocus you're a turtle dove"
# Is there a Lowercase letter t is contained in s?
print("t" in s)
#Is there an uppercase letter t is contained in s?
print("T" in s)
#Is there no uppercase T in s?S
print("T" not in s) 
#Print 15 hyphens in a row
print("-"*15)
#Print first character in string X
print(s[0])
# Print characters 33 - 39 from string x
print(s[33:39]) 
#Print every third character in s starting at zero
print(s[0:44:3])
#Print Lowest character is s (a space is lower than the letter a)
print(min(s))
#Print the highest character is s
print(max(s)) 
#Where is the first uppercase P?
print(s.index("P"))
#Where is the first Lowercase 0 in the latter half of string s 
#Note that the returned value still starts counting from zero 
print (s.index("o",22,44))
#How many Lowercase letters a are in string s? 
print(s.count("a"))

#ASCII stands for American Standard Code for Information Interchange. 
# It is a 7-bit character code where each individual bit represents a unique character.]
""""Below are the ASCII values of printable characters (33, 126):,
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
"""""
print("------------------------------------------------------------------------------------------------------------------------")

#Build in maethod for string
#learn for methos string from wbsite ( https://www.w3schools.com/python/python_ref_string.asp  )
s1 = "There is no such word as schmeedledorp"
s2=" a b c "
s3="ABC"
s4="54.75"
#Captiolize first letter, the rest Lowercase 
print(s3.capitalize())
#Count the number of spaces in sl 
print(s1.count(" "))
# Find the dot in $4 
print(s4.find("."))
# Is s2 all Lowercase letters?
print(s2.islower())
# Convert 53 to all lowercase 
print(s3.lower())
# String Leading characters from $2
print(s2.lstrip())
# String Leading and trailing characters from $2
print(s2.strip())
# Swap the case of letters in si 
print(s1.swapcase())
# Show si in title case (initial caps)
print(s1.title())
# Show s1 uppercase
print(s1.upper())

print("------------------------------------------------------------------------------------------------------------------------")

#Uncovering Dates and time

import datetime as dt
today=dt.date.today()
lastData=dt.date(2002, 5 , 19)
timedelt=dt.timedelta(days=12)
diffdate=today-lastData 
diffdate1=today+timedelt #time delt is a time span u want to add or sub
diffdate2=today-timedelt
duration=dt.datetime(2019 ,3,31 ,8 ,0,0)
duration1=dt.datetime(2019 ,3,31 ,5 ,0,0)
# duraadd=duration+duration1 #TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'datetime.datetime' we can't perform + operation on datetime.datetime and another datetime.datetime

durasub=duration-duration1
print(today)
print(lastData)
print(diffdate)# type "datetime.timedelt"
print(diffdate1)
print(diffdate2)
#print(duraadd)
print(durasub)

print("------------------------------------------------------------------------------------------------------------------------")


print(f"{today:%a,%A,%w,%d,%b,%B,%m,%y,%Y,%H,%I,%p,%M,%S,%f,%z,%Z,%j,%U,%W,%c,%x,%X,%%}")

"""""
A reference of all the legal format codes:


%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01

#simple date format string

1st -----

%a, %b %d %Y         |     Sat, Jun 01 2019
%X   | 06/01/19
%m-%d-%y  |  06-01-19
This %A %B %d   |  This Saturday June 01
%A %B %d is day boss number %j of %Y | Saturday June 01 is day number 152 of 2019

2nd -----------

%I:%M %p         |   11:59 PM
%H:%M:%S and %f microseconds    | 23:59:59 and 999999 microseconds
%X   | 23:59:59

3rd -----------

%A, %B %d at %I:%M%p  | Tuesday, December 31 at 11:59PM
%m/%d/%y at %H:%M%p  |   12/31/19 at 23:59
%I:%M %p  on %b %d |     11:59 PM on Dec 31
%X  | 12/31/19
%C  | Tue Dec 31 23:59:00 2019
%m/%d/%y at %I:%M %p |  12/31/19 at 11:59 PM
%I:%M %p on %m/%d/%y  |   1:59 PM on 12/31/2019 


"""

print("------------------------------------------------------------------------------------------------------------------------")

#Accounting for time zone

import datetime as dt 
utc_now=dt.datetime.utcnow()
now_here=dt.datetime.now()
diff=now_here-utc_now
DIFF=utc_now-now_here
print(diff)
print(DIFF)# misliding difference time
print(now_here)
print(utc_now)

"""
How to get the current time ?
In order to get the local time, we can use the time module. Some important functions of the time module

localtime() – it helps to get the current local time
strftime(“%H:%M:%S”, t) – it helps to decide the format of the time to be used to display the time
How to get current time in different zones ?
In order to get the current time of a particular timezone there is a need to use the pytz Python library. Some of the important commands of pytz library are

utc – it helps to get the standard UTC time zone
timezone() – it helps to get the time zone of a particular location
now() – it helps to get the date, time, utc standard in default format
astimezone() – it helps to convert the time of a particular time zone into another time zone

"""
print("------------------------------------------------------------------------------------------------------------------------")


# import datetime, give it an alias
import datetime as dt
 # import timezone helpers from dateutil 
from dateutil.tz import gettz
# UTC time right now.
utc=dt.datetime.now(gettz('Etc/UTC'))
print(f" {utc: %A %D %I:%M %p %Z}")

# USA Eastern time.
est = dt.datetime.now(gettz ('America/New_York'))
print (f" {est:%A %D %I:%M %p %Z}")
# USA Central time
cst=dt.datetime.now(gettz ('America/Chicago'))
print (f"{cst: %A %D %I:%M %p %Z}")

# USA Mountain time
mst=dt.datetime.now(gettz ('America/Boise')) 
print (f"{mst:%A %D %I:%M %p %Z}")

pst=dt.datetime.now(gettz('America/Los_Angeles')) 
print (f" {pst: %A %D %I:%M %p %Z}")

"""If you want to work directly with time zone names, you'll need to import some dateutils. 
In particular, you need gettz (short for get timezone) from the tz class of dateutil. So in your code,
 right after the line where you import datetime, use from dateutil.tz import gettz like this:"""


"""Afterwards, you can use gettz ('name') to get time zone information for any time zone. 
Replace name with the name of the time zone from the Olson database. 
For example, America/New_York for USA Eastern Time, or Etc_UTC for UTC Time.

shows an example where we get the current date and time using datetime.now() 
with five different time zones - UTC and four USA time zones."""

