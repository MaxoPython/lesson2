def str_comarisor (string1,string2):
   if type (string1)==type(string2):
            if string1==string2:
                return 1
            elif len(string1)>len(string2):
                return 2
            elif string1 != string2 and string2=="learn":
                return 3
            else:
                return "Нет такой комбинации"    
                      
   else:
        return 0

string1=input("Введите строку 1: ")
string2=input("Введите строку 2: ")

str_comarisor (string1,string2)
print (str_comarisor (string1,string2))