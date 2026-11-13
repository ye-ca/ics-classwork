input_string = input(" input something atp: ")

initial_list = input_string.split(" - ")

final_list = []

for i in range(len(initial_list)):
    temp_list = initial_list[i].split(",")
    temp_coords = []
    for i in range(2):
        another_temp_list = temp_list[i].split(":")
        temp_coords.append(int(another_temp_list[1]))
    final_list.append(temp_coords)

print(final_list)
    
