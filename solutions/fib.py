# recurrence relation - define a term in a seq wrt to the value(s) of the previous term(s).

# fibonacci's rabbits
# any given month = prev month + new off spring (duh)
# any given month's num of off spring = num of rabbits alive two months prior

# F_{n} = num of rabbit *pairs* alive after the n-th month.
# F_{n} = F_{n-1} + F_{n+2} (F_1 = F_2 = 1 to init)

# given pos int n<=40, k <=5
# return total num of rabbit pairs that will be present after n months

# begin : 1 pair
# each gen: every pair of reproduction-age rabbits produces a litter of k rabbit pairs
# (instead of only one pair)

def rabbits(n, k):
    # start = [1,1]
    #return start + [rabbits(i-1, k) + (k*rabbits(i-2, k)) for i in range(2, n)]
    # works but is slow
    start = [1,1]
    for i in range(2,n):
        start.append(start[i-1] + (k*start[i-2]))
    return start[-1]