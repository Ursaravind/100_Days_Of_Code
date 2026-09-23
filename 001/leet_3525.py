nums = [1, 2, 3, 4, 5]
k = 3
queries = [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]]


# step:1 subsititute nums[index] = values , query = [index , value , start , x]

# query_map = {}
# for index in range(0,len(queries)):
#     query_map[index] = {"i":queries[index][0],"v":queries[index][1],"s":queries[index][2],"x":queries[index][3]}


# print(query_map)


# # subsititue nums[i] = value
# print(nums)

# for _ , values in query_map.items():
#     # print(values)
#     for key , val in values.items():
#         if key == "i":
#             nums[val] = values["v"]
#     print(nums)

for query in queries:
    i, v, s, x = query
    nums[i] = v
    print(nums)

