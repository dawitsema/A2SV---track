class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)
        self.freq = defaultdict(set)
        
    def add(self, number: int) -> None:
        prevCount = self.count[number] 
        if number in self.freq[ prevCount ]:
            self.freq[self.count[number]].remove(number)

        self.count[number] += 1
        newCount = prevCount + 1 
        self.freq[newCount].add(number)
        
    def deleteOne(self, number: int) -> None:
        if number in self.freq[ self.count[number] ]:
            self.freq[self.count[number]].remove(number)
        
        if self.count[number]: 
            self.count[number] -= 1
            if self.count[number] == 0: 
                del self.count[number]
            else: 
                newCount = self.count[number]
                self.freq[newCount].add(number) 
    
    def hasFrequency(self, frequency: int) -> bool:
         
        return self.freq[frequency]
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)