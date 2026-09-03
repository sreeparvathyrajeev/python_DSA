class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        num_of_zeros=0
        free_positions=[]
        flowers_left=n
        length_of_flowerbed= len(flowerbed)
        my_flowerbed=flowerbed
        for i in range(length_of_flowerbed):
            if flowerbed[i]==0:
                num_of_zeros+=1
                free_positions.append(i)
        if num_of_zeros < n:
            return False
        if length_of_flowerbed==1:
            return True
        for j in free_positions:
            
            if j==0:
                if my_flowerbed[j+1]==0:
                    flowers_left-=1
                    
                    my_flowerbed[j]=1
                else:
                    num_of_zeros-=1
                    if num_of_zeros<flowers_left:
                        return False
            elif j==(length_of_flowerbed-1):
                if my_flowerbed[j-1]==0:
                    flowers_left-=1
                    
                    my_flowerbed[j]=1
                else:
                    num_of_zeros-=1
                    if num_of_zeros<flowers_left:
                        return False
            elif my_flowerbed[j-1]==0 and my_flowerbed[j+1]==0:
                flowers_left-=1
                
                my_flowerbed[j]=1
            else:
                num_of_zeros-=1
                if num_of_zeros<flowers_left:
                        return False
        if flowers_left<=0:
            return True
        else:
            return False

                
                    

                    
