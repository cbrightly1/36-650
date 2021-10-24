# q5

def triangle_stars(rows):
    for i in range(0,rows):
        for j in range(0,rows-i-1): # the amount of whitespace before *
            print(end=" ") # end makes the spaces on the same line, prints whitespace before *
        for j in range(0,i+1): # the number of starts (related to row numbers)
            print("*", end = " ")
        print()
triangle_stars(3)
triangle_stars(5)