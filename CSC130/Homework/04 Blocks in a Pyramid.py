#########################################################################
# name: Caleb Matherne
# date: 10/16/2021
# description: Blocks in a Pyramid Program
#########################################################################

# A function to prompt the user for the number of levels that their
# pyramid will have and return it to the calling statement.

def prompt_layers():
    return int(input("How many levels will your pyramid have? "))



# A function that receives the number of pyramid levels and the number
# of blocks as arguments, and prints the appropriate results to the
# screen.

def results(l, b):
    print(f"For {l} levels, you will need {b} blocks")

    

# A recursive function that receives the number of the level, calculates
# the number of blocks required, and returns the result to the calling
# statement.

def block_count(n):
    if n == 1:
        return n
    else:
        return (n)**2 + block_count(n-1)

    
    

################################ MAIN ################################
# using the function(s) defined above, ask the user for the number of
# pyramid levels

layers = prompt_layers()



# using the function(s) defined above, calculate and display the final results

results(layers,block_count(layers))

