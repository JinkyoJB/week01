# 모범





# My
class ListNode:
    def __init__(self, item = 0, next=None):
        self.item = item
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        arr =[]
        for i in range(len(list1)):
            arr.append(list[i])
        for i in range(len(list2)):
            arr.append(list[i])

        temp = []

        q = (len(arr)) // 2
        i = 0; j = q + 1; t = 0
        temp = [0 for i in range(len(arr))]

        # arr to temp with 2 parts
        while i <= q and j <= len(arr):
            if arr[i] <= arr[j]:
                temp[t] = arr[i]; t += 1; i += 1
            else:
                temp[t] = arr[j]; t += 1; j += 1
        while i <= q:
            temp[t] = arr[i]; t += 1; i += 1
        while j <= len(arr):
            temp[t] = arr[j]; t += 1; i += 1

        # temp to arr
        i = 0; t = 0
        while i <= len(arr):
            arr[i] = temp[t]; t +=1; i += 1

        return(arr)
