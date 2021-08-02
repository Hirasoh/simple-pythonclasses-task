###Given a string, we'll say that the front is the first 
# 3 chars of the string. If the string length is less than 
# 3, the front is whatever is there. Return a new string which is 3 copies of the front.###########



def front3(a):
      front=len(a)
      z=''
      if front>3:
        for i in range(3):
            z+=a[:3]
        return z
      else:
        return a+a+a


print(front3("java"))
print(front3("Chocolate"))
print(front3("abc"))



#with the help of classes
class front:
    def front3(self,a):
      front=len(a)
      z=''
      if front>3:
        for i in range(3):
            z+=a[:3]
        return z
      else:
        return a+a+a
z=front()  
print(z.front3("java"))
print(z.front3("Chocolate"))
print(z.front3("abc"))






#part2

####Given a string, return a new string where the first 
# and last chars have been exchanged.###3.......


class front_back:
    def front2(self,str):
         if len(str) <= 1:
          return str
  
         mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
         # last + mid + first
         return str[len(str)-1] + mid + str[0]
  

z=front_back()
print(z.front2("code"))
print(z.front2("a"))
print(z.front2("ab"))




#part3


# a new string where the char at index n has been removed. The value
#  of n will be a valid index of a char in the original 
# string (i.e. n will be in the range 0..len(str)-1 inclusive).



class remove_specific():
   def missing_char(self,str, n):
    z=str[n]
    if z in str:
        k= str.replace(z,"")
        return k


j=remove_specific()
print(j.missing_char("kitten",4))
print(j.missing_char("kitten",0))
print(j.missing_char("kitten",1))



#part4


#Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the 
# string unchanged.
class no: 
 def not_string(self,str):
  if str=="not":
    return str
  else:
    return "not "+ str

z=no()
print(z.not_string("bad"))
print(z.not_string("x"))
print(z.not_string("canady"))


#####Given 2 int values, return True if one is negative and one is positive.
#  Except if the parameter "negative" is True, then return True
#  only if both are negative.

class boolen:
  def pos_negation(self,a,b,c):
    if c=="True":
      return (a < 0 and b < 0)
    else:
     return ((a < 0 and b > 0) or (a > 0 and b < 0))

z=boolen()
print(z.pos_negation(1,-1,"False"))
print(z.pos_negation(-1,1,"False"))
print(z.pos_negation(-4,-5,"True"))


###Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes
#  the absolute value of a number.means ky when you take a number then it's difference is less than 10
# or it's equal to 10

class near:
  def near_hundred(self,n):
    
   return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


z=near()
print(z.near_hundred(93))
print(z.near_hundred(100))
print(z.near_hundred(89))
print(z.near_hundred(121))



#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

class makesten():
  def make10(self,a,b):
   if a+b==10 or a==10 or b==10:
     return True
   else:
     return False



z=makesten()
print(z.make10(1,9))
print(z.make10(9,10))
print(z.make10(9,9))




####We have a loud talking parrot. The "hour" parameter is the current hour time in the range 
# 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return
#  True if we are in trouble.

class talking:
  def parrot_trouble(self,a, b):
      return (a and (b < 7 or b > 20))


z=talking()
print(z.parrot_trouble(True,6))
print(z.parrot_trouble(True,7))
print(z.parrot_trouble(False,6))


####Given an int n, return the absolute difference between n and 21, except
#  return double the absolute difference if n
#  is over 21.

class difference:
  def diff21(self,a):
    if a<=21:
      return abs(a-21)
    else:
      return abs(a-21)*2


z=difference()
print(z.diff21(19))
print(z.diff21(10))
print(z.diff21(21))

###Given two int values, return their sum. Unless the two values are the same, then return double their sum.

class summation:
  def summ(self,a,b):
    if a==b:
      return (a+b)*2
    else:
      return a+b


z=summation()
print(z.summ(1,2))
print(z.summ(3,5))
print(z.summ(2,2))


##We have two monkeys, a and b, and the parameters a_smile and b_smile
#  indicate if each is smiling. We are in trouble if they are both smiling or
#  if neither of them is smiling. Return True if we are in trouble.

class boolen2:
  def monkey_trouble(self,a_smile, b_smile):
    if a_smile and b_smile:
     return True
    if not a_smile and not b_smile:
     return True
    return False   

z=boolen2()
print(z.monkey_trouble(True,True))
print(z.monkey_trouble(False,False))
print(z.monkey_trouble(True,False))


###The parameter weekday is True if it is a weekday,
#  and the parameter vacation is True if we are on vacation. We sleep 
# in if it is not a weekday or we're on vacation. Return True if we sleep in.

class boolen3:
  def sleep_in(self,a,b):
    return (not a or b)
z=boolen3()
print(z.sleep_in(True,True))
print(z.sleep_in(False,True))
print(z.sleep_in(True,False))




