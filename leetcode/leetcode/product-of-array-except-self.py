class Solution(object):
    def productExceptSelf(self, nums):
        product = [1]
        for i in range(1, len(nums)):
            product.append(nums[i-1] * product[-1])
        
        r_product = 1
        for i in range(len(nums)-1, -1, -1):
            product[i] *= r_product
            r_product *= nums[i]
        
        return product
