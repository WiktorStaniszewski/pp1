winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}
totalhours = 0
for key, value in winter_semester.items():
    print(f"{key:<12} : {value:<4}")
    totalhours += value
print(f"Total hours  : {totalhours:<4}")