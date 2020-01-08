def alghoritm(arr):
    i = 0
    for x in range(len(arr)):
        for j in range(len(arr)):
            if i == len(arr)-1:
                i = 0
            if arr[i] < arr[i+1]:
                arr.pop(i)
            else: i+=1
    return arr
