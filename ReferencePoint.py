

class ReferencePoint:


    InitialRange = InitialRange()
    NumberOfChecks = NumberOfChecks()
    EndRange = InitialRange + NumberOfChecks

    RangeArray = range(Iti)
        
    range(InitialRange,EndRange, 1)

    def __init__(self):
        pass

    def returnRange(self, RangeArray):


class InitilalRange(object):
    
    def __init__(self, InitialRange):
        self.InitialRange = InitialRange
        print('{self.InitialRange} создан')


class NumberOfChecks(object):

    def __init__(self, NumberOfChecks):
        self.NumberOfChecks = NumberOfChecks
        print('{self.NumberOfChecks} создан')
    

NumberOfChecks(input())

