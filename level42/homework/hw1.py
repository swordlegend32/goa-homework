def calculator(txt):
    Split = txt.split(" ")
    operators = {"+":int.__add__,"-":int.__sub__,"*":int.__mul__,"/":int.__truediv__,"//":int.__truediv__}
    return "." * operators[Split[1]](int(len(Split[0])), int(len(Split[2])))

