Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Note: If the number x is not found in the array just print '-1'

Example:
Input:
2
9 5
1 3 5 5 5 5 67 123 125
9 7
1 3 5 5 5 5 7 123 125

Output:
2 5
6 6


#code

def firstOccurence(array,size,peak_element):
    low = 0
    last = size-1
    while(low<=last):
        mid = (low+last)//2
        if (array[mid] == peak_element and (mid==0 or array[mid-1] != peak_element)):
            return mid;
        if (array[mid] >= peak_element):
            last = mid-1;
        else:
            low = mid+1;
    return -1
    
    
def lastOccurence(array,size,peak_element):
    low = 0
    last = size-1
    while(low<=last):
        mid = (low+last)//2
        if (array[mid] == peak_element and (mid == size-1 or array[mid+1] != peak_element)):
            return mid;
        if (array[mid] <= peak_element):
            low = mid+1;
        else:
            last = mid-1;
    return -1
    
    
    
    
test_case = int(input())
for i in range(test_case):
    size,peak_element = map(int,input().split())
    array = list(map(int,input().split()))
    first_occur = firstOccurence(array,size,peak_element)
    last_occur = lastOccurence(array,size,peak_element)
    if(first_occur == -1 or last_occur == -1):
        print(-1)
    else:
        print(first_occur,end=" ")
        print(last_occur)
    
