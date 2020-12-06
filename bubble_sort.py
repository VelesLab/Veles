def bubble_sort(mas):
    # mas = list(map(int,input().split()))
    count = 0
    for run in range(len(mas)-1):
        for i in range(len(mas)-1 - run):
            if mas[i] > mas[i + 1]:
                count += 1
                mas[i], mas[i+1] = mas[i+1], mas[i]
    print(*mas)
    print(count)


bubble_sort(list(map(int,input().split())))

