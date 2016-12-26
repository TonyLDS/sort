# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 11:46:38 2016

@author: luzhangqin
"""

#排序算法

#shell排序

#平均时间O(nlogn)
#最差情形O(n^s) 1<s<2
#稳定度：不稳定
#额外空间O(1)
#备注：s是所选分组

'''
希尔排序，也称递减量增量排序算法，希尔排序是非稳定排序算法。
该方法又称缩小增量排序，因DL.Shell于1959年提出而命名。
先选取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。
所有距离为d1的倍数的记录放在同一个组中。
先在组内进行排序，然后取第二个增量d2。
'''

def shell_sort(nums):
    nums_len = len(nums)
    rf = 3
    gap = nums_len // rf #增量
    while gap > 0:
        for i in range(gap):
            m = i
            while m < nums_len:
                if m == i:
                    pass
                else:
                    for j in range(m, i, -gap):
                        if nums[j] < nums[j - gap]:
                            nums[j], nums[j-gap] = nums[j-gap], nums[j]
                        else:
                            break
                m += gap
        if (gap // rf == 0 and gap != 1):
            gap = 1
        else:
            gap //= rf
                    

if __name__ == '__main__':
    nums = [49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    print('nums is: ', nums)
    shell_sort(nums)
    print('shell_sort: ',nums)