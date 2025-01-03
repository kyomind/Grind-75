import heapq


# hash map + min heap 法
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 先算出每個數字出現的次數
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
            # 相當於 counter[n] = counter.get(n, 0) + 1

        # 用最小堆積來找出前 k 個最大的數字
        heap = []  # XXX 要初始化一個空的 list，然後再用 heapq.heapify() 來建立最小堆積
        # 接著就是常規操作，push和pop已足夠
        # 但請注意，需要排序的是第一個元素！ XXX 這裡是 counter[n]，而不是 n 本身
        for n, count in counter.items():
            # 寫法不佳，改用衛語句把else的部分拿掉
            # if len(heap) < k:
            #     heapq.heappush(heap, (count, n))
            # else:
            #     if count > heap[0][0]:
            #         heapq.heappop(heap)
            #         heapq.heappush(heap, (count, n))

            # 這樣寫比較好，直觀很多！
            heapq.heappush(heap, (count, n))
            if len(heap) > k:
                heapq.heappop(heap)

        # 迴圈結束後，heap 裡面就是前 k 個最大的數字
        # 我們只需要取出第二個元素即可，次數不需要
        return [n for _, n in heap]
