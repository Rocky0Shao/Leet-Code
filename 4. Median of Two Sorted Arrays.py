class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out = []
        for i in nums1:
            
            out.append(i)
        print(f"nums1: {nums1}\n nums2: {nums2}")
        if len(nums1) == 0 and len(nums2) == 0: return 0
        for i in nums2:
            out.append(i)
        out = sorted(out)
        print(f"out: {out}")

        #short circuits
        if len(out) == 0: return 0
        if len(out) == 1: return out[0]
        if len(out) %2 ==0:
            late_index = int(len(out)/2)
            early_index = late_index -1
            print("even")
            print(f"len: { len(nums1)}\nlate_index: {late_index}\nearly_index: {early_index}")
            return (out[late_index] + out[early_index])/2
        print("odd")
        middle = int(len(out)/2)
        return out[middle]
