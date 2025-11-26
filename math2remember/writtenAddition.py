def writtenAddition(summand1, summand2):
    if int(summand1) < 0 or int(summand2) < 0:
        return None
    
    summand1 = str(summand1)
    summand2 = str(summand2)
    
    maxSummand, minSummand = (summand1, summand2) if len(summand1) > len(summand2) else (summand2, summand1)

    acc = 0
    result = ''
    
    for idx, maxNumber in enumerate(reversed(maxSummand)):

        if idx < len(minSummand):
            minNumber = int(minSummand[len(minSummand) - 1 - idx]) 
            curr = int(maxNumber) + minNumber + acc 
        else:
            curr = int(maxNumber) + acc
        result = str(curr%10) + result
        acc = curr // 10
    return result

if __name__ == '__main__':
    print(writtenAddition('28791','568891'))
    
