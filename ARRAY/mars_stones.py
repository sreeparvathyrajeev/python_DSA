#greedy algorithm

def max_num_stones(m,common_weights):
    mars_set=set(range(1,m+1))
    common_set=set(common_weights)
    mars_weights=sorted(list(mars_set - common_set))
   
    
    weight_sum=0
    count=0
    for weight in mars_weights:
        if weight_sum + weight <= m:
            weight_sum += weight
            count+=1
        else:
            break
    return count

if __name__ == "__main__":
    m=int(input())
    
    common_weights=list(map(int,input().split()))

    max_stones=max_num_stones(m,common_weights)
    print(max_stones)

        
    
    




