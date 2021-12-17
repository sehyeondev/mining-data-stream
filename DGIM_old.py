import sys
import math

# from the number of ones, make buackets
# EX) # ones = 11, [4.0, 4.0, 2.0, 1.0] buckets are returned
# size_cnt = 3 because buckets of  size (4, 2, 1) are needed
# bucket_dec = 4 because 4th bucket among buckets of size (4, 2, 1) 
# bucket_bin = 100 because 4 is 100 in binary number 
def make_bucket(one_cnt):
    buckets = []
    # if there's no one, return empty bucket
    if one_cnt == 0:
        return buckets

    # compute the number of size of buckets
    if one_cnt+1 == math.pow(2, math.floor(math.log2(one_cnt))+1):
        size_cnt = math.floor(math.log2(one_cnt)) + 1
    else:
        size_cnt = math.floor(math.log2(one_cnt))
    
    # compute how full the buckets are EX) # ones = 11, bucket_bin = 100
    bucket_dec = one_cnt - (math.pow(2, size_cnt) - 2) -1
    bucket_bin = format(int(bucket_dec), "b")

    # compute how many buckets there are in each size  
    for j in range(size_cnt - len(bucket_bin)):
        buckets.append(math.pow(2, size_cnt-j-1))
    for j in range(len(bucket_bin)):
        for _ in range(int(bucket_bin[j]) + 1):
            buckets.append(math.pow(2, (len(bucket_bin)-j-1) ))

    # return final buckets ex) [4.0, 4.0, 2.0, 1.0]
    return buckets

argv = sys.argv
file = open(argv[1], 'r')
stream =  list(map(int, file.readlines()))

for k in argv[2:]:
    # estimate # 1's in last k bits
    if k == "0":
        print(0)
        continue
    last_k_bits = stream[-int(k):]
    buckets = make_bucket(sum(stream))
    for i in range (len(buckets)):
        if sum(buckets[-(i+1):]) >= sum(last_k_bits):
            break
    buckets_in_k = buckets[-(i+1):]
    estimate = buckets_in_k[0]/2 + sum(buckets_in_k[1:])
    print(estimate)

        
