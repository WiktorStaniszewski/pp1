class C:
    def __init__(self, datadict):
        self.datadict = datadict
    def m1(self, s, n):
        if s not in self.datadict:
            self.datadict[s] = n        
        else:
            self.datadict[s] = n
    def m2(self, s):
        total = 0
        for i in s:
            for key,value in self.datadict.items():
                if key == i:
                    total += value
        return total  



if __name__ == "__main__":
    stadium = C({"A":120, "D":150,"G":90,"K":110})
    stadium.m1("G",130)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))