"""""
Code by: Charanpreet Singh
Email: Charanmakkar@gmail.com
Linkedin profile: https://www.linkedin.com/in/charanpreet-singh-a29949133/
DM linkedin if need any help (Always open to help)
Development date Nov 5, 2020
Final editing done on Dec 25, 2020
Github Upload: Dec 27, 2020
"""""

##Importing required libraries
import datetime

#Command to read LIVE Date and Time (It consists all values)
e = datetime.datetime.now()

"""
#In Numeric values
%Y = Year (Eg. 2020, 2021, ....)
%m = Month (Eg. 01, 02, 03, ....)
%d = Date (Eg. 01, 02, 03, 04, ....)


#12 Hr Clock
%I = Hours (Eg. 01, 02, .... , 12)
%M = Minutes (Eg. 00, 01, ..., 60)
%S = Seconds (Eg. 00, 01, ..., 60)
%p = AM , PM (Live)

#24 Hr Clock
%H = Hours (Eg. 00, 01, ..., 24)
%M = Minutes (Eg. 00, 01, ..., 60)
%S = Seconds (Eg. 00, 01, ..., 60)


#In Words
%a = Day (Eg. Sun, Mon, ...)
%b = Monthv(Eg. Jan, Feb, Mar, ...)
%p = AM , PM (Live)


#SEPERATORS
Seperators are of your choice
%Y-%m-%d = "-" is seperator
%H:%M:%S = ":" is seperator
"%d/%m/%Y" = "/" is seperator
"%a, %b %d, %Y" = ", " is seperator (a comma with a space)
"%a %b %d %Y" = " " is seperator (just a single space)
"""



####TIPS
#"N" = Numerical value (Eg. 1,2,3,4,5,6.....31)
#"W" = Alphabetic words (Eg. January, Feb....., // Monday, Tuesday, Wed .....)

#Different format for example that how can u print and use the values
print (e.strftime("%Y-%m-%d %H:%M:%S"))
print (e.strftime("%d/%m/%Y"))
print (e.strftime("%I:%M:%S %p"))
print (e.strftime("%a, %b %d, %Y"))
print("#" * 40)


"""
#Print and store values Seperatly
yearN = str(e.strftime("%Y"))
monthW = str(e.strftime("%b"))
dateN = str(int(e.strftime("%d"))-1)
monthN = str(e.strftime("%m"))

print(yearN)
print(monthN)
print(monthW)
print(dateN)
"""
