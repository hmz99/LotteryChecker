from django.shortcuts import render
from .models import WinningNumbers
from contextlib import closing
import csv 
import requests
import datetime 

# Create your views here.
def index(request):
    if request.method =="GET":

        # Update the database using the lottery csv.
        url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"
        with closing(requests.get(url, stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            reader = csv.reader(f, delimiter=',', quotechar='"')
            counter = 0
            for row in reader:
                if counter == 0: #Skip header line
                    counter += 1
                    continue 
                date = row[0]
                date = datetime.datetime.strptime(date, "%m/%d/%Y").date()
                numbers = row[1]
                numbers = numbers.split()
                numbers = list(map(int,numbers))
                RB = row[2]
                WB1,WB2,WB3,WB4,WB5 = numbers
                obj,created = WinningNumbers.objects.get_or_create(
                    WB1=WB1,
                    WB2=WB2,
                    WB3=WB3,
                    WB4=WB4,
                    WB5=WB5,
                    RB=RB,
                    DD=date)
                obj.save()

        return render(request,'base/index.html')
    else:
        # The user is posting data. Grab all of it and check!
        WB1 = int(request.POST.get('WB1',None))
        WB2 = int(request.POST.get('WB2',None))
        WB3 = int(request.POST.get('WB3',None))
        WB4 = int(request.POST.get('WB4',None))
        WB5 = int(request.POST.get('WB5',None))
        RB = int(request.POST.get('RB',None))
        DD = request.POST.get('DD',None)
    
        DD = datetime.datetime.strptime(DD, "%Y-%m-%d").date()

        result = ""
        # Check if draw date is correct and return result as context
        if WinningNumbers.objects.filter(DD=DD).exists():
            Numbers = WinningNumbers.objects.get(DD = DD)
            LNumbers = [Numbers.WB1,Numbers.WB2,Numbers.WB3,Numbers.WB3,Numbers.WB4,Numbers.WB5]
            UserMatch = []
            RBMatch = False
            if WB1 in LNumbers:
                UserMatch.append(WB1)
            if WB2 in LNumbers:
                UserMatch.append(WB2)
            if WB3 in LNumbers:
                UserMatch.append(WB3)
            if WB4 in LNumbers:
                UserMatch.append(WB4)
            if WB5 in LNumbers:
                UserMatch.append(WB5)
            if Numbers.RB == RB:
                RBMatch = True 
            result = WinCheck(UserMatch,RBMatch)
        else:
            result = "Invalid Draw Date!"
        return render(request,'base/results.html',{'result':result})


# Function to check the status of a ticket.
def WinCheck(UserMatch,RBMatch):
    if len(UserMatch) == 5 and RBMatch == True:
        return "Congratulations! You have won the jackpot!"
    if len(UserMatch) == 5 and RBMatch == False:
        return "Congratulations! You matched all 5 White Balls!"
    if len(UserMatch) >= 1 and RBMatch == True:
        return "Congratulations! You matched {0} White Balls and the Mega Ball!".format(len(UserMatch))
    if len(UserMatch) >= 3 and RBMatch == False:
        return "Congratulations! You matched {0} White Balls!".format(len(UserMatch))
    if len(UserMatch) == 0 and RBMatch == True:
        return "Congratulations! You matched the Mega Ball!"
        
    return "Unfortunately you didn't win this time! Better luck next time!"

