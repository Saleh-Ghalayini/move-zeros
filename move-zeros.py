#defining a function called move_zeros
def move_zeros(numbers):
    
    #will be counting the appearances of zeros in the list and storing them in the zeros_counter
    zeros_counter = 0
    #this will store the non zero numbers at first then all the zeros will get appended to it after that
    zeros_moved_numbers = []

    #going through the whole numbers list to check all the numbers
    for i in range(len(numbers)):
        #the counter will be added by 1 every time the number is a 0 
        if(numbers[i] == 0):
            zeros_counter += 1
        #adding the non zero numbers to the new list made
        else:
            zeros_moved_numbers.append(numbers[i])
    #appending all the zeros seen according to the counter to the end of the list
    for i in range(zeros_counter):
        zeros_moved_numbers.append(0)
    
    print(zeros_moved_numbers)
#sending the numbers_list to the move_zeros to ughhhh move zeros maybe ?? :)
numbers_list = [0,1,2,3,0,5,00,2]
move_zeros(numbers_list)
    