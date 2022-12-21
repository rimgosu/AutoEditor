if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5]
 
    dup = [x for i, x in enumerate(nums) if i != nums.index(x)]
    print(dup)  # [1, 5, 1]
 