input = open("2023/input.txt",'r').read().splitlines()

numbers = []

numdict = ["one","two","three","four","five","six","seven","eight","nine"]

lettonum = {"one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9}

for line in input:
        u = 1
        for x in numdict:
                print(f"line{u}: {(line.find(x))}")
                u += 1
                



# for l in input:
#         number = l.translate({ord(i): None for i in 'abcdefghijklmnpoqrstuvqwxyzxz'})
#         if len(number) > 2:
#                 number = (f"{number[0]}{number[-1]}")
#                 print(number)
#         elif len(number) == 1:
#                 number = (f"{number}{number}")
#                 print(number)
#         else:
#                 print(number)
#         numbers.append(int(number))       

# print(sum(numbers))

