def song(n) :
    if n == 1 :
        obj_1 = "bottle"
    else :
        obj_1 = "bottles"
    if n == 2 :
        obj_2 = "bottle"
    else :
        obj_2 = "bottles"

    print(str(n) + " " + obj_1 + " of beer on the wall, " + str(n) + " " + obj_1 + " of beer.")
    print("Take one down and pass it around, " + str(n-1) + " " + obj_2 +" of beer on the wall.")
#print("Sample")
bottles = 99
while bottles > 0 :
    song(bottles)
    bottles -= 1
