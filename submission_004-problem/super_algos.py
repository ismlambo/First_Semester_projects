
def find_min(element):
    """TODO: complete for Step 1"""

    """Given a list, this function has to iterate through every element
    and give back(return) the minimum value. 
    it also has to check if the list is empty(and return a -1) or not. 
    Else if the list contains letters or any other characters besides numbers.
    """    
    
    if len(element) == 0:
        return -1
    
    for i in element:
        if str(i).isalpha() == True:
            return -1

    else:
        if len(element) == 1:
            return element[0]
        one_digit = find_min(element[1:])
        minimum = element[0]
        if one_digit < minimum:
            minimum = one_digit
        return minimum
    


def sum_all(element):
    """TODO: complete for Step 2"""

    """Given a list of numbers, this function will calculate a total of all integers
    in the list by adding up all of them but one at a time
    """

    if element == []:
        return -1

    if len(element) == 1:
       return element[0]
    
    for i in element:
        if str(i).isalpha() == True:
            return -1
 
    else:
        return element[0] + sum_all(element[1:])




def combinations(combos,tempArray, character_set, n):

  """this function will be utilised by the function "find_possible_strings"
  which takes only two parameters, hence this function takes 4 parameters
  which will allow us to avoid using global variables to store our 
  different generated combinations of letters or characters.
  """

  if character_set == []:
        return []

  elif len(character_set) == 1:
    return character_set

  else:
    for i in character_set:
      if str(i).isalpha() == False:
        return []

      if len(tempArray) == n:
        combos.append("".join(tempArray))

      else:

        for i in range(0, len(character_set)):
          tempArray.append(character_set[i])
          combinations(combos,tempArray, character_set, n)
          tempArray.pop(len(tempArray) - 1)
      
      return combos

def find_possible_strings(character_set, n):
    """for a list of characters specified, various different combinations of all
    the letters will be created and return(given back).
    """ 
    combos = []
    tempArray = []
    return combinations(combos,tempArray, character_set, n)