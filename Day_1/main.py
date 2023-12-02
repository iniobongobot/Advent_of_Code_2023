from word2number import w2n
file = open('./file.txt', 'r+', encoding='UTF-8')
numbers = {"zero":0, "one":1,"two":2,
               "three":3, "four":4,"five":5,"six":6,"seven":7,"eight":8,
               "nine":9, "ten":10,"eleven":11,"twelve":12, "thirteen":13,
               "fourteen":14, "fifteen":15,"sixteen":16,"seventeen":17,
               "eighteen":18,"nineteen":19, "twenty":20,"thirty":30, "forty":40,
               "fifty":50,"sixty":60,"seventy":70, "eighty":80,"ninety":90}



calibration_list = [i.rstrip('\n') for i in file.readlines()]
calibration_sum = 0
for calibration in calibration_list:
    # Start of Part 2, Comment out to get Part one Answer
    # for keys, value in numbers.items():
    #     if calibration.lower().find(keys) != -1:
    #         calibration = calibration.replace(keys,  keys[0] + str(value) + keys[-1])
    # End of Part 2
    values = ''
    for char in calibration:
        if char.isnumeric():
            values += char
            break
    for char in calibration[::-1]:
        if char.isnumeric():
            values += char
            break
    print(calibration)
    # print(values)
    calibration_sum += int(values)

print(calibration_sum)
