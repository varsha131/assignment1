Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #print all the numbers from 0 to 6 except 3 and 6
for x in range(6):
                  if(x==3 or x==6):
                          continue
                  print(x,end=' ')
print("\n")