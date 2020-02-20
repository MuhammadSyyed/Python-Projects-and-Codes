def tan(angle):
    if angle==90 or angle==270 or angle==450:
        return 'Math error'
    x=sin(angle)/cos(angle)
    return(x)
def sin(angle):
    while True:
        a=1
        if angle>360:
            angle=angle-360
            continue
        elif 90<angle<181: 
            angle=180-angle
            continue
        elif 180<angle<271:
            angle=angle-180
            a=-1
            angle=90-angle
            angle=angle*0.01745329252
            y=1-angle**2/2+angle**4/24
            return (y*a)
            continue
        elif 270<angle<361:
            angle=360-angle
            a=-1
            angle=90-angle
            angle=angle*0.01745329252
            y=1-angle**2/2+angle**4/24
            return y*a
            continue
        elif angle==0:
            return 0
        angle=90-angle
        angle=angle*0.01745329252
        y=1-angle**2/2+angle**4/24
        return y*a
 
def cos(angle):
    while True:
        a=1
        if angle>360:
            angle=angle-360
            continue
        if 90<angle<181: 
            angle=180-angle
            a=-1
            angle=angle*0.01745329252
            y=1-angle**2/2+angle**4/24
            return y*a
        elif 180<angle<271:
            angle=angle-180
            a=-1
            angle=angle*0.01745329252
            y=1-angle**2/2+angle**4/24
            return y*a
        elif 270<angle<361:
            angle=360-angle
        angle=angle*0.01745329252
        y=1-angle**2/2+angle**4/24
        return y*a

        
