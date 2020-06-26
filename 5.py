Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #print a string from two given string
def char(a,b):
               new_a= b[:2] + a[2:]
               new_b= a[:2] + b[2:]
               return new_a + ' ' + new_b
print(char('abc', 'xyz'))