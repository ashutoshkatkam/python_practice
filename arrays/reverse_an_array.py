def reverse_an_array_slicing(arr):
    return arr[::-1]

def reverse_an_array_2_pointer(arr):
    left = 0
    right = len(arr)

    # swap the left and right until left is less than right

    while left < right:
        arr[left],arr[right]=arr[right],arr[left]
        left += 1
        right -= 1
    return arr

def reverse_an_array_swap(arr):
    i = 0

    # swap i with n-i-1 until i < mid index
    n = len(arr)
    mid = (n-1)//2 
    
    while i<=mid:
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
        i += 1
    return arr

def reverse_an_array_recursion(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    reverse_an_array_recursion(arr,l+1,r-1)


if __name__ == "__main__":
    print(reverse_an_array_slicing([1,2,3,4,5,6,7]))
    print(reverse_an_array_slicing([1,2,3,4,5,6,7]))
    print(reverse_an_array_swap([1,2,3,4,5,6,7]))

    arr = [1,2,3,4,5,6]
    reverse_an_array_recursion(arr,0,len(arr)-1)
    print(arr)