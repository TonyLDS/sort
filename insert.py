# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 17:24:54 2016

@author: luzhangqin
"""

#排序算法

#插入排序

#平均时间O(n^2)
#最差情形O(n^2)
#稳定度：稳定
#额外空间O(1)
#备注：大部分已排序时较好

'''
有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，
但要求插入此数据之后序列依旧有序。
刚开始的一个元素显然有序，然后插入一个元素到适当位置，
然后插入一个元素到适当位置，然后再插入第三个元素，依次类推。
'''

def insert_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len):
        if i == 0:
            continue
        else:
            for x in range(i):
                if nums[x] > nums[i]:
                    nums[x], nums[i] = nums[i], nums[x]
    

if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print('nums is: ', nums)
    insert_sort(nums)
    print('insert_sort: ',nums)