def f(d):
    cin = d.count("+")
    cout = d.count("-")
    return cin-cout



if __name__ == "__main__":
    print(f(""))
    print(f("+-+"))
    print(f("+-+++-+---"))
    print(f("+-+++++-"))