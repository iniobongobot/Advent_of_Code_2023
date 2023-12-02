import re

file = open('./input.txt', 'r+', encoding='UTF-8')

random_lists = [[i[0], i[1].strip().split(';')] for i in [i.rstrip('\n').split(':') for i in file.readlines()]]

def random_cubes_one(red_limit, green_limit, blue_limit):
    final_answer = 0
    success_dict = {}
    for random_list in random_lists:
        for random_cubes in random_list[1]:
            cube = (random_cubes.strip())
            red = re.search(r'(\d+)\sred',cube)
            green = re.search(r'(\d+)\sgreen', cube)
            blue = re.search(r'(\d+)\sblue', cube)

            blue = blue[1] if blue else 0
            green = green[1] if green else 0
            red = red[1] if red else 0
            if int(red) <= red_limit and int(green) <= green_limit and int(blue) <= blue_limit:
                if random_list[0] not in success_dict:
                    success_dict[random_list[0]] = 1
                else:
                    success_dict[random_list[0]] += 1
            else:
                success_dict[random_list[0]] = 0


                # print(red, green, blue)
                #
                # print(random_list[1])
        # print(success_dict, len(random_list[1]), random_list[0])
        if int(success_dict[random_list[0]]) == len(random_list[1]):
            final_answer += (int(random_list[0].replace('Game ', '')))

    print(final_answer)



# random_cubes_one(12, 13, 14)

def random_cubes_two():
    final_answer = 0
    success_dict = {}
    for random_list in random_lists:
        print(random_list[0])
        red_max = 0
        blue_max = 0
        green_max = 0
        for random_cubes in random_list[1]:
            cube = (random_cubes.strip())
            red = re.search(r'(\d+)\sred',cube)
            green = re.search(r'(\d+)\sgreen', cube)
            blue = re.search(r'(\d+)\sblue', cube)

            blue = int(blue[1]) if blue else 0
            green = int(green[1]) if green else 0
            red = int(red[1]) if red else 0

            red_max = red if red > red_max else red_max
            blue_max = blue if blue > blue_max else blue_max
            green_max = green if green > green_max else green_max

        print(red_max * green_max * blue_max)
        final_answer += red_max * green_max * blue_max
    print(final_answer)


random_cubes_two()
