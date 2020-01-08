from array_func.gen_array import gen_array
from array_func.print_arr import print_arr
from logic.general import delete_sort


def main():
    arr1 = gen_array(int(input("Dimmenstion of 1 array: ")))
    arr2 = gen_array(int(input("Dimmenstion of 2 array: ")))
    arr3 = gen_array(int(input("Dimmenstion of 3 array: ")))
    print_arr(arr1, arr2, arr3)
    delete_sort(arr1, arr2, arr3)


if __name__ == '__main__':
    main()
