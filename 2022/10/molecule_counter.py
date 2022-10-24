"""
TODO
Fix incorrect counting
 - Do not count same graph with different order
 - Exampel:
   [[], [0, 0], [0, 0], [1, 1, 2, 2]] and
   [[], [0, 0], [1, 1], [0, 0, 2, 2]]
"""


def get_unused_degrees(unused_atoms):
    return sum((i+1)*j for i, j in enumerate(unused_atoms[::-1]))


def count_graphs(unused_atoms: list[int], unused_connections: list[int]):
    # Index of the first element which is not zero
    idx = 0
    for i in range(4):
        if unused_atoms[i]:
            idx = i
            break
    else:
        return 0

    if len(unused_connections) == 0:
        unused_atoms[idx] -= 1
        return count_graphs(unused_atoms, [4 - idx])

    unused_degrees = get_unused_degrees(unused_atoms)
    sum_unused_connections = sum(unused_connections)
    if unused_degrees < sum_unused_connections:
        # Impossible
        return 0

    if sum(unused_atoms) and sum_unused_connections == 0:
        # Impossible
        return 0

    if sum(unused_atoms) == 1:
        if unused_degrees == sum_unused_connections:
            return 1
        else:
            return 0

    # Recursive
    count = 0
    unused_atoms[idx] -= 1

    # Degree (4 - idx)

    # Case 1: add 1 edge
    len_unused_connections = len(unused_connections)
    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            count += count_graphs(unused_atoms,
                                  unused_connections + [3 - idx])

            unused_connections[i] += 1

    # Case 2: add 2 edges
    if not (idx < 3 and sum_unused_connections > 1):
        unused_atoms[idx] += 1
        return count

    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            for j in range(i, len_unused_connections):
                if unused_connections[j] != 0:
                    unused_connections[j] -= 1

                    count += count_graphs(unused_atoms,
                                          unused_connections + [2 - idx])

                    unused_connections[j] += 1
            unused_connections[i] += 1

    # Case 3: add 3 edges
    if not (idx < 2 and sum_unused_connections > 2):
        unused_atoms[idx] += 1
        return count

    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            for j in range(i, len_unused_connections):
                if unused_connections[j] != 0:
                    unused_connections[j] -= 1

                    for k in range(j, len_unused_connections):
                        if unused_connections[k] != 0:
                            unused_connections[k] -= 1

                            count += count_graphs(unused_atoms,
                                                  unused_connections + [1 - idx])

                            unused_connections[k] += 1
                    unused_connections[j] += 1
            unused_connections[i] += 1

    # Case 4: add 4 edges
    if not (idx < 1 and sum_unused_connections > 3):
        unused_atoms[idx] += 1
        return count

    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            for j in range(i, len_unused_connections):
                if unused_connections[j] != 0:
                    unused_connections[j] -= 1

                    for k in range(j, len_unused_connections):
                        if unused_connections[k] != 0:
                            unused_connections[k] -= 1

                            for l in range(k, len_unused_connections):
                                if unused_connections[l] != 0:
                                    unused_connections[l] -= 1

                                    count += count_graphs(unused_atoms,
                                                          unused_connections + [0])

                                    unused_connections[l] += 1
                            unused_connections[k] += 1
                    unused_connections[j] += 1
            unused_connections[i] += 1

    unused_atoms[idx] += 1
    return count


def count_graphs_with_connections(unused_atoms: list[int], unused_connections: list[int], connections: list[list[int]]):
    # Index of the first element which is not zero
    idx = 0
    for i in range(4):
        if unused_atoms[i]:
            idx = i
            break
    else:
        return 0

    if len(unused_connections) == 0:
        unused_atoms[idx] -= 1
        return count_graphs_with_connections(unused_atoms, [4 - idx], [[]])

    unused_degrees = get_unused_degrees(unused_atoms)
    sum_unused_connections = sum(unused_connections)
    if unused_degrees < sum_unused_connections:
        # Impossible
        return 0

    if sum(unused_atoms) and sum_unused_connections == 0:
        # Impossible
        return 0

    if sum(unused_atoms) == 1:
        if unused_degrees == sum_unused_connections:
            last_connection = []
            for i, j in enumerate(unused_connections):
                for k in range(j):
                    last_connection.append(i)
            print(connections + [last_connection])
            return 1
        else:
            return 0

    # Recursive
    count = 0
    unused_atoms[idx] -= 1

    # Degree (4 - idx)

    # Case 1: add 1 edge
    len_unused_connections = len(unused_connections)
    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            count += count_graphs_with_connections(unused_atoms,
                                                   unused_connections + [3 - idx], connections + [[i]])

            unused_connections[i] += 1

    # Case 2: add 2 edges
    if not (idx < 3 and sum_unused_connections > 1):
        unused_atoms[idx] += 1
        return count

    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            for j in range(i, len_unused_connections):
                if unused_connections[j] != 0:
                    unused_connections[j] -= 1

                    count += count_graphs_with_connections(unused_atoms,
                                                           unused_connections + [2 - idx], connections + [[i, j]])

                    unused_connections[j] += 1
            unused_connections[i] += 1

    # Case 3: add 3 edges
    if not (idx < 2 and sum_unused_connections > 2):
        unused_atoms[idx] += 1
        return count

    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            for j in range(i, len_unused_connections):
                if unused_connections[j] != 0:
                    unused_connections[j] -= 1

                    for k in range(j, len_unused_connections):
                        if unused_connections[k] != 0:
                            unused_connections[k] -= 1

                            count += count_graphs_with_connections(unused_atoms,
                                                                   unused_connections + [1 - idx], connections + [[i, j, k]])

                            unused_connections[k] += 1
                    unused_connections[j] += 1
            unused_connections[i] += 1

    # Case 4: add 4 edges
    if not (idx < 1 and sum_unused_connections > 3):
        unused_atoms[idx] += 1
        return count

    for i in range(len_unused_connections):
        if unused_connections[i] != 0:
            unused_connections[i] -= 1

            for j in range(i, len_unused_connections):
                if unused_connections[j] != 0:
                    unused_connections[j] -= 1

                    for k in range(j, len_unused_connections):
                        if unused_connections[k] != 0:
                            unused_connections[k] -= 1

                            for l in range(k, len_unused_connections):
                                if unused_connections[l] != 0:
                                    unused_connections[l] -= 1

                                    count += count_graphs_with_connections(unused_atoms,
                                                                           unused_connections + [0], connections + [[i, j, k, l]])

                                    unused_connections[l] += 1
                            unused_connections[k] += 1
                    unused_connections[j] += 1
            unused_connections[i] += 1

    unused_atoms[idx] += 1
    return count


def count_molecules(total_atoms):
    if sum(total_atoms[1::2]) % 2:
        return 0
    return count_graphs_with_connections(total_atoms, [], None)


def main():
    # Order: C, N, O, F
    total_atoms = [*map(int, input().split())]
    print(count_molecules(total_atoms))


if __name__ == '__main__':
    main()
