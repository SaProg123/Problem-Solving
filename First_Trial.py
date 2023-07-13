### 1480. Running Sum of 1d Array
# -------------------------------------
from builtins import list

"""
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sum_li = []
    sum = 0
    for i in nums:
        sum = sum + i
        sum_li.insert(i, sum)

    return sum_li

"""
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = i + 1
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


####1672. Richest Customer Wealth
"""Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""


def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    temp = 0
    list_ou = []
    sum = 0
    for i in accounts:
        for ele in i:
            sum = sum + ele
        list_ou.append(sum)
        sum = 0

    print(list_ou)

    for max in list_ou:
        if max > temp:
            temp = max
        elif max == temp:
            temp = max

    return temp

""" if u  got a number n if divided by  3  append fizz and if dividded by 5 append buzz  if both  append fizzbuzz"""
def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    li_ou = []
    for i in range(1, int(n+1)):
        print(i)

        if i % 3 == 0 and i % 5 == 0 :
            li_ou.insert(i, str("FizzBuzz"))
        elif i % 3 == 0  :
            li_ou.insert(i,str("Fizz"))
        elif i % 5 == 0 and i !=0:
            li_ou.insert(i,str("Buzz"))
        else:
            li_ou.append(str(i))
    return li_ou

#1342. Number of Steps to Reduce a Number to Zero
"""Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
"""


def numberOfSteps( num):
    """
    :type num: int
    :rtype: int
    """
    if  num ==0 :
        return 0
    elif num % 2 ==0 :
        return 1+numberOfSteps(num/2)
    else :return 1+numberOfSteps(num-1)
#876. Middle of the Linked List
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

def count_list(head):
    count=0
    for i in range(1,len(head)):
        #print(i)
        count=i+1
    return count

def middleNode( head):
    new_list=[]
    count= count_list(head)
    if count %2 ==0 :

        midd=count //2

        for midd in range(midd+1,len(head)+1) :
            new_list.append(midd)
        return new_list
    else :
        midd= count //2 + 1
        print(midd)

        for midd in range(midd,len(head)+1):
            new_list.append(midd)
        return new_list



if __name__ == '__main__':
    #print("array_Sum ---> ")
    #print(runningSum([1, 2, 3, 4]))
    #print("indcies_sum_arr ---- > ")
    #print(twoSum([2, 5, 5, 11], 10))
    #print(twoSum([2, 7, 11, 15], 9))
    #print("incies_sum_arr_2 --=====>")
    # print(twoSum2([2, 5, 5, 11], 10))

    #print("Max_Wealth ---- >> ")
    #print(maximumWealth([[1, 2, 3], [3, 2, 1]]))
    #print("FIZZBUZZ ----->>>> ")
    #print(fizzBuzz(15))
    #print(numberOfSteps(123))
    print(middleNode([1,2,3,4,5,6]))
