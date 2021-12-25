

def get_pivot_low_high(low, high, data: list):

    pivot = data[high]
    pivot_index = high
    i = low
    j = high -1

    while i <= j:

        while data[i] < pivot:
            i +=1

        while data[j] > pivot:
            j -= 1

        if i <= j:
            data[i], data[j] = data[j], data[i]

        if i >= j:
            # print('swap',data, i, high)
            data[i],data[high] = data[high],data[i]
            # print('swap',data, i, high)
            pivot_index = i
            # print('if',data,i,j,high)
            break

    return pivot_index

def get_pivot(low, high, data: list):

    i = low-1
    pivot = data[high]
    j = low
    while j < high:

        if data[j] <= pivot:

            i+=1
            data[i],data[j] = data[j],data[i]

        j +=1

    data[i+1],data[high] = data[high],data[i+1]

    pivot_index = data.index(pivot)

    return pivot_index

def quick_sort(low, high, data: list):

    if low < high:
        pivot_index = get_pivot(low, high, data)

        # print(low,pivot_index,high)
        print(data)

        quick_sort(low=low,high=pivot_index-1,data=data)
        quick_sort(low=pivot_index+1,high=high,data=data)


if __name__ == '__main__':

    # data = ['e','d','c','b','a']
    data = [8,7,6,1,0,9,2]
    data = [8,7,6,5,4,3,2,1]
    print(data)
    last_index = len(data)-1
    low = 0
    high = last_index

    quick_sort(low=0, high=last_index, data =data)
