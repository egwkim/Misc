def get_next_row(row, n):
    next_row = [0]*(len(row)+n-1)
    for i, x in enumerate(row):
        for j in range(n):
            next_row[i+j] += x
    return next_row


def get_mth_row(n, m, row=[1]):
    '''
    By default, [1] is the 0th row.
    '''
    for i in range(m):
        row = get_next_row(row, n)
    return row


def get_mth_table(n, m, row=[1]):
    '''
    By default, [[1]] is the 0th table.
    '''
    table = []
    table.append(row)
    for i in range(m):
        row = get_next_row(row, n)
        table.append(row)
    return table


if __name__ == "__main__":
    n = 6
    m = 10
    table = get_mth_table(n, m)

    for r in table:
        print(r)

    import matplotlib.pyplot as plt

    ys = table[-1]
    xs = range(len(ys))

    plt.plot(xs, ys, 'o')
    plt.vlines(xs, 0, ys)
    plt.ylim(bottom=0)
    plt.show()
