# import
import sys

# default values
my_alpha, my_beta = -float('inf'), float('inf')


# Calculating Best move
def mab_common(temp_pile_ab_val, pile_color_nums, count_pile, max_bool):
    # global variables
    global my_alpha
    global my_beta
    # loop to iterate 
    for temp_pile_color_num in pile_color_nums:
        if count_pile[ temp_pile_color_num] > 0:

            new_count_pile =  count_pile.copy()

            new_count_pile[ temp_pile_color_num] -= 1

            minmax_val, _ =  mab_func( new_count_pile,  max_bool,  h - 1)
            if max_bool:

                if minmax_val < temp_pile_ab_val:
                    temp_pile_ab_val =  minmax_val

                    temp_best_pile_color_num =  temp_pile_color_num
            else:

                if minmax_val > temp_pile_ab_val:
                    temp_pile_ab_val =  minmax_val

                    temp_best_pile_color_num =  temp_pile_color_num
                    
            my_alpha =  max(my_alpha, temp_pile_ab_val)
            # break condition
            if my_alpha >= my_beta:
                break
    pile_ab_val =  temp_pile_ab_val 

    best_pile_color_num =  temp_best_pile_color_num 

    # final return statement 
    return pile_ab_val, best_pile_color_num

# helper function 1
def mab_helper_1(pile_color_nums, count_pile):
    global my_alpha
    global my_beta

    max_bool =  False

    temp_pile_ab_val =  -float('inf')
    return mab_common( temp_pile_ab_val,  pile_color_nums ,  count_pile, max_bool)

# helper function 2
def mab_helper_2(pile_color_nums, count_pile):
    global my_alpha

    global my_beta


    max_bool =  True
    temp_pile_ab_val =  float('inf')

    return mab_common( temp_pile_ab_val,  pile_color_nums , count_pile, max_bool)

# Min Max Alpla-Beta Pruning
def mab_func(count_pile, max_player_value, h):
    # Return result, if either pile is empty
    if min(count_pile) == 0:
        return (2 * count_pile[0] + 3 * count_pile[1]) * (1 if max_player_value else -1), None
    # setting varaibles 
    best_pile_color_num  =  None

    pile_color_nums =   [0, 1]  


    # Apply min max alpha beta pruning
    if max_player_value:
        pile_ab_val, best_pile_color_num =   mab_helper_1( pile_color_nums  ,  count_pile)
    else:
        pile_ab_val, best_pile_color_num =   mab_helper_2(  pile_color_nums ,   count_pile)


    # final return statement  
    return pile_ab_val, best_pile_color_num

# main function
def main(cr, cb, fp, h):
    # default game
    count_pile = [cr,  cb]


    # Check first player is computer or human 
    if fp not in ('computer', 'human'):

        print("Write valid name human/computer.")
        return
    


    # choose first player
    chance = fp == 'computer'


    # Run till one of the pill will become empty
    while min(count_pile) > 0:
        # printing state
        print("Red -> ",  count_pile[0], "\nBlue -> ",   count_pile[1] ,  "\n")


        if chance:

            # getting details using helper 
            _, pile_color_num =   mab_func( count_pile,  True ,   h)

            count_pile[pile_color_num] -=   1


            # printign the move
            print("Computer removed from - ", end="")

            if pile_color_num == 0:
                print("Red")
            else:
                print("Blue")
        else:

            # taking input
            pile_color_num = input("Your turn - Choose One (red/blue)->").lower()


            # making move
            if pile_color_num == 'red' and count_pile[0] > 0:
                count_pile[0] -=   1
            elif pile_color_num == 'blue' and count_pile[1] > 0:
                count_pile[1] -=   1
            else:
                # writing invalid condition
                print("Write properly (red/blue). Try Again.")
                continue


        # changing player
        chance = not chance


    # Winner Declaration
    winner = "Computer" if chance else "Human"


    score = 2 * count_pile[0] + 3 * count_pile[1]

    print(" Winner ->",   winner, "\tPoints Won By ->",   score)

# running main
if __name__ == "__main__":

    # picking command line arguments

    cr =  int(sys.argv[1])

    cb =  int(sys.argv[2])


    # deciding first player
    if len(sys.argv) >= 4 and sys.argv[3].lower() == "human":
        fp =  "human"
    else:
        fp =  "computer"


    # picking depth
    if len(sys.argv) >= 5:
        h =   int(sys.argv[4])
    else:
        h =  0


    # making the main function run
    main(cr, cb, fp, h)
