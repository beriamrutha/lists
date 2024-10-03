'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
9)Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''
def count_repeated():
    """
    Count the number of times a given value is repeated in a list.

    Returns:
        int: The number of times the value is repeated.
    """
    lst = list(map(int, input().split()))
    target = int(input())
    count = lst.count(target)

    return count
count = count_repeated()
print(count)
