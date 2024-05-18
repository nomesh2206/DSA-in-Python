def nearestPerfectSquare(self, n: int) -> int:
        aboveNumber = (math.ceil((n + 1) ** 0.5)) ** 2
        belowNumber = (math.floor((n - 1) ** 0.5)) ** 2
        
        diff_1 = aboveNumber - n
        diff_2 = n - belowNumber
        
        if diff_1 == diff_2:
            return belowNumber
        elif diff_1 < diff_2:
            return aboveNumber
        else:
            return belowNumber
