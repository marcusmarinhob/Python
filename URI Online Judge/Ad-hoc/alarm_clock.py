# URI ONLINE JUDGE ##############################################
# PROBLEM: 1103 - Alarm Clock
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################


while True:
   H1, M1, H2, M2 = input().split()
   if (H1 == '0' and M1 == '0' and H2 == '0' and M2 == '0'):
    break

   h1 = int(H1)
   m1 = int(M1)
   h2 = int(H2)
   m2 = int(M2)
   
   t1 = (h1 * 60) + m1
   t2 = (h2 * 60) + m2

   if t1 < t2:
     output = t2-t1
   else:
     output = 1440+(t2-t1) #24*60 = 1440
    
   print(output)
    
    