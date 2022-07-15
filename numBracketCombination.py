from math import factorial

def countBraComb(num):
    """
    This function will return the number of possible combination of bracket form by the number of brucket inputed
  
    Parameters:
    num (int): number of bracket
  
    Returns:
    int: number of possible bracket combination
  
    """
    return int(factorial(2*num)/(factorial(num+1)*factorial(num)))


if __name__ == "__main__":
    number_of_bracket = 5
    number_of_possible_combination = countBraComb(number_of_bracket)
    print(f"There are {number_of_possible_combination}  combinations that can be generated using {number_of_bracket} brackets.")