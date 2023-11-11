def f(bc):
    if len(str(bc)) != 13:
        return False
    elif len(str(bc)) == 13:
        if str(bc)[0:3] == "590":
            return True
        else:
            return False
