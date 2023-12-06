class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = len(list1) + len(list2)
        list3 = []
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j <= m:
                        if list3 == None:
                            list3.append(list2[j])
                        
                        elif m == i+j:
                            list3.append(list2[j])
                        
                        else:
                            list3.clear()
                            list3.append(list2[j])
                        
                        m = i + j
        return list3