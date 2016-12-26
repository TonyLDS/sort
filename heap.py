# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:17:19 2016

@author: luzhangqin
"""

#排序算法

#堆排序

#平均时间O(nlogn)
#最差情形O(nlogn)
#稳定度：不稳定
#额外空间O(1)
#备注：n大时较好

'''
堆的定义：在起始索引为0的堆中：
节点i的右子节点在位置2×i+2,
节点i的父节点在位置floor((i-1)/2)
备注：floor表示取整。

堆的特性：
每个节点的键值一定大于（或小于）他的父节点。

最大堆：
堆的根节点保存的是键值最大的节点。
即堆中每个节点的键值都总大于他的子节点。

上移，下移：
当某个节点的键值大于他的父节点时，就要进行上移的操作，
即把该节点移动到父节点的位置，
而让他的父节点到他的位置，然后继续判断该节点，
直到该节点不再大于他的父节点为止。
当某节点键值变小之后，就要进行下移操作。

方法：
首先建立一个最大堆时间复杂度为O(n),
然后每次只需要把根节点与最后一个位置的节点交换，
然后把最后一个位置排除在外，
然后把交换后的根节点进行调整（时间复杂度为O(lgn)），
即对根节点进行下移操作。
堆排序总时间复杂度为O(nlgn)
''' 

#保存最大堆性质
#使以i为根的子数成为最大堆    
def max_heapify(nums, i, heap_size):
    if heap_size < 0:
        pass
    else:
        #将父节点和较大的子节点进行交换
        #从下往上建立最大堆
        largest = i
        lchild = i * 2 + 1
        rchild = i * 2 + 2
        if lchild < heap_size and nums[lchild] > nums[largest]:
            largest = lchild
        if rchild < heap_size and nums[rchild] > nums[largest]:
            largest = rchild
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            #追踪largest
            max_heapify(nums, largest, heap_size)

#建堆
def bulid_max_heap(nums):
    heap_size = len(nums)
    if heap_size > 1:
        node  = (heap_size - 1) // 2
        while node >= 0:
            max_heapify(nums, node, heap_size)
            node -= 1

def heap_sort(nums):
    bulid_max_heap(nums)
    heap_size = len(nums)
    i = heap_size -1
    while i > 0:
        #将根节点和最后未交换的子节点进行交换
        nums[i], nums[0] = nums[0], nums[i]
        #堆长度减少1
        heap_size -= 1
        #交换以后指针向前一位
        i -= 1
        #根节点进行下移,保证最大堆
        max_heapify(nums, 0, heap_size)


if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print('nums is: ', nums)
    heap_sort(nums)
    print('heap_sort: ',nums)