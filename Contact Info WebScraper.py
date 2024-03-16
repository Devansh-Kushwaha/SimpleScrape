import urllib.request
website=input("Enter the website to be searched: ")
response=urllib.request.urlopen(website)
htmlSource = str(response.read())
cp=0
ce=0
for i in range(0,len(htmlSource)):

    if (htmlSource[i:i+5]=="Phone"):
        n=0
        while htmlSource[i+5+n].isnumeric()==0:
            n=n+1
        if n>5:
            break
        cp=1
        print("Phone Number: ",end="")
        
        while htmlSource[i+5+n].isnumeric()==1 or htmlSource[i+5+n]=="-":
            print(htmlSource[i+5+n],end="")
            n=n+1
        print("\n")
    if (htmlSource[i:i+5]=="Email"):
        n=0
        mail=""
        while htmlSource[i+5+n].isalnum()==0:
            n=n+1
        

        while htmlSource[i+5+n] not in [" ","<","\\"]:
            
           mail=mail+htmlSource[i+5+n]
           n=n+1
        for i in mail:
            if i=="@":
                ce=1
                print("Email ID: ",end="")
                print(mail,"\n")
                
if cp==0:
    print("Phone number NOT FOUND!!")
if ce==0:
    print("Email ID NOT FOUND!!")
    
