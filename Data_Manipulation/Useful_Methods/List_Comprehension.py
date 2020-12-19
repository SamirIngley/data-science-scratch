# transform a list into another list choosing only certain elements or transforming elements or both

even_numbers = [x for x in range(5) if x % 2 == 0]      # [0, 2, 4]
squares      = [x * x for x in range(5)]                # [0, 1, 2, 4, 9, 16]
even_squares = [x * x for x in range(5) if (x*x)%2 == 0] # [0, 4, 16]
even_squares2= [x * x for x in even_numbers]            # [0, 4, 16]

# can similarly turn lists into dictionaries or sets:

square_dict = {x: x*x for x in range(5)} # {0:0, 1:1, 2:4, 3:9, 4:16}
square_set = [x * x for x in [1, -1]}    # {1}

# ZEROS
zeros = [0 for _ in even_numbers] # has the same length as even_numbers

# can have multiple fors
pairs = [(x,y)
         for x in range(10)
         for y in range(10)] # 100 pairs (0,0)(0,1)...(9,8)(9,9)





if __name__ == "__main__":
    print(even_squares)