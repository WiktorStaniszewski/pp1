def f(mnumbers):
    import re
    correct = 0
    for i in mnumbers:
        pattern = rf"[+-]*[a-dA-D1-7]+$"
        nice = re.findall(pattern, i)
        for n in nice:
            if len(n) == len(i):
                correct+=1
            
    return correct
    
print(f(["A15",
         "-31",
         "7abC",
         "+D1",
         "-gH"]))
print(f(["A05",
         "-3+1",
         "7ab8C",
         "+D1",
         "-22k"]))