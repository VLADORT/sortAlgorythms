def heapSort(li):
    def downHeap(li, k, n):
        new_elem = li[k]
        while k <= n / 2:
            child = 2 * k
            if child < n and li[child] < li[child + 1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem

    size = len(li)
    for i in range(round(size / 2 - 1), -1, -1):
        downHeap(li, i, size - 1)
    for i in range(size - 1, 0, -1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i - 1)
    return li

def quickSort(li):
    if len(li) == 1 or len(li) == 0:
        return li
    else:
        pivot = li[0]
        i = 0
        for j in range(len(li)-1):
            if li[j+1] < pivot:
                li[j+1],li[i+1] = li[i+1], li[j+1]
                i += 1
        li[0],li[i] = li[i],li[0]
        first_part = quickSort(li[:i])
        second_part = quickSort(li[i+1:])
        first_part.append(li[i])
        return first_part + second_part

a=[79, 24, 191, 71, 46, 73, 187, 107, 9, 167, 134, 95, 189, 68, 50, 54, 40, 5,144,57]
print(heapSort(a))
print(quickSort(a))