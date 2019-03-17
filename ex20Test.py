current_line =0
    
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file= open("test.txt")

def printt():
    print("Lets print three lines ")
    current_line = 0
    current_line += 1
    print_a_line(current_line, current_file)

printt()
