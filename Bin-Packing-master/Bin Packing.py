"""
-Bin Packing
-Joe Pagani Hello did the branch work
-Nevin Leh
"""
def find_solution(rectangles):
	global final_posns = []		""" the final list of all rectangles"""
	global x_cor = 0 			""" the x cordinates for each rectangle"""
	global y_cor = 0			""" the y cordinates for each rectangle"""
	
	next_x = 0
	next_y = 0
	
	curr_x = 0
	curr_y = 0
	
	width = []
	width.reverse()				"""prefered width sorted highest to lowest"""
	while(len(width) != 0):
		
		curr_x += place_box()
		
	return (final_posns)

def place_box():
	curr_y = 0
	hold_x = width[0][1]
	while(width[0][0] + curr_y < y_max):	"""y_max determine later"""
		add_box = width[0]
		
		final_posns = [key][curr_y][curr_x]
		
		curr_y += add_box[0]
		
		width.remove(add_box)
		
	return(hold_x)