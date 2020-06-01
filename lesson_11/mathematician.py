class Mathematician:
    @staticmethod
    def square_nums(nums):
        squared_nums = list(map(lambda x: x ** 2, nums))
        return squared_nums
    
    @staticmethod
    def remove_positives(nums):
##        for n in nums:          
##            if n > 0:
##                nums.remove(n)
##        return nums

        filtered_nums = list(filter(lambda x: x < 0, nums))

        return filtered_nums
    
    @staticmethod
    def filter_leaps():
        pass
    
    @staticmethod
    def additional():
        print('THis is staic method')


m = Mathematician()


def square(n):
    return n ** 2

##
##squared_nums = list(map(square, [1,2,3,4,5]))
##print(squared_nums)
##
##int_nums = list(map(int, ['1','2','3','4','5']))
##
##plus_nums = list(map(lambda x: x + 1, [1,2,3,4,5]))
numbers = [1,-2,3,-4,5, 6, -8]

filtered_numbers = m.remove_positives(numbers)
print(filtered_numbers)

