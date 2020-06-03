from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import Ticket
from base.views import WinCheck
from base.models import WinningNumbers
from django.http import JsonResponse
import datetime
from collections import Counter

# Create your views here.
@login_required
def home(request):
    user = request.user
    if request.method == "POST":
        WB1 = int(request.POST.get('WB1',None))
        WB2 = int(request.POST.get('WB2',None))
        WB3 = int(request.POST.get('WB3',None))
        WB4 = int(request.POST.get('WB4',None))
        WB5 = int(request.POST.get('WB5',None))
        RB = int(request.POST.get('RB',None))
        DD = request.POST.get('DD',None)
    
        DD = datetime.datetime.strptime(DD, "%Y-%m-%d").date()

        result = ""
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
            print(UserMatch)
            print(RBMatch)
            print(result)
        else:
            result = "Invalid Draw Date!"
        obj = Ticket(WB1=WB1,WB2=WB2,WB3=WB3,WB4=WB4,WB5=WB5,RB=RB,DD=DD,user=user,status=result)
        obj.save()

    tickets = Ticket.objects.all().filter(user=user)
    return render(request,"home/profile.html",{"tickets":tickets})

@login_required
def deleteticket(request,id):
    ticket = Ticket.objects.get(pk=id)
    ticket.delete()
    return redirect("/profile")

@login_required
def statistic(request):
    wlabels = []
    wdata = []
    rdata = []
    rlabels = []
    stats = {}
    rStats = {}
    queryset = WinningNumbers.objects.all()
    for entry in queryset:
        if entry.WB1 in stats:
            stats[entry.WB1] += 1
        else:
            stats[entry.WB1] = 1

        if entry.WB2 in stats:
            stats[entry.WB2] += 1
        else:
            stats[entry.WB2] = 1
        
        if entry.WB3 in stats:
            stats[entry.WB3] += 1
        else:
            stats[entry.WB3] = 1
        
        if entry.WB4 in stats:
            stats[entry.WB4] += 1
        else:
            stats[entry.WB4] = 1
        
        if entry.WB5 in stats:
            stats[entry.WB5] += 1
        else:
            stats[entry.WB5] = 1
        
        if entry.RB in rStats:
            rStats[entry.RB] += 1
        else:
            rStats[entry.RB] = 1

    for x in stats:
        stats[x] = (stats[x] / WinningNumbers.objects.count()) * 100
        
    for x in rStats:
        rStats[x] = (rStats[x] / WinningNumbers.objects.count()) * 100
    
        
    temp = Counter(stats)
    highestwhite = temp.most_common(20)
    temp = Counter(rStats)
    highestred = temp.most_common(20)

    for x in highestwhite:
        wlabels.append(x[0])
        wdata.append(x[1])
    
    for x in highestred:
        rlabels.append(x[0])
        rdata.append(x[1])
    

    return JsonResponse(data={
        'wlabels': wlabels,
        'wdata': wdata,
        'rlabels': rlabels,
        'rdata': rdata
    })