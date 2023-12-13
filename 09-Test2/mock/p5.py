def f(first_letter,last_letter):
    import re
    with open("data.txt", "r", encoding="UTF-8") as kfc:
        kfc_content = kfc.read()
        pattern = rf'\b{first_letter}[\w-]*{last_letter}\b'
        ass = re.findall(pattern, kfc_content, re.IGNORECASE)
    lenn = len(ass)
    return lenn
        
if __name__ == "__main__":
    print(f("w","d"))