from random import shuffle, randint

# Things you can change 
mode = ["LINEAR", "RANDOMIZED"][0]
lenght = 50
algorithm = ["bubble", "selection", "bozo"][1]

# Initialize the list
if mode == "LINEAR":
    original_list = [i for i in range(lenght)]
    shuffle(original_list)  # randomize
else:
    original_list = [randint(0, lenght) for i in range(lenght)]

sorted_list = list(original_list)

# Initialize useful stuff
sorted_count = 0
sorting = True
what_to_do_next = "comparing"
context = []
check_i = 0

BUBBLE = algorithm == "bubble"
SELECTION = algorithm == "selection"
BOZO = algorithm == "bozo"

width_unit = height_unit = 0
delay(100)


def setup():
    global width_unit, height_unit, algorithm
    # window size
    size(900, 650)
    # frame rate
    frameRate(100)
    # width and height of the rectangles
    width_unit = width//len(original_list)
    height_unit = height//max(original_list)
    background(0)


def update_view(list_):
    """Update graphics"""
    global context
    clear()
    background(0)
    for i in range(len(list_)):
        if len(context) >= 1 and i == context[0]:
            fill(255, 0, 0)
        elif len(context) >= 2 and i == context[1]:
            fill(0, 255, 0)
        elif len(context) >= 3 and i == context[2]:
            fill(0, 0, 255)
        rect(i*width_unit, height, width_unit, -list_[i]*height_unit)
        fill(255)


def draw():
    global sorted_list, sorting, sorted_count, what_to_do_next, context, check_i
    update_view(sorted_list)
    
    if sorting:
        if BUBBLE:
            # BUBBLE SORT
            if what_to_do_next == "comparing":
                finish = True
                increment_sorted_count = True
                temp_list = list(sorted_list)
                for i in range(len(temp_list) - sorted_count - 1):
                    if temp_list[i] > temp_list[i+1]:
                        what_to_do_next = "swapping"
                        temp_list[i], temp_list[i+1] = temp_list[i+1], temp_list[i]
                        context.append(i)
                        context.append(i+1)
                        finish = False
                        if i != len(temp_list) - sorted_count - 2:
                            increment_sorted_count = False
                        break
                
                if finish:  # the list is sorted
                    sorting = False
                
                if sorted_count < len(sorted_list) and increment_sorted_count:
                    sorted_count += 1
                elif sorted_count > len(sorted_list):
                    sorting = False
            else:
                while len(context) != 0:
                    sorted_list[context[0]], sorted_list[context[1]] = sorted_list[context[1]], sorted_list[context[0]]
                    context = context[2:]
                what_to_do_next = "comparing"
        elif SELECTION:
            # SELECTION SORT
            if what_to_do_next == "comparing":
                if sorted_count+1 < len(sorted_list):
                    lowest_i = sorted_count
                    next_is_swap = False
                    if len(context) == 3:
                        lowest_i = context[1]

                    if sorted_list[check_i] < sorted_list[lowest_i]:
                        lowest_i = check_i
                    if check_i >= len(sorted_list)-1:
                        next_is_swap = True
                    
                    context = [sorted_count, lowest_i, check_i]
                    if next_is_swap:
                        sorted_count += 1
                        what_to_do_next = "swapping"
                        check_i = sorted_count+1
                    else:
                        check_i += 1
                else:
                    sorting = False
            else:
                while len(context) != 0:
                    sorted_list[context[0]], sorted_list[context[1]] = sorted_list[context[1]], sorted_list[context[0]]
                    context = context[3:]
                what_to_do_next = "comparing"
        elif BOZO:
            # BOZO SORT
            sorted_ = True
            for i in range(len(sorted_list)-1):
                if sorted_list[i] > sorted_list[i+1]:
                    sorted_ = False
            if sorted_:
                sorting = False
            else:
                shuffle(sorted_list)
    
    delay(25)
