inp=input()
in_list=inp.split()
print (in_list)
def median(x):
    sec=float(len(x))
    tot=float(0)
    for i in x:
        i=float(i)
        tot+=i
    med=float(tot/sec)
    #print tot
    #print sec
    return med

print (median(in_list))
print ("\n")
while True:
    fin=(input("Premi invio per chiudere o digita 'again' \n"))
    if fin=="again" or fin=="Again" or fin=="AGAIN":
        inp=input("Digita la sequenza: ")
        in_list=inp.split()
        print (in_list)
        print (median(in_list))
        print ("\n")
    else:
        quit()
