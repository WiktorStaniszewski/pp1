movie_titles = ["Harry Potter", "Green Mile", "Forrest Gump", "Cast Away", "The Office"]
file = open("movies.txt", 'w')
word = ""
count = 0
for i in movie_titles:
    count +=1
    if count == len(movie_titles):
        file.write(i)
    else:
        file.write(i + "\n")
file.close()
file = open("movies.txt", 'r')
file_content = file.read()
print(file_content)
file.close()