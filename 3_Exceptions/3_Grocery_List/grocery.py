#Loop
    # Get Input (to UPPER)
    # APPEND to list
    # CTRL-Z to exit
# PRINT list with items in alphabetical order
    # Once per (remove dupes)
# Add the number of items in front

def main():
    g_list = []
    w_bool = True
    while w_bool == True:
        try:
            item = input().upper()
            g_list.append(item)
        except EOFError:
            w_bool =  False

    #print(f"----- {g_list}")

    mod_list(g_list)

    #print(g_list)



def mod_list(ml):
    r_list = []
    ml.sort()

    for i in ml:
        num_i = ml.count(i)
        if (f"{num_i} {i}") not in r_list:
            r_list.append(f"{num_i} {i}")

    #print(r_list)

    for t in r_list:
        print(t)




main()
