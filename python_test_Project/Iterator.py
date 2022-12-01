# Iterator when we want values from list
# we can use for loop but its required index number but in below we can do without index values

num = [12, 44, 55, 6, 4, 2, 6]

it = iter(num)

print(it)  # gives object
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))


# build own iterator

class top10:

    def __init__(self):
        self.num = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 20:
            val = self.num
            self.num += 1
            return val
        else:
            raise exit()


values = top10()

# print(next(values))


for i in values:
    print(i)
