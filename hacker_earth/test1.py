
numbers_shown = input()

space_sep_ints = input()

space_sep_ints_max = len(space_sep_ints)

number_to_count_map = {}

for i in space_sep_ints:
    if i.isdigit() :
        number = int(i)
        if number in number_to_count_map :
            number_to_count_map[number] = number_to_count_map[number] + 1
        else :
            number_to_count_map[number] = 1
            
number_of_ints = int(input())

count = 0

while count < number_of_ints :
    val = int(input())
    count = count + 1
    if val in number_to_count_map:
        print(number_to_count_map[val])            
    else:
        print("NOT PRESENT")