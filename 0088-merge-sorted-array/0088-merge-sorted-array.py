class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        src = m-1
        tgt = m+n-1
        
        for i in range(m):
            nums1[tgt-i] = nums1[src-i]
        
        print(f'nums1 = {nums1}')
        x,y = n,0
        
        for i in range(m+n):
            if x >= m+n:
                nums1[i] = nums2[y]
                y+=1
            elif y >= n:
                nums1[i] = nums1[x]
                x+=1
            else:
                if nums1[x] < nums2[y]:
                    nums1[i] = nums1[x]
                    x+=1
                else:
                    nums1[i] = nums2[y]
                    y+=1
