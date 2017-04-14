"""
@author = gauravmokhasi
This is a program to help sync a video and its respective .srt file
It works when there is a fixed delay throughout the video
The user is required to enter file name and value of the delay required in ms
"""
def syncSubs(c):
    """
    function that fixes subtitle delay
    c = [['h1', 'm1', 's1,ms1'], ['-->'], ['h2', 'm2', 's2,ms2']]
    eg. [['0', '44', '32,513'], ['-->'], ['0', '44', '33,570']]
    """
    for ele in c:
        if ele == ['-->']:
            continue
        else:
            scount = int(ele[2].split(",")[0])
            mscount = int(ele[2].split(",")[1])
            mscount+=ms
            scount+=mscount/1000 + s
            mscount%=1000
            if mscount:
                while mscount < 100:
                    mscount*=10
                m = scount/60
                scount%=60
                ele[2]=str(scount)+","+str(mscount)
                mcount = int(ele[1]) + m
                hcount = int(ele[0]) + mcount/60
                mcount%=60
                ele[1]=str(mcount)
                ele[0]=str(hcount)

req_file = raw_input("Enter filename without extension: ")+".srt"

delay = int(raw_input("Enter Subtitle delay in ms: "))
#splitting delay into seconds and milliseconds
s= delay/1000
ms= delay%1000

f_old = open(req_file, 'r')
x=f_old.readlines()

f_new= open(req_file, 'w') # output file

for line in x:
    line1=line
    temp1 = ""
    if "-->" in line: # assuming "-->" will not appear in dialogue
        b = line.split()
        # b = ['h1:m1:s1,ms1', '-->', 'h2:m2:s2,ms2']
        # eg. ['0:44:0,382', '-->', '0:44:1,334']
        c = []
        for val in b:
            c.append(val.split(':'))
        syncSubs(c) # calling function that fixes subtitle delay
        for val in c:
            x = ""
            for temp in val:
                x += temp + ":"
            x=x.strip(':')
            # x will be either h:m:s,ms or -->, blocks of 3 x's make 1 time row
            temp1 = (temp1 + x + " ")
        temp1 = temp1.strip(" ")+'\n'
        # temp1 = 'h1:m1:s1,ms1 --> h2:m2:s2,ms2'; eg. 0:46:50,234 --> 0:46:52,674
        line1 = temp1
    f_new.write(line1)

f_old.close()
f_new.close()
