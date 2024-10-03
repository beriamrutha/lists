'''
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
'''
def create_list():
    """
    Create a list of integers based on the user's input.

    Returns:
        list: A list of integers.
    """
    n = int(input())
    lst = []
    for _ in range(n):
        element = int(input())
        lst.append(element)

    return lst
lst = create_list()
print(' '.join(map(str, lst)))
