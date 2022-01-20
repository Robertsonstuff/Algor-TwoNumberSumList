# 2 for loops - sub optimal - O(n**2) Time, O(1) space

def twoNumberSum(array, targetSum):
    # this function iterates through an array.
    # the for loops will stop after it's gone through the array, in this case, i = 7 times, j = 6
    # the i will start at 3, the j will start at the 5
    # the firstNum and secondNum variables just help you call the value, should you need to find a value.
    # the last piece is the if statement, which adds the target values that we are interating to match it to our target number.
    for i in range(len(array)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return(f"Success!! your target sum is {targetSum}. The numbers{firstNum,secondNum} where found in your list.")
    return("No dice grandma!\nThere wasn't any numbers in this array that matched. ")

result = twoNumberSum([3,5,-4,8,11,-1,6], 10)
print(result)
