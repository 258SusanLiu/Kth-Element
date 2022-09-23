#Citation for the following functions: merge_sort, merge
#Date 10/6/2021
#Copied from: canvas and Github
#Source URL:
#  https://github.com/DURepo/CS_325_Exercises/blob/main/DivideAndConquer-mergeSort.py
#  https://canvas.oregonstate.edu/courses/1830227/pages/exploration-divide-and-conquer-algorithms?module_item_id=21389046


def merge_sort(Arr,start,end):
    if(start<end):
        mid = (start+end)//2 #Computes floor of middle value
        merge_sort(Arr,start,mid)
        merge_sort(Arr,mid+1,end)
        merge(Arr,start, mid, end)

def merge(Arr, start, mid, end):
  #temporary arrays to copy the elements of subarray
  leftArray_size = (mid-start)+1
  rightArray_size = (end-mid)

  leftArray = [0]*leftArray_size
  rightArray = [0]*rightArray_size

  for i in range(0, leftArray_size):
    leftArray[i] = Arr[start+i]

  for i in range(0, rightArray_size):
    rightArray[i] = Arr[mid+1+i]

  i=0
  j=0
  k=start

  while (i < leftArray_size and j < rightArray_size):
    if (leftArray[i] < rightArray[j]):
      # filling the original array with the smaller element
      Arr[k] = leftArray[i]
      i = i+1
    else:
      # filling the original array with the smaller element
      Arr[k] = rightArray[j]
      j = j+1
    k = k+1

  # copying remaining elements if any
  while (i<leftArray_size):
    Arr[k] = leftArray[i]
    k = k+1
    i = i+1

  while (j<rightArray_size):
    Arr[k] = rightArray[j]
    k = k+1
    j = j+1


if __name__ == '__main__':
  Arr1 = [1,4,6,4]
  Arr2 = [5,6,1,8]
  join = Arr1+Arr2
  #print(join)
  
  k=input("Which k element you want to see?\n")
  k=int(k)
  #print(type(k))
  length=len(join)
  length=int(length)
  if length<k:
    print("You are searching outside of array length")
    exit()
  else:
    #print(length)
    merge_sort(join,0, length-1)
    print(join)
    thex=join[int(k-1)]
    print(thex)
  
  
  #merge_sort(Arr, 0, 8)
  #print(Arr)  