# Time Display
# https://trinket.io/sense-hat

# imported for the time_display.py

# Color codes
# green = (0, 128, 0)
# lime = (0, 255, 0)
# yellow = (255, 255, 0)
# blue = (0, 0, 255)
# red = (255, 0, 0)
# white = (255,255,255)
# pink = (255,105, 180)
# aqua = (0, 255, 255)

highlight = (0, 255, 255)
digit = (255,255,255)
nothing = (0,0,0)

def blank():
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def m00():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m01():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m02():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m03():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m04():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m05():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m06():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m07():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m08():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m09():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m10():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m11():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m12():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m13():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m14():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m15():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m16():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m17():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m18():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m19():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m20():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, O, l,
    O, l, O, O, O, l, O, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m21():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m22():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, O,
    O, l, O, O, O, l, O, O,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m23():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m24():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m25():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m26():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m27():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m28():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m29():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m30():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m31():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m32():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m33():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m34():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m35():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m36():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m37():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m38():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m39():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m40():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m41():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m42():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m43():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m44():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m45():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m46():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m47():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m48():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def m49():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def m50():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m51():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m52():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m53():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m54():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, O, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m55():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m56():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m57():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def m58():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def m59():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, O, O, O, O, h, h, h,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

# Hour displays
def h00():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h01():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def h02():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, O, l, O, l, O, O,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h03():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h04():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def h05():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h06():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, O,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h07():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def h08():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h09():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, l, O, l, O, l, O, l,
    O, l, O, l, O, l, l, l,
    O, l, O, l, O, O, O, l,
    O, l, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def h10():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def h11():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def h12():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def h13():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def h14():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def h15():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def h16():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def h17():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def h18():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    ]
    return logo

def h19():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, O, O, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    ]
    return logo

def h20():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, l, O, l,
    O, l, l, l, O, l, O, l,
    O, l, O, O, O, l, O, l,
    O, l, O, O, O, l, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h21():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, O, O, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, O, O, l,
    ]
    return logo

def h22():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, l, O, O,
    O, l, O, O, O, l, O, O,
    O, l, l, l, O, l, l, l,
    ]
    return logo

def h23():
    l = digit
    h = highlight
    O = nothing
    logo = [
    O, h, h, h, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, l, l, l, O, l, l, l,
    O, O, O, l, O, O, O, l,
    O, l, l, l, O, l, l, l,
    O, l, O, O, O, O, O, l,
    O, l, O, O, O, O, O, l,
    O, l, l, l, O, l, l, l,
    ]
    return logo
