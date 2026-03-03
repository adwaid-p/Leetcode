# Sort Elements of an Array by Frequency

# Problem Statement: Given an array of integers, having some duplicate elements, sort the array by frequency .

# Examples

# Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
# Output: 2 2 2 1 1 3 3 4 
# Explanation: Since  2 is present 3 times in an array , so print it 3 times ,
# then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.

# Input: N = 6, array[] = {-199,6,7,-199,3,5}
# Output: -199 -199 3 5 6 7
# Explanation: Since -199 is present 2 times so it will be printed at first , then 3 , 5 ,6 ,7 are present once in array ,
# so print them in their sorted order.

arr = [1,1,2,2,2,3]
freq_dict = {}

for num in arr:
    freq_dict[num] = freq_dict.get(num,0)+1     # Check the number present in the dictionary 
                                                # If it present then retrun the number and then add 1 to it
                                                # If it not presnet then return 0 and then add 1 to it
sorted_items = sorted(freq_dict.items(), key=lambda x :(x[1],x[0]))

result = []

for num, count in sorted_items:
    result.extend([num]*count)

print(result)