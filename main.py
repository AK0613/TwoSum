# Given an array of integers, return the indices of the two numbers that add up to a given target

nums = [1, 3, 7, 9, 2]
tgt = 11


def find_tgt(nums, tgt):
    num_items = len(nums)
    dict = {}

    if num_items > 2:
        for x in range(num_items):
            num2find = tgt - nums[x]
            if nums[x] in dict:
                sol = [dict.get(nums[x]), x]
                print(f'The answer is [{dict.get(nums[x]), x}] since {num2find} + {nums[x]} = {tgt}')
                return sol
            else:
                dict[num2find] = x


solution = find_tgt(nums, tgt)
print(solution)

# Runs at O(n^2)
# def find_tgt(set, tgt):
#     set_len = len(set)
#     if(set_len >= 2):
#         for p1 in range(set_len):
#             for p2 in range(p1 + 1, set_len):
#                 num2find = tgt - set[p1]
#                 if set[p2] == num2find:
#                     solution = [p1, p2]
#                     print(f'Solution with index of [{p1},{p2}] since {set[p1]}+{set[p2]} = {set[p1]+set[p2]}')
#                     return solution
#     else:
#         print('List does not contain enough items')
#
#
#
#
# print(sol_found)
