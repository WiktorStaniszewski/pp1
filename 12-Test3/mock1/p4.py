def f(fnc,prods):
    result = list(map(fnc, prods))
    final = ','.join(result)
    return final
    
    
if __name__ == "__main__":    
    prods = ["water","cheese","tomato"] 
    fnc1 = lambda x: "id:"+x[:2] 
    fnc2 = lambda x: (x[0]+x[-1]).upper() 
    print(f(fnc1,prods))
    print(f(fnc2,prods))