def intfactorial(num):
    """
    This function will return the factorial of input integer. 
  
    Parameters:
    num (int): input integer
  
    Returns:
    int: factorial of input.
  
    """
    result = 1
    while num > 0:
        result *= num
        num -= 1

    return result

if __name__ == "__main__":
    int_list = [0 , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print()
    for i_int in int_list:
        print(f"Factorial of {i_int} is {intfactorial(i_int)}")
    print()
