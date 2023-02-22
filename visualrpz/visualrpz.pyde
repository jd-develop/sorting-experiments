from random import shuffle

original_list = [i for i in range(100)]
shuffle(original_list)
sorted_list = list(original_list)
sorted_count = -1
sorting = True
width_unit = height_unit = 0
delay(100)

BUBBLE = False
SELECTION = True
BOZO = False


def setup():
    global width_unit, height_unit
    size(900, 650)
    # frameRate(999999)
    width_unit = width//len(original_list)
    height_unit = height//max(original_list)


def update_view(list_):
    clear()
    for i in range(len(list_)):
        rect(i*width_unit, height, width_unit, -list_[i]*height_unit)


def draw():
    global sorted_list, sorting, sorted_count
    update_view(sorted_list)
    
    if sorting:
        if BUBBLE:
            if sorted_count == -1:
                sorted_count = 0
            # BUBBLE SORT
            swapped = False
            for i in range(len(sorted_list) - sorted_count - 1):
                if sorted_list[i] > sorted_list[i+1]:
                    sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
                    swapped = True
            
            if not swapped:  # the list is sorted
                sorting = False
            
            if sorted_count < len(sorted_list):
                sorted_count += 1
            else:
                sorting = False
        elif SELECTION:
            # SELECTION SORT
            if sorted_count+1 < len(sorted_list):
                sorted_count += 1
                
                lowest_i = sorted_count
                for check_i in range(sorted_count + 1, len(sorted_list)):
                    if sorted_list[check_i] < sorted_list[lowest_i]:
                        lowest_i = check_i
                sorted_list[sorted_count], sorted_list[lowest_i] = sorted_list[lowest_i], sorted_list[sorted_count]
            else:
                sorting = False
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
    
    delay(100)
