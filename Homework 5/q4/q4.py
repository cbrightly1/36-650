# q4

def triangle(rows):
    if rows < 0 or type(rows) != int:
        print("Invalid Input")
        return
    num_count = 1
    row_num = 1
    while row_num <= rows:
        print(*(range(num_count, num_count + row_num)))
        num_count += row_num
        row_num +=1
    
triangle(6)
triangle(-1)
triangle(1.5)
triangle(3)