Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.
Example:
Input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
Hint:
    By default of sorted is ASC . reverse=True will sort DES
    Need to sort h ASC and k DES so need -k to sort DES. 
    Ex: [7,2],[7,1]. if - sign, will be -2, -1 then sort ASD will be 2, 1
   (iteration, key=keyFunction, reverse=False)
    Given: [[7,0], [4,4], [7,1], [5,0], [6,1],[5,2]]
 sorted  = [[7,0], [7,1], [6,1], [5,0], [5,2],[4,4]]

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        x = sorted(people, key= lambda (h,k): (h, -k), reverse=True)
        output = []
        for h,k in x:
            output.insert(k, (h,k))
        return output
         
