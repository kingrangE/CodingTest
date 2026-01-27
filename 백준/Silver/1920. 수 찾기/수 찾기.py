from bisect import bisect_left

int(input())
nums = sorted(list(map(int,input().split())))
int(input())
check_nums = list(map(int,input().split()))
for check_num in check_nums:
	try :
		if nums[bisect_left(nums,check_num)] == check_num : 
			print("1")
		else:
			print("0")
	except:
		print("0")
