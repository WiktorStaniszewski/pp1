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

def f(text, dict):
    word = ''
    for i in text:
        i = str(i).lower()
        for key, value in dict.items():
            if key == i:
                word+=f'{value} '
    return word

print(f("UEK",ICAO_dictionary))
        