arr =  [[-38, 19], [5,40],[-7,11],[29,-70]]
def max(array):
    which_sublist = 0   #numer podlisty arr                         (arr - var)
    current_number = 0  #jest to numer aktualnej liczby w subarr    (subarr - var)
    overall_number = 0  #ile generalnie jest liczb w arrayu         (arr-subarr - var)
    save_number = 0     #jaki numer ma byc zachowany                (subarr - const)
    save_row = ""       #zachowuje numer listy w głównym arrayu     (subarr - const)
    save_column = ""    #zachowuje liczbe w sublist                 (subarr - cosnt)
    for sublist in list(array):
        #dla kazdego sublista w liscie:                                   
        for i in sublist:              
            #dla kazdej liczby w subliscie:                                                      
            if overall_number == 0:                             
                save_number = i                                 
                save_row = f"{which_sublist}"                   
                save_column = f"{current_number}"
                overall_number+=1
                current_number+=1
            else:
                if i > save_number:
                    save_number = i
                    save_row = f"{which_sublist}"
                    save_column = f"{current_number}"
                    overall_number+=1
                    current_number+=1
                else:
                    overall_number+=1
                    current_number+=1
        current_number=0
        which_sublist +=1
    return save_number, save_column, save_row

def min(array):
    which_sublist = 0   #numer podlisty arr                         (arr - var)
    current_number = 0  #jest to numer aktualnej liczby w subarr    (subarr - var)
    overall_number = 0  #ile generalnie jest liczb w arrayu         (arr-subarr - var)
    save_number = 0     #jaki numer ma byc zachowany                (subarr - const)
    save_row = ""       #zachowuje numer listy w głównym arrayu     (subarr - const)
    save_column = ""    #zachowuje liczbe w sublist                 (subarr - cosnt)
    for sublist in list(array):
        #dla kazdego sublista w liscie:                                   
        for i in sublist:              
            #dla kazdej liczby w subliscie:                                                     
            if overall_number == 0:                             
                save_number = i                                 
                save_row = f"{which_sublist}"                   
                save_column = f"{current_number}"
                overall_number+=1
                current_number+=1
            else:
                if i < save_number:
                    save_number = i
                    save_row = f"{which_sublist}"
                    save_column = f"{current_number}"
                    overall_number+=1
                    current_number+=1
                else:
                    overall_number+=1
                    current_number+=1
        current_number=0
        which_sublist +=1
    return (save_number, save_column, save_row)



print(max(arr))
print(min(arr))