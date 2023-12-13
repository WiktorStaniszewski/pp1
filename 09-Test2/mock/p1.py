def f(player1, player2):
    sump1 = 0
    sump2 = 0
    for i in player1:
        if i == 'A' or i == 'K' or i == 'Q' or i == 'J' or i == 'T':
            sump1 += 10
        else:
            sump1 += int(i)
    for i in player2:
        if i == 'A' or i == 'K' or i == 'Q' or i == 'J' or i == 'T':
                sump2 += 10
        else:
            sump2 += int(i)
    return sump1 >= sump2

if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))