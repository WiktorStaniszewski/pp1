def hotel_list(hotels):
    hotel = ''
    count = 0
    for i in hotels:
        for key, value in i.items():
            if key == "name":
                if count == len(hotels)-1:
                    count += 1
                    hotel += value
                else:
                    count += 1
                    hotel += value + ", "
    return hotel                
            
    
def avg_price(hotels):
    hotels_price = 0
    avg_val = 0
    count = 0
    for i in hotels:
        for key, value in i.items():
            if key == "price":
                count += 1
                hotels_price += value
    avg_val = hotels_price/count
    return round(avg_val, 2)               
            
    
    
Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

Hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
one_hotel_price = avg_price(Hotels_in_Krakow)
sec_hotel_price = avg_price(Hotels_in_Sopot)
if sec_hotel_price > one_hotel_price:
    cheaper = "Krakow"
else:
    cheaper = "Sopot"


print(f"Hotels in Krakow: {hotel_list(Hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {avg_price(Hotels_in_Krakow)}")
print(f"Hotels in Sopot: {hotel_list(Hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {avg_price(Hotels_in_Sopot)}")
print(f"Cheaper hotels in: {cheaper}")
