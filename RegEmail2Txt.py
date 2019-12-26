# coding:utf-8
import  re,sys
 
MailFile = open(sys.argv[1], 'r')
strings=MailFile.read()
MailFile.close()
matches = []
 
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)
for groups in emailRegex.findall(strings):
    matches.append(groups[0])
 
NewFile = open(sys.argv[2],'a')
 
list2 = list(set(matches))
# print(list2)
list_nums = len(list2)

for line in range(list_nums):
 
    NewFile.writelines(list2[line]+"\n")
NewFile.close()

print("\nSuccess\n")
