
#basic mergesort routine to merge a set of numbers
class mergeSorter:
    def mergeSort(self,initialList):
        return self.split(initialList)
    
    def split(self,initialList):
        if(len(initialList) < 2):
            return initialList
        middle = int(len(initialList)/2)
        leftcount = 0
        leftList = []
        rightcount = middle
        rightList = []
        while leftcount < middle:
            leftList.append(initialList[leftcount])
            leftcount = leftcount +1
        while rightcount < len(initialList):
            rightList.append(initialList[rightcount])
            rightcount = rightcount +1
        leftList = self.split(leftList)
        rightList = self.split(rightList)
        return self.merge(leftList,rightList)

    def merge(self,left,right):
        returnList = []
        while len(left) > 0 or len(right) > 0:
            if(len(left)>0 and len(right) > 0):
                if(left[0] <= right[0]):
                    returnList.append(left[0])
                    left = left[1:]
                else:
                    returnList.append(right[0])
                    right = right[1:]
            else:
                if(len(left)>0):
                    returnList.append(left[0])
                    left = left[1:]
                else:
                    if(len(right)>0):
                        returnList.append(right[0])
                        right = right[1:]
        return returnList

