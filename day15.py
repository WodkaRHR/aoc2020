from collections import defaultdict

nums = [2,0,1,7,4,14,18]
nums_set = set(nums[:-1]) # Does not hold the previous number

idxs = defaultdict(list)
for idx, n in enumerate(nums):
    idxs[n].append(idx)

while len(nums) < 30000000: # < 2020:
    previous = nums[-1]
    if previous not in nums_set:
        new_num = 0
    else:
        idx_previous = idxs[previous]
        new_num = idx_previous[-1] - idx_previous[-2]
    # print(f'new num is {new_num}')
    idxs[new_num].append(len(nums))
    nums.append(new_num)
    nums_set.add(previous)

print(nums[-1])

