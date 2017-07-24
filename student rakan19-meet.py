Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b=
SyntaxError: invalid syntax
>>> b
10
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
10
>>> four='4'
>>> print(four*4)
4444
>>> print(four*3)
444
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> my_name='student'
>>> print("hi,"+myname')
      
SyntaxError: EOL while scanning string literal
>>> print("hi,"+my_name)
hi,student
>>> my_age=15
>>> print('Iam'+my_age+'yearsold')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print('Iam'+my_age+'yearsold')
TypeError: Can't convert 'int' object to str implicitly
>>> print('iam'+15+'yearsold')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print('iam'+15+'yearsold')
TypeError: Can't convert 'int' object to str implicitly
>>> ('iam'+'15'+'yearsold')
'iam15yearsold'
>>> score=1
>>> total=score+(count*2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    total=score+(count*2)
NameError: name 'count' is not defined
>>> print (total)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print (total)
NameError: name 'total' is not defined
>>> count=11
>>> total=23
>>> total=score+(count*2)
>>> 
>>> print(total)
23
>>> 
==== RESTART: /home/student/rakan19_lab2/meet2017y1lab2/squareinTurtle.py ====
