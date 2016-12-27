# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:51:10 2016

@author: luzhangqin
"""

#基于桶排序的基数排序
#正整数

def radix_sort(nums):
    count = 0
    top_digit = 1
    while top_digit:
        top_digit = 0
        s=[[] for i in range(10)]#因为每一位数字都是0~9，故建立10个桶
        '''对于数组中的元素，首先按照最低有效数字进行
           排序，然后由低位向高位进行。'''
        for i in nums:
            '''对于3个元素的数组[977, 87, 960]，第一轮排序首先按照个位数字相同的
               放在一个桶s[7]=[977],s[7]=[977,87],s[0]=[960]
               执行后list=[960,977,87].第二轮按照十位数，s[6]=[960],s[7]=[977]
               s[8]=[87],执行后list=[960,977,87].第三轮按照百位，s[9]=[960]
               s[9]=[960,977],s[0]=87,执行后list=[87,960,977],结束。'''
            s[i//(10**count)%10].append(i) #977/10=97(小数舍去),87/100=0
            if (i // 10**(count+1)) != 0:
                top_digit = 1
        nums = [j for i in s for j in i]
        count += 1
    return nums

if __name__ == '__main__':
    nums = [10, 80, 4, 1, 2, 6, 7, 3,81]
    print('nums is: ',nums)
    nums = radix_sort(nums)
    print ('radix_sort',nums)