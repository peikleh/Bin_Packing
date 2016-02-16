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
    print (len(sizes))
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
    curr_y = 0

    while(len(sizes) != 0 and ((sizes[0][2] + curr_y) <= y_max)):
        final_pos.append([sizes[0][0],curr_x, curr_y])
        
        if(sizes[-1][1] <= (hold_width - sizes[0][1])):#check if last box fits in gap
            
            temp_x = curr_x + sizes[0][1]#set start x value of gap
            
            max_y = curr_y + sizes[0][2]#set max y which is the end of the box
            
            gap(temp_x, curr_y, hold_x, max_y)#(start x, start y, final x, final y) dimensions of gap
        curr_y += sizes[0][2]
        sizes.remove(sizes[0])
    fill_y_gap(curr_y, y_max, curr_x)
    return (hold_x)
        
    
def gap (temp_x, temp_y, max_x, max_y):
    """
    Fills any x gap if one exists after a 
    """
    gap_list_len = int(len(sizes)/2)#set size of new list
    y_list = []
    y_list.append(temp_y)
    start_x = temp_x
    
    while(gap_list_len != 0 and ((sizes[-1][1]+ temp_x)<= max_x)):#add boxes from end of the list
        
        new_y = temp_y + sizes[-1][2]#current y of new box
        
        if(new_y <= max_y ):#make sure y does not exceed max y
            
            final_pos.append([sizes[-1][0],temp_x, temp_y])#add the box
            
            temp_x += sizes[-1][1]#update the x
            y_list.append(new_y)
            gap_list_len -= 1
            
            sizes.pop()#remove from our main list
        else:
            break
    temp_y += max(y_list)
    if((sizes[-1][2]+ temp_y)<= max_y):
        gap(start_x, temp_y, max_x, max_y)

        
def fill_y_gap(curr_y, y_max, curr_x):
    """
    Fill the gap between the last box and the y max with the next box that fits. Recursively called
    """
    global sizes
    global final_pos
    plc_hldr = 1
    
    while (plc_hldr < len(sizes) and
           sizes[plc_hldr][2] > (y_max - curr_y)):
        plc_hldr += 1
        
    if(plc_hldr < len(sizes)):
        final_pos.append([sizes[plc_hldr][0], curr_x, curr_y])
        curr_y += sizes[plc_hldr][2]
        sizes.remove(sizes[plc_hldr])
        if((y_max - curr_y) > 0):
            fill_y_gap(curr_y, y_max, curr_x)
    


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

