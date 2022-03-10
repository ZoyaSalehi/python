def sort_sizes(A):
    A = [x.lower() for x in A]

    A.sort(reverse=True)

    print(A)

sort_sizes(['s', 'L', 'm', 'S', 'M', 'S', 'l', 'l'])
