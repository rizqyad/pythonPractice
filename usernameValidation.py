def usernameValidation(strParam):
    """
    This function will return if a string is an appropriate username or not. 
  
    Parameters:
    strParam (str): username string
  
    Returns:
    str: true if username is appropriate, otherwise false.
  
    """
    slen = len(strParam)
    status = True
    if slen < 4: # minimum username length is 4
        status = False
    if slen > 25: # maximum username length is 25
        status = False
    if not (strParam[0].isalpha()): # username first character must be an alphanumeric 
        status = False
    if not (strParam.replace('_','').isalnum()): # username must only consist of alphanumeric and underscore char
        status = False
    if strParam[slen-1] == '_': # username last character must not an underscore
        status = False

    if status:
        return True
    else:
        return False

if __name__ == "__main__":
    username_list = ['Halimunan_87', '1juara', 'moai_', '@muir9', 'joan#ns', 'aaabcdefghijklmnopqrstuvwxyz', 'kimans']
    for username in username_list:
        validity = "valid" if usernameValidation(username) else "not valid"
        print(f"The username '{username}' is {validity}.")