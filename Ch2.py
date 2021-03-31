#string creation

stri='Hello "python" world' #if you want specify with hifens inside the statement which u are printing
long_string='''By giving three hifens, we can able to type
more than one line'''
print(stri)

# There is also a method to convert any type of variable into string i.e, "str"--> Method name
#Example
mynum=123
print(mynum)
mystr=str(mynum)
print(mystr,'--> This is considered as a string not int')
print(type(mystr))#By this, It is verified that method 'str' converted int to string.

#String Concatenation

# '+' oprend can add two string.
#Example

Yu='Hi'
uy='London'
ty=Yu+' '+ uy
print(ty)

# String Methods.

# We have some methods which can be used for string. For example we do the in upper case letter etc.,

print(stri.upper()) #--> 'upper()' is a method will returns string in upper case.
print(stri.lower()) #--> 'lower()' is a method will returns string in lower case.
sty='  hello world fy  ds'
print(sty.strip()) #--> 'strip()' It will remove one white space between words.
print(len(ty)) #--> 'len()' gives us the length of the string
print(format(ty))

#String Slicing

name='Sai Pranav'
print(name[0:5]) #--> This will be getting the values by reffering the index starts from 0
print(name[2:]) # --> Here we are starting to print the value from index 2.

