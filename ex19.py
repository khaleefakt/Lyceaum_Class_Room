def bread_and_jams(bread_count, jam_boxes):
    print(f"you have {bread_count} breads and {jam_boxes} boxes of jams")
    print("Man thats enough for a party")
    print("get a blanket\n")

print("we can just give function value directly")
bread_and_jams(100,20)

print("or we can use variables from scripts")
no_of_breads = 100
no_of_jams = 20
bread_and_jams(no_of_breads, no_of_jams)

print("we can even do math inside too")
bread_and_jams(100+10, 20+2)

print("and we can combine to variable with math")
bread_and_jams(no_of_breads + 10, no_of_jams + 2)
