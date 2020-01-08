from . import alghoritm


def delete_sort(arr1, arr2, arr3):
    print('First array sorted:', ', '.join([str(x) for x in alghoritm.alghoritm(arr1)]))
    print('Second array sorted:', ', '.join([str(x) for x in alghoritm.alghoritm(arr2)]))
    print('Third array sorted:', ', '.join([str(x) for x in alghoritm.alghoritm(arr3)]))
