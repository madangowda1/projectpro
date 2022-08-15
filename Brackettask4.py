def paraCheck( seq ):  
   res=seq
   m=''
   for i in seq:
       if i in '{[(}])':
           m=m+i
           #print(m)        
           
   while True:  
       if '()' in m :  
           m = m.replace ( '()' , '' )  
       elif '{}' in m :  
           m = m.replace ( '{}' , '' )  
       elif '[]' in m :  
           m = m.replace ( '[]' , '' )  
       else: 
           
           if len(m)==0:
               return "Valid Expression"
           else:
               print(res.rfind(m))
               return "InValid Expression"
   
  

seq=input("enter string")
print(paraCheck(seq))


   
  