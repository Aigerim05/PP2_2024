x = ['o', 'key2', 'key3']
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


# class myclass():
#     def __init__(self, title) -> None:
#         self.title = title
#     def __len__(self):
#         if (self.title.count("a") % 2 == 0):
#             return 1
#         return 0

# x = myclass(input())
# print(bool(x))