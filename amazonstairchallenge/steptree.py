import pprint


class StepTree(object):
    """
        The purpose of this program is to find the number of unique ways you can climb a stair case taking 1 or 2 steps
        at a time.
        For example, if N is 4, then there are 5 unique ways to climb the stairs:
                        1, 1, 1, 1
                        2, 1, 1
                        1, 2, 1
                        1, 1, 2
                        2, 2
                        
        The design behind this was inspired after drawing a tree that represents the possible paths available
        starting from the the top of the stairs to the bottom. The number found in each node of the tree represents
        the number of available steps left. each '/' or '\' represents a path to take, the negative number next to it
        represents the action take at that step--in this case the number of steps taken. leaf nodes with 0 steps
        remaining implies a valid path sequence was found while leaf nodes with value -1 represent invalid path sequences.
        
        
        The program uses recursion to simulate tree navigation without actually going through the process of creating a
        tree data structure. The program does not consider left paths from nodes that have less than two steps remaining.
        
        
                                  (# starting steps) 3
                    (two steps taken)      -2 /            \ -1  (1 step taken)
               (#steps after 2 steps taking) 1             2  (#steps remaining after 1 step taking)
                                         -2 / \ -1    -2 /   \ -1
                     (invalid step seq)  -1   0         0    1
                                                          -2/ \ -1
                                                         -1    0
                           
    """
    
    def __init__(self):
        self.solutions = dict()
        self.solution_count = 0
    
    def run(self, num_of_steps):
        print("Number of stairs to climb: ", num_of_steps)
        self.step_tree(num_of_steps, [])
        print("Number of solutions ", self.solution_count)
        pprint.pprint(self.solutions)
    
    def step_tree(self, steps_left, parent_sequence):
        if steps_left == 0:
            self.solutions[self.solution_count] = parent_sequence
            self.solution_count += 1
        if steps_left > 1:
            left_list = list(parent_sequence)
            left_list.append(2)
            self.step_tree(steps_left - 2, left_list)
        if steps_left > 0:
            right_list = list(parent_sequence)
            right_list.append(1)
            self.step_tree(steps_left - 1, right_list)