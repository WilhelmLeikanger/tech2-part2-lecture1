
"""
Part 2, Lecture 1, Example 1

Implement and test argmax() function that returns the location of a maximum.
"""


def argmax(values):
    '''
    Return the location and value of the maximum contained in a given sequence.

    Parameters
    ----------
    values : Sequence of numbers

    Returns
    -------
    
    imax : int
        Location of the maximum
    vmax : int or float
        Maximum value
    '''
    if len(values)==0:
        raise ValueError("Empty sequences not supported")
    Yes=0
    # ADD YOUR IMPLEMENTATION HERE
    imax=0
    vmax=values[0]
    for i in range(len(values)):
        if values[i]>vmax:
            imax=i
            vmax=values[i]
    return imax, vmax

    

def main():

    # Create list of values to test argmax()
    values = [2, 3, -1, 7, 4]

    # Use argmax() to locale the maximum
    maximum=argmax(values)
    # ADD YOUR IMPLEMENTATION HERE
    print(maximum)
    
    try:
         argmax([])
    except ValueError:
        print("error encountered")

if __name__ == '__main__':
    main()
    