def reverseString(thestr):
    """
    This function will output the reverse of the inputed string.
    
    Parameters:
    thestr (str): string to be reveresed
  
    Returns:
    newstr (str): reversed string 
  
    """
    strl = list(thestr)
    newstr = ''
    for i in range(1, len(strl)+1):
        newstr += strl[-i]

    return newstr


if __name__ == "__main__":
    mystring = 'Good Job'
    print(reverseString(mystring))