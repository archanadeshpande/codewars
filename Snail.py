
"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

def snail(snail_map):
    start,end,path,j,chg,stance, snail = 0, 0,[],0,1,'right',[]
    length=len(snail_map)
    iterate=(length + (length-1))
    if not any(snail_map):
        return []
    #print(start,end,path,iterate)
    else:
        for i in range(iterate):
            #print(start,end)
            while (start in range(0,length) and end in range(0, length)) and [start,end] not in path:
                #print('inside while loop')
                path.append([start,end])
                #print(path)
                snail.append(snail_map[start][end])
                #print(snail)
                if stance=='right' and end < length-1 and [start,end+chg] not in path:
                    end+=chg
                    if end == -1:
                        end=0
                if stance=='left' and start < length-1 and [start+chg,end] not in path:
                    start+=chg
                    if start == -1:
                        start =0
            #print(f'after while loop:stance:{stance} i {i} chg: {chg}, start: {start}, end:{end} ')    
            j+=1
            if j==2 and chg==1:
                j=0
                chg=-1
            elif j==2 and chg==-1:
                j=0
                chg=1
            if stance=='right':
               stance='left'   
               start+=chg
            elif stance=='left':  
               stance='right'
               end+=chg
            
        return(snail)