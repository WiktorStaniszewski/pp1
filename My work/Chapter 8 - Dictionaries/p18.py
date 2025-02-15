ICAO_dictionary = {
    'a':"Alfa", 
    'b':"Bravo", 
    'c':"Charlie", 
    'd':"Delta", 
    'e':"Echo", 
    'f':"Foxtrot", 
    'g':"Golf", 
    'h':"Hotel", 
    'i':"India", 
    'j':"Juliett",
    'k':"Kilo", 
    'l':"Lima", 
    'm':"Mike", 
    'n':"November", 
    'o':"Oscar", 
    'p':"Papa", 
    'q':"Quebec", 
    'r':"Romeo", 
    's':'Sierra', 
    't':"Tango", 
    'u':'Uniform', 
    'v':'Victor',
    'w':'Whiskey', 
    'x':'X-ray', 
    'y':'Yankee', 
    'z':'Zulu'
}

with open("ICAO.txt", 'w') as kfc:
    for key,value in ICAO_dictionary.items():
        kfc.write(f"{key} {value}\n")