def odd_one(L):
    type_count = {}
    
    for item in L:
        t = type(item)
        type_count[t] = type_count.get(t,0) + 1
        
    for t, count in type_count.items():
        if count == 1:
            if t == int:
                return "int"
            if t == float:
                return "float"
            if t == str:
                return "str"
            if t == bool:
                return "bool"
            