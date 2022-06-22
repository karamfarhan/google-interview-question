s1 = [["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
t1 = ["9:00","20:00"]


s2 = [["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]
t2 = ["10:00","18:30"]

mt = 30


output = [["11:30","12:00"],["15:00","16:00"],["18:00","18:30"]]


#? helper function
## To Convert an string-time to how much minute is equal . e.g --> "20:00" = 1200
def str_to_min(time):
    hour,minute = time.split(":")
    time_in_minute = (int(hour)*60) + int(minute)
    return time_in_minute


## This code will:
## 1) mereging the tow lists of schedul times
## 2) converting the string-times to minute . e.g --> "20:00" == 1200
## 3) sorting the merged list
nat = sorted([[ str_to_min(start), str_to_min(end)] for start,end in s1+s2])



## This code will merege the tow lists into one list means one or both of the persons are poked in this time
## e.g Input  = [[540, 630], [600, 690], [720, 780], [750, 870], [870, 900], [960, 1020], [960, 1080]]
##     output = [[540, 690], [720, 900], [960, 1080]]
nb = 0
while nb < len(nat)-1:
    # geting the end-time for the first block and the start-time for the second block
    end1 = nat[nb][1]
    start2 = nat[nb+1][0]
    # getting the end-time for the second block
    end2 = nat[nb+1][1]
    #(@1)
    # if the end-time for the first block is == to the start time of the second block
    # that means the tow blocks of time are connected(it mens there is not free time between the tow blocks)
    # so we will take the start-time for the first block and the end-time for the second block and merege them in one block
    # after that we will delete the second block 
    if end1 == start2:
        nat[nb][1] = end2
        nat.pop(nb+1)
        nb-=1
    # elif the end-time for the first block is greater than start-time of the second block that is mean alos we don't have free time between them
    # so we can merege them 
    elif end1 > start2:
        # but if the end-time for the second block is less than the end-time for the first block 
        # that is mean we don't need for the whole second block because the (peroid)-time of second-block is inside the (period)-time of the first block
        # so we just delete the second block
        if end2 < end1:
            nat.pop(nb+1)
            # and here we have to (minas) one from the index because after we got new block(we mereged the first one and the second one)
            # we have to also check the times between new block and the second one after it
            nb-=1
        # elif the end-time of the second block is greater than the end-time of the first block
        # that's mean we can merege them because the end-time of the first block is crossing the start-time of the second one     
        elif end2 > end1:
            # so we can change the end-time of the first block to the end-time of the second block after that we delete the second block
            # it's the same like the first (condetion) when we have the end-time and the start-time  similar ot each other LOOK TO (@1)
            nat[nb][1] = end2
            nat.pop(nb+1)
            nb-=1
    nb+=1


"""
This is the main code 

"""
valid_minute = []

for i in range(1441): # the day is 24 hours and each hour is 60 minute so we have 1440 minute in the day
    # Here i will check if this minute is not between the work time of both persons 
    # that's mean this minute of the day is with is the work time for the both persons 
    if (i >= str_to_min(t1[0]) and i >= str_to_min(t2[0])) and (i <= str_to_min(t1[1]) and i <= str_to_min(t2[1])):
        valid = True # default value of the minute is True
        for tm1 in nat : # after that i have to check minute is within the time when one of persons is bussy 
            if i > tm1[0] and i < tm1[1]: # if it is between the the time of when they are bussy
                valid = False # i will not take it becuse it is not valid minute
        
        if valid: # if the valid is still True that mean this minute is valid and it's free time for both of the persons
            valid_minute.append(i) # so i will append it to the valid minute (free-time minute)
            # print(get_miltary_time_from_minute(i))

## To This point if i you print the (valid_minute) list you will a list of all  availabe minute to make meetting for both of them
# print(valid_minute)

#########################

## but if you want to convert this availabe and free minute to a readable format uncomment this code

#? helper funcion
## To Get the miltary time from number of given minutes . e.g --> 1200 = "20:00"
def get_miltary_time_from_minute(minute):
    return f"{minute//60}:{minute%60 if len(str(minute%60))>1 else f'0{minute%60}' }"


final_nat = []
for inx,min in enumerate(valid_minute):
    if inx == 0 or inx+1 == len(valid_minute):
        final_nat.append(get_miltary_time_from_minute(min))
    if inx+1 < len(valid_minute):

        if min+1 == valid_minute[inx+1]:
            continue
        else:
            final_nat.append(get_miltary_time_from_minute(min))
            final_nat.append(get_miltary_time_from_minute(valid_minute[inx+1]))

print(final_nat)

