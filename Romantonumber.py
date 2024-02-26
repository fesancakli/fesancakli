"""I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.1"""
def Romantonumber(roman):
      result=0
      roman_list = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
      for i in range(len(roman)):
            if i<len(roman)-1 and roman_list[roman[i]]<roman_list[roman[i+1]]:
                  result+= -roman_list[roman[i]]
            else:
                  result+=roman_list[roman[i]]
      return  result

print(Romantonumber("CMM"))
