# Basic_problems
# Problem1.py
Question-- Given N integers, count the number of pairs of integers whose difference is K . The first line contains N and K. The second line contains N numbers of the set. All the N numbers are unique. Sample Input 5 2 1 5 3 4 2 Sample Output 3

Answer-- A simple solution is to consider all pairs one by one and check difference between every pair. Following program implements the simple solution. We run two loops: the outer loop picks the first element of pair, the inner loop looks for the other element. This solution doesn’t work if there are duplicates in array as the requirement is to count only distinct pairs.
