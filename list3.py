'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
'''
def find_largest():
    """
    Find the largest number in a list of integers.

    Returns:
        int: The largest number in the list.
    """
    n = int(input())
    lst = []
    for _ in range(n):
        element = int(input())
        lst.append(element)
    return max(lst)
largest = find_largest()
print(largest)
