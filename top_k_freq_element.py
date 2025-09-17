def topKFrequent(nums, k):
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        sorted_freq=sorted(freq.items(),key=lambda item:item[1])

        top_k=[item[0] for item in sorted_freq[-k:]]

        return top_k
if __name__ =="__main__":
    nums=list(map(int,input().split()))
    k=int(input())
    print(topKFrequent(nums,k))