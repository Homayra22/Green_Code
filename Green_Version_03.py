import sys
import re
integer_list = []
text_list = []
total_list =[]
int1_list=[]
def remove(string):
    return "".join(string.split())
#file1 = open('test1.txt', 'r')
for line in sys.stdin:
 
  no_specials_string = re.sub('[!#?,.:";]', '', line)
  total_list.append(no_specials_string.rstrip())

for list in total_list:
     #list.split() 
     joint = "".join(list.split())
     joint=unicode(joint, 'utf-8')
     #print(joint)
     if(joint.isnumeric()):
         
         int1_list.append(list.split())
     else:
         #list.replace('       ',"")
         text_list.append(list)

Test_case = len(int1_list)


total_test_case = int1_list[0]
line_no=[]
#line_i=1
test_cases = {}
lower_limit=0
for i in range(1,len(int1_list)):
  
  line_no.append(int(int1_list[i][0]))
  upper_limit = lower_limit + int(int1_list[i][0])
  test_cases[i] = text_list[lower_limit:upper_limit]
  lower_limit = upper_limit


test_case_assoicated_line_numbers = line_no
# Put the test case line number & associated lines in a dictionary.
#test_cases = {}
#lower_limit=0
#for i, j in enumerate(line_no):
    #upper_limit = lower_limit + j
    #test_cases[i] = text_list[lower_limit:upper_limit]
    #lower_limit = upper_limit
#print(test_cases)  

#from typing import Dict
import itertools
def Convert(f):
  
    s= sorted(f.items(), key=lambda kv: kv[::-1], reverse=True)
    
    result = []
    for k, v in itertools.groupby(s, lambda item: item[1]):
        result.extend(sorted(v))
    return result
#out_file = open("out.txt", "w")

line_i=1
for i in range(1,len(test_cases)+1):
  x=test_cases[i]
  x = ' '.join(map(str, x))
  lines= x.strip()
  words = x.split(" ")
  #print(words)
  d={}
  for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
  
  #print(f"\n Test Case #{i+1}\n")
  print'\nTestcase# %s' % (i)
  #out_file.write(f"\n Test Case #{i+1}\n")
# Print the contents of dictionary
  #for key in list(d.keys()):
    #print(key, ":", d[key])
  sorted_age = Convert(d)
 
  #print(Convert(sorted_age))
  
  #result = []
  #for k,v in itertools.groupby(sorted_age, lambda item: item[1]):
    #result.extend(sorted(v))
  #print(result)

  len_result=len(sorted_age)
  for i in sorted_age:
      if i[0] == '':
          sorted_age.remove(i)
 
  for i in range(int(int1_list[line_i][1])-1,int(int1_list[line_i][2])):
      #print(int(int1_list[line_i][1]) - 1)
      #print(int(int1_list[line_i][2]))
      #print(f"{result[i][0]} :{result[i][1]}")
      print'%s:%s' % (sorted_age[i][0], sorted_age[i][1])
  line_i= line_i+1
#result










