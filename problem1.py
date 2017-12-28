"""
Question--Given N integers, count the number of pairs of integers whose
difference is K . The first line contains N and K.
The second line contains N numbers of the set. All the N numbers are unique.
Sample Input 5 2 1 5 3 4 2 Sample Output 3

Answer -- A simple solution is to consider all pairs one by one and check difference
between every pair. Following program implements the simple solution.
We run two loops: the outer loop picks the first element of pair,
the inner loop looks for the other element.
This solution doesn’t work if there are duplicates in array as the requirement
is to count only distinct pairs.
"""

# Solution in Python
n = [5, 2, 1, 5, 3, 4, 2]
k = 3


def countPairsWithDiffK (n, k):
    count = 0
    for i in n:
        for j in range(k):
            if (i - n[j]) == k:  # if (i - n[j]) == k or (n[j] - i) == k: , use as required
                count += 1

    return count


print(countPairsWithDiffK(n, k))
