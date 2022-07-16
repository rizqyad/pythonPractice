def questionsMarks(strParam): 
    """
    This function will return if a string contain three question mark between two pair of single digit number that sum to 10. 
  
    Parameters:
    strParam (str): input string
  
    Returns:
    str: true if there are three question mark between two pair of single digit number that sum to 10, otherwise false.
  
    """

    idxs = [idx for idx in range(len(strParam)) if strParam[idx].isdigit()] # get all number position in the string
    if len(idxs) <= 1: # if there is less than 1 number in the string
        return False
    tenTotal = False # initialize variable to monitor the sum of number pairs
    for id in range(1,len(idxs)):
        prev_idx = idxs[id-1] # first number
        curr_idx = idxs[id] # second number

        if int(strParam[prev_idx])+int(strParam[curr_idx]) == 10: # check if number pairs sum is equal to 10
            tenTotal = True # set true because the number pairs sum is equal 10
            qmark = strParam[prev_idx:curr_idx].count('?') # count the number of question mark between number pairs
            if qmark != 3: # check if question mark appear three times
                return False # return false because question mark does not appear three times

    return True if tenTotal else False # return true if number pairs sum is equal to 10 otherwise, false.
    
# keep this function call here 
if __name__ == "__main__":
    string_list = ['aa6?9', 'acc?7??sss?3rr1??????5']
    print("There are three question mark between two number pairs that sum to 10. ")
    for i_string in string_list:
        print(f"{i_string} : {questionsMarks(i_string)}")
