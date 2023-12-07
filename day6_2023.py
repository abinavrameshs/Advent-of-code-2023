# %%
time_lst =  list(map(int,"62     64     91     90".split()))
distance_lst =   list( map(int, "553   1010   1473   1074".split()))

time_lst, distance_lst
# %%

def calc_wins(t, dis):
    wins = 0
    for hold_time in range(0,t+1):
        speed = hold_time 
        travel_time = t - hold_time
        dist_travelled = travel_time*speed
        if dist_travelled> dis : 
            wins+=1
    return wins


# %%
num_required =1
for i,j in zip(time_lst,distance_lst):
    num_required*=calc_wins(i,j)
num_required
# %%

########### PART 2 #################

t = 62649190
d = 553101014731074

calc_wins(t, d)
# %%
