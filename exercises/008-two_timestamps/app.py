def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here   
    time1 = hr1 * 3600
    time1 += min1 * 60
    time1 += sec1

    time2 = hr2 * 3600
    time2 += min2 * 60
    time2 += sec2

    
    return time2 - time1


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
