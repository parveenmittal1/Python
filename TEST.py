def count_ones(n):
    CNT = 0;
    while(n>0):
        TEMP = n % 2;
        n = n / 2;
        CNT =CNT+TEMP
    print(CNT)

count_ones(2)