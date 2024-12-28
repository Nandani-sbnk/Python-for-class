def pour_water(juga,jugb):
    max1,max2,fill=5,7,4
    print("%d %d"%(juga,jugb))
    if jugb==fill:
        return
    elif jugb==max2:
        pour_water(0,juga)
    elif juga!=0 and jugb==0:
        pour_water(0,juga)
    elif juga==fill:
        pour_water(juga,0)
    elif juga<max1:
        pour_water(max1,jugb)
    elif juga<(max2 -jugb):
        pour_water(0,(juga+jugb))
    else:
        pour_water(juga-(max2-jugb),(max2-jugb)+jugb)

print("JUGA JUGB")
pour_water(0,0)                        
    