'''
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
'''
def separate_even_odd():
    """
    Separate the even and odd elements in a list into two different lists.

    Returns:
        list, list: Two lists, one containing even numbers and the other containing odd numbers.
    """
    n = int(input())
    even_lst = []
    odd_lst = []
    for _ in range(n):
        element = int(input())
        if element % 2 == 0:
            even_lst.append(element)
        else:
            odd_lst.append(element)

    return even_lst, odd_lst
even_lst, odd_lst = separate_even_odd()
print("The even list", even_lst)
print("The odd list", odd_lst)
