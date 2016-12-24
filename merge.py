# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:36:50 2016

@author: luzhangqin
"""

#排序算法

#归并排序

#平均时间O(nlogn)
#最差情形O(nlogn)
#稳定度：稳定
#额外空间O(1)
#备注：n大时较好

'''
归并排序也称合并排序，是分治法的典型应用。
分治思想是将每个问题分解成各个小问题，将每个小问题解决，然后合并。

将一组无序数按n/2递归分解成只有一个元素的子项，一个元素就是已经排序好的了。
然后将这些有序的子元素进行合并。

合并过程就是对两个已经排序好的的子序列，先选取两个子序列中最小的元素进行比较，
选择两个元素最小的那个子序列并将其从子序列去掉并添加到最终的结果集中，
直到两个子序列归并完成。
'''

def merge(nums, first, middle, last):
    #print(first, ' ',middle, '', last)
    #切片边界，左闭右开并且是0为开始
    lnums = nums[first: middle + 1]
    rnums = nums[middle + 1: last + 1]
    
    temp = []
    i = first
    
    while(len(lnums) and len(rnums)):
        if lnums[0] < rnums[0]:
            temp.append(lnums.pop(0))
        else:
            temp.append(rnums.pop(0))
        
    temp = temp + lnums + rnums
    
    for x in temp:
        nums[i] = x
        i += 1
        

def merge_sort(nums, first, last):
    #print(first, ' ', last)
    if first < last:
        middle = (first + last) // 2
        merge_sort(nums, first, middle)
        merge_sort(nums, middle + 1, last)
        merge(nums, first,middle, last)



if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print('nums is: ',nums)
    merge_sort(nums, 0, len(nums) - 1)
    print ('merge_sort',nums)