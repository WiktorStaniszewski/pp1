def f(years, course):
    import json
    count = 0
    with open("data.json",'r') as kfc:
        kfc_con = json.load(kfc)
        for row in kfc_con:
            if row['age'] >= years:
                sum = 0
                for i in row["studies"]['courses']:
                    if i['name'] == course:
                        for n in i["grades"]:
                            sum += n
                if sum/len(i["grades"]) >= 4:
                    count+=1
    return count
                        
if __name__ == "__main__":        
    print(f(21, "statistics"))
                