class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            height_left=height[left]
            height_right=height[right]
            current_area=min(height_left,height_right)*width
            max_area=max(current_area,max_area)
            if height_left<height_right:
                left+=1
            else:
                right-=1
        return max_area
        # left=0
        # right=len(height)-1
        # max_area=0
        # while left<right:
        #     width=right-left
        #     height_left=height[left]
        #     height_right=height[right]
        #     current_area=min(height_left,height_right)*width
        #     max_area=max(max_area,current_area)
        #     if height_left < height_right:
        #         left+=1
        #     else:
        #         right-=1
        # return max_area