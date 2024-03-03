class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        left = right = result =  0
        while right < time:
            for i in range(len(clips)):
                temp_left =  clips[i][0]
                temp_right = clips[i][1]
                if temp_left<=left and temp_right>right:
                    right = temp_right
            if left == right: return -1
            left = right
            result += 1 
        return result