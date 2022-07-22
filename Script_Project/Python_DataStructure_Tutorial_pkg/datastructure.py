
def use_set_dt_struc():
    set1 = set([
        1,2,4,6])
    set2=set([1,3,5,7])
    intersection =set1 & set2
    print("using SET to do interesection")
    print (intersection)

def use_dic_dt_struc():
    ages=dict()
    ages["bob"]=22
    ages["emily"]=21
    print("using DIC to map key & value")
    for key,value in ages.items():
        print(key,value)