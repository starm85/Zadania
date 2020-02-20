a=["A123AA11", "A222AA123", "A12AA123", "A123CC1234", "AA123A12","FE5557ACCE","E748BC","A157AE155"] # Регистрационные номера
x=set("ABEKMHOPCTYX") # Все разрешенные буквы в регистрационном номере 
result=[]
for element in a:
    if len(element)==8:   
        if element[0] in x:
            if (element[1].isdigit):
                if (element[2].isdigit):
                    if (element[3].isdigit):    
                        if element[4] in x:
                            if element[5] in x:
                                if (element[6].isdigit):
                                    if (element[7].isdigit):
                                        result.append(element)    
    elif len(element)==9:
        if element[0] in x:
            if (element[1].isdigit):
                if (element[2].isdigit):
                    if (element[3].isdigit):    
                        if element[4] in x:
                            if element[5] in x:
                                if (element[6].isdigit):
                                    if (element[7].isdigit):
                                        if (element[8].isdigit):
                                            result.append(element)
print(result)