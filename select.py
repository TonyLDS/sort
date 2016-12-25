# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 20:25:07 2016

@author: luzhangqin
"""

#排序算法

#选择排序

#平均时间O(n^2)
#最差情形O(n^2)
#稳定度：不稳定
#额外空间O(1)
#备注：n小时较好

'''
选择排序是一种简单直观的排序算法。
他的工作原理如下。
首先在未排序序列中找到最大（小）的元素，存放到排序序列的起始位置，
然后，从剩余为排序元素 中继续找寻最大（小）的元素，放到排序序列的末尾。
以此类推，直到所有元素排序完毕。
'''

def select_sort(nums):
    nums_len = len(nums)
    min_key = 0
    for i in range(nums_len):
        min_key = i
        for x in range(i + 1, nums_len):
            if nums[min_key] > nums[x]:
                min_key = x
        nums[min_key], nums[i] = nums[i], nums[min_key]

if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print('nums is: ', nums)
    select_sort(nums)
    print('select_sort: ',nums)
