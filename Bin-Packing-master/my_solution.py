import Driver
def find_solution(sizes):
    sizes = sort_width(addKey(sizes))
    print_10(sizes)
    
def sort_width (sizes):
    """Sorts list acording to width"""
    p = sorted(sizes, key=lambda x: x[1])
    return p


def addKey(sizes):
    """Adds index of original list to keep order"""
    n_sizes = []
    for i in range (0, len(sizes)):
        t_sizes = (i, sizes[i][0], sizes[i][1])
        n_sizes.append(t_sizes)
    return n_sizes

def print_10(list):
    for i in range(0, 10):
        print (list[i])
    
sets = Driver.get_dataset(1)
find_solution(sets[0])

