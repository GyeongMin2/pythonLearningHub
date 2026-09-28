# 리스트 또 손봄 — count만 추가
nums = [10, 20, 5, 7, 10]
print('첫값', nums[0], '길이', len(nums))
nums.append(3)
print('append 후', nums)
nums.sort()
print('정렬', nums)
print('10 개수', nums.count(10))
