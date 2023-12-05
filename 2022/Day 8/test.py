# def maxCost(cost, labels, dailyCount):
#     passed=[]
#     failed=[]
#     max_daily_cost=[]
#     laptop = zip(cost,labels)
#     laptop=list(laptop)
#     chunked_list = list()
#     for i in range(0,len(laptop),dailyCount):
#         if laptop(y[1] for y in laptop) == 'illegal':
#             failed.append(y[1] for y in laptop)
#         elif laptop(y[1] for y in laptop) == 'legal':
#             passed.append(y[1] for y in laptop)
#         chunked_list.append(laptop[i:i+dailyCount])
#     print(passed)
#     # for x in chunked_list:
#     #     # print(x)
#     #     for a in x:
#     #         # print(a)
#     #         if a[1] == 'legal':
#     #             max_daily_cost.append(a[0])
#     # # print(chunked_list)


# cost=[0,3,2,3,4]
# label = ['legal','legal','illegal','legal','legal',]
# count = 2 # 'legal' per day
# total = maxCost(cost,label,count)
# print(total)

students = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    scores.append(score)
secondlow = sorted(list(set(scores)))
names = sorted([name for [name,score] in students if score == secondlow[1]])
a = [print(i) for i in names]