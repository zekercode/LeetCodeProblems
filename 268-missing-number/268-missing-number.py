class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortednums = nums.sort()
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (right + left)//2
            if mid == nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
            
            
           
            
#       POSITION       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
 #          NUMS       0 1 2 3 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20
  #                    L                                               R
   #                                        M
    #                                          L
  #
   #                                          11 12 13 14 15 16 17 18 19
    #                                         11 12 14 15 16 17 18 19 20
     #                                        L                        R
      #                                                 M
       #                                      L      R
        #                                         M
         #                                           L
          #                  
        #                            when L and R are pointing to the same location
        #                            then we know that's where the missing value is
        #                            so we can either return L or R to get the missingnumber
           #                 RETURN L OR R
                          
                
                
                
            #    IF MID = NUMS[MID] MOVE L POINTER TO MID + 1
             #   IF MID < NUMS[MID] MOVE R POINTER TO MID - 1
                # Theres never going to be a situation where mid > nums because that would mean some numbers are repeated