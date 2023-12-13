def f(arr):
    correct_password = 0
    count = 0
    has_num = 0
    has_under = 0
    has_lower = 0
    for password in list(arr):
        for letters in password:
            if 4 <= len(password) <= 12:
                if letters.islower():
                    count += 1
                    has_lower+=1
                elif letters.isnumeric():
                    count+=1
                    has_num+=1
                elif letters == "_":
                    count +=1
                    has_under+=1             
            else:
                continue
        if count == len(password) and has_num and has_under and has_lower:
            correct_password+=1
        count = 0
        has_lower = 0
        has_under = 0
        has_num = 0
    return correct_password
            
if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f","water7x"]))
    
def f2(arr):
    import re
    