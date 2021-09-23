"""
Python program to find the largest element and its location.
"""

def largest_element(a):
    """ Return the largest element of a sequence a.
    """
    maxval = a[0]
    maxloc = 0
    for i in range(1, len(a)):
        if a[i] > maxval:
            maxval = a[i]
            maxloc = i
    if locals == True:
        return maxval, maxloc
    return maxval, maxloc   

if __name__ == "__main__":

    a = [1,1,1,3,5]
    print("Largest element is {:}".format(largest_element(a)))

