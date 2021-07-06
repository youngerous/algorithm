numbers = set(range(1, 10001))
generator = set()
for num in numbers:
    for n in str(num):
        num += int(n)
    generator.add(num)

self_nums = numbers - generator
for self_num in sorted(self_nums):
    print(self_num)
