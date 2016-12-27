# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:19:00 2016

@author: luzhangqin
"""

#排序算法

#冒泡排序

#平均时间O(n^2)
#最差情形O(n^2)
#稳定度：稳定
#额外空间O(1)
#备注：n小时较好

'''
原理是临近的数字两两进行比较,按照从小到大或者从大到小的顺序进行交换,
这样一趟过去后,最大或最小的数字被交换到了最后一位,
然后再从头开始进行两两比较交换,直到倒数第二位时结束,以此类推。
'''
def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1],nums[j]
        


if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print('nums is: ',nums)
    bubble_sort(nums)
    print ('bubble_sort',nums)