input = open("2023/input.txt",'r').read().splitlines()

numbers = []
numlist = ["one","two","three","four","five","six","seven","eight","nine"]

lettonum = {"one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9}


def text2int(textnum):
    units = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    if textnum.find(units) >=0:
        
      

for x in input:
   print (text2int(x))


# for line in input:
#         print(f"{line}")
#         for x in numlist:
#                 if line.find(x) >= 0:
#                         print(f"Found match from  numlist: {line.find(x)}")
#                 else: 
#                         continue



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

