def is leapyear(year):
 if( year%4==0 and year%100!=0) or
     year%400==0:
     return true 
     else:
        return false 
      year = 2011
    if is leapyear(year):
       print("{} is a leapyear "format (year))
     else :
       print("{} is not a leapyear"formal (year)