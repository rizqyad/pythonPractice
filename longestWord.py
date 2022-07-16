def longestWord(strParam):
    """
    This function will return the first longest word in a string. It only count alphanumeric characters.
  
    Parameters:
    strParam (str): input string
  
    Returns:
    str: longest word in input string
  
    """
    wordList = strParam.split()
    longestWord = 0
    longest = 0
    for i in range(len(wordList)):
        word = wordList[i]
        filteredWord = ''.join(filter(str.isalnum, word))
        if len(filteredWord) > longest:
            longest = len(filteredWord)
            longestWord = i
    
    return wordList[longestWord]

if __name__ == "__main__":
    string_list = ['I go to the mall', "Let's have a wonderfull dinner!!!!!!", "Good rain"]
    for i_string in string_list:
        print(f"The longest word in string '{i_string}' is '{longestWord(i_string)}'.")