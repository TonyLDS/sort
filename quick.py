# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:48:28 2016

@author: luzhangqin
"""

#排序算法

#快速排序

#平均时间O(nlogn)
#最差情形O(n^2)
#稳定度：不稳定
#额外空间O(nlogn)
#备注：n大时较好

'''
快速排序算法和归并算法一样，也是基于分治算法。
对于子数组A[p...r]快速排序的分治过程的三个步骤为：
分解：
    把数组A[p...r]分为A[p...q-1]和A[q+1...r]两部分，
其中A[p...q-1]中的每个元素都小于等于A[q],
而A[q+1...r]中的每个元素都大于等于A[q]。
解决：
    通过递归调用快速排序，对子数组A[p...q-1]和A[q+1...r]进行排序;
合并：
    因为两个子数组是就地排序的，所以不需要额外操作。
    
对于划分partition每一轮迭代的开始，x=A[r],
对于任何数组下标k，有：
1)如果p<=k<=i,则A[k]<=x
2)如果i+1<=k<=j-1,则A[k]>x
3)如果k=r,则A[k]=x
'''

'''
划分使满足A[r]为基准对数组进行一个划分，比A[r]小的放左边，大的放右边。
快速排序的分治partition有两种：
一种是上述两指针索引一前一后逐步向后扫描的方法，
另一种两指针从首位向中间扫描的方法。
'''
#方法1
def partition(nums, p, r):
    x = nums[r]
    i = p - 1
    j = p
    while j < r:
        if nums[j] < x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1

#方法2
def partition2(nums, p, r):
    i = p
    j = r
    x = nums[p]
    while i < j:
        while i < j and nums[j] >= x:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1
        while nums[i] <= x and i < j:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
        nums[i] = x
    return i

    nums[j] = nums[i]
    nums[i] = x
    return i
    

def quick_sort(nums, p, r):
    if p < r:
        q = partition2(nums, p, r)
        quick_sort(nums, p, q-1)
        quick_sort(nums, q+1, r)

if __name__ == '__main__':
    nums = [2,8,7,1,3,5,6,4]
    print('nums is: ', nums)
    quick_sort(nums, 0, len(nums)-1)
    print('quick_sort: ',nums)