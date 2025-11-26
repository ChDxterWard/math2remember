def writtenAddition(summand1, summand2):
    try:
        if int(summand1) < 0 or int(summand2) < 0:
            return None
    except (ValueError, TypeError):
        return None
    
    summand1 = str(summand1)
    summand2 = str(summand2)
    
    max_len = max(len(summand1), len(summand2))
    # Fill with 0 until max_len
    summand1 = summand1.zfill(max_len)
    summand2 = summand2.zfill(max_len)
    
    acc = 0
    result = ''
    
    # From left to right [max_len, 0] 
    for i in range(max_len - 1, -1, -1):
        curr = int(summand1[i]) + int(summand2[i]) + acc
        result = str(curr % 10) + result
        acc = curr // 10
    
    # Add spare acc.
    if acc > 0:
        result = str(acc) + result
    
    return result
if __name__ == '__main__':
    pass
