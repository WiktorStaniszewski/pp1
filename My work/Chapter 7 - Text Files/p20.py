with open("MeatAndFish.txt", 'w') as ff, open("GrainsAndBread.txt", 'w') as sf:
    ff.write("Skinless white meat\nTuna fish\nLuncheon meat\nLean cuts of red meat")
    sf.write("Bread\nRice\nAll purpose flour\nBreakfast cereal\nPasta")
with open("MeatAndFish.txt") as ff, open("GrainsAndBread.txt") as sf, open("allproducts.txt", 'w') as apf:
    file_f_contents = ff.read()
    file_s_contents = sf.read()
    apf.write(file_f_contents)
    apf.write(file_s_contents)
    
    
    
    
