"""
-Bin packing problem
-Nevin Leh
-Joe Pagina
This solution is a simple way of improving the perimeter by about 95%. We simply sort
the boxes from widest to narrowest. We then place boxes in a top down approach until a
certain y_max is reached. We then start a new column. This ensures that there is no overlap
because the boxes are always getting narrower.
"""
sizes = []
final_pos = []
def find_solution(rectangles):
    global sizes
    global final_pos
    hold_x = 0
    
    sizes = sort_width(addKey(rectangles))#sort by width
    sizes.reverse()
    
    while(len(sizes)!= 0):
        hold_x = place_box(hold_x)#place boxes an update the new x coordinate
        

    
    solution = sorted(final_pos , key = lambda x: x[0])#put back in order
    solution1 = []
    for i in solution:#put in correct format
        del i[0]
        hold = (i[0], i[1])
        solution1.append(hold)
    final_pos = []   
    return solution1
    
        


def place_box(hold_x):
    """
    Place boxes at the hold_x coordinate and increasing y coordinates
    until y_max is reached
    """
    global sizes
    global final_pos
    y_max = 20000
    curr_x = hold_x
    hold_x += sizes[0][1]
    hold_width = sizes[0][1]
    curr_width = hold_width
    curr_y = 0

    while(len(sizes) != 0 and ((sizes[0][2] + curr_y) < y_max)):
        final_pos.append([sizes[0][0],curr_x, curr_y])
        if(sizes[-1][1] <= (hold_width-curr_width)):
            temp_x = curr_x + curr_width
            max_y = curr_y +sizes[0][2]
            gap(temp_x, curr_y, hold_x, max_y)
        curr_y += sizes[0][2]
        curr_width = sizes[0][1]
        sizes.remove(sizes[0])
    
    return (hold_x)
        
    
def gap (temp_x, temp_y, hold_x, max_y):
    gap_list_len = int(len(sizes)/2)
    gap_list = sizes[gap_list_len:]
    while(len(gap_list)!= 0 and (gap_list[-1][1]+ temp_x)< hold_x):
        if(gap_list[-1][2] <= max_y ):
            final_pos.append([sizes[-1][0],temp_x, temp_y])
            temp_x += gap_list[-1][1]
            #temp_y = max(temp_y, (temp_y + gap_list[-1][2])
            gap_list.pop()
            sizes.pop()
        else:
            break    

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
    """
    Print first 10 elements of a list
    """
    for i in range(0, 10):
        print (list[i])
    
#sets = Driver.get_dataset(1)
#find_solution(sets[0])

