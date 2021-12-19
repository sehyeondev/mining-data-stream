import sys
import math

size_dic = {1:0}
buckets = []

# merge bucket if there are three buckets of same size
def merge_buckets():
    # pop buckets of same size and merge them
    recent = buckets.pop()
    buckets.pop()
    cur_size = recent[1]
    next_size = cur_size*2
    size_dic[cur_size] = 0

    # there are still three buckets of same size
    if math.log2(cur_size)+2 <= len(size_dic):
        if size_dic[next_size] == 2:
            size_dic[next_size] = 0
            merge_buckets()
    
    # append merged bucket with most recent end 
    if math.log2(cur_size)+2 > len(size_dic):
        size_dic[next_size] = 0
    size_dic[next_size] += 1
    buckets.append((recent[0], next_size))
    return True

argv = sys.argv
file = open(argv[1], 'r')
stream =  list(map(int, file.readlines()))

timestamp = 0
for bit in stream:
    timestamp += 1
    # if new bit = 0, do nothing
    if bit == 0:
        continue
    # here, new bit = 1
    # if there are three buckets of size 1 merge buckets first
    if size_dic[1] == 2:
        merge_buckets()
    # now, create new bucket with current timestamp and size 1
    buckets.append((timestamp, 1))
    size_dic[1] += 1

# for each k, estimate # 1s in most recent k bits
for k in argv[2:]:
    k = int(k)
    if k == 0:
        print(0)
        continue
    # find bucket with earliest timestamp in k most recent bits
    for i in range (len(buckets)):
        if buckets[-(i+1)][0] < timestamp-k+1:
            break
    in_k_bits = [bucket[1] for bucket in buckets[-i:]]
    # estimate # 1s using sizes of buckets
    estimate = in_k_bits[0]/2.0 + sum(in_k_bits[1:])
    print(estimate)