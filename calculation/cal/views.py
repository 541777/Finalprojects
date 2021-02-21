from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime
import re



def home(request):
    return render(request,'home.html')



def add(request):

    policynumber =request.POST['num1']
    policystart = request.POST['sdate']
    policypermium =(request.POST['pamt'])
    policymembership = request.POST['mship']
    policyuplift = (request.POST['percentage'])


    date_verification = time(policystart)

    policynumber_verficiation = polnumber(policynumber)

    permium_verficiation = polpermium(policypermium)

    membership_verfication = polmembership(policymembership)

    uplift_verficitation = poluplift(policyuplift)



    print(date_verification)
    print(policynumber_verficiation)
    print(permium_verficiation)
    print(membership_verfication)
    print(uplift_verficitation)
    print(len(policynumber))


    if((date_verification and policynumber_verficiation and permium_verficiation and membership_verfication and uplift_verficitation)==True):
        policy_managementfee = 0
        if (policynumber[0] == "A"):
            policy_managementfee = (calmanagement(0.03, (policypermium)))
        elif (policynumber[0] == "B"):
            policy_managementfee = (calmanagement(0.05, (policypermium)))
        elif (policynumber[0] == "C"):
            policy_managementfee = (calmanagement(0.07, (policypermium)))

        polstartdate = policystart
        policy_discretionary = Discretionarybonus(polstartdate, policynumber, policymembership)

        policy_uplift_percentage = caluplift(policyuplift)

        policy_maturity = ((float(
            policypermium) - (policy_managementfee)) + policy_discretionary) * policy_uplift_percentage
        return render(request, 'home.html',
                      {'result': policynumber, 'result2': policystart, 'result3': policypermium,
                       'result4': policymembership,
                       'result5': policyuplift, 'result6': policy_maturity})


    else:
        print("else part")
        m = "Give proper values"
        return render(request, 'home.html',
                      {'result': policynumber, 'result15': m})



def time(date1):

    k= False
    if (date1 == ' '):
      return k
    else:
        print("hiiifgfedgdfsdfse")
        inputDate = date1
        day, month, year = inputDate.split('/')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if (isValidDate):
            return True
        else:
            return False


def polnumber(policynumber1):
    regex = '^[0-9]+$'

    policynumber = policynumber1

    if (len(policynumber) != 0):

        if (policynumber[0] == 'A' and re.search(regex, policynumber[1:7])):
            return True
        elif (policynumber[0] == 'B' and re.search(regex, policynumber[1:7])):
            return True
        elif (policynumber[0] == 'C' and re.search(regex, policynumber[1:7])):
            return True
        else:
            print("inside")
            return False
    else:
        print("outside")
        return False

def polpermium(policypermium):
    regex = '^[0-9]+$'

    policypermium = policypermium

    if (re.search(regex, policypermium)):
        return True
    else:
        return False


def polmembership(policymembership1):
    y = policymembership1

    if (y == 'yes' or y == 'no'):
        return True
    else:
        return False


def poluplift(policyuplift1):
    regex = '^[0-9]+$'

    policypermium = policyuplift1

    if (re.search(regex, policypermium)):
        return True
    else:
        return False



def calmanagement(polmanagementfee, polpermium):
    return polmanagementfee * float(polpermium)

def Discretionarybonus(policystartdate, policynum, policymember):
        policydetails = policynum
        policymem = policymember
        if ((policydetails[0] == "A") and (policystartdate[6:10] < '1990')):
            Discretionary = 1000
        elif ((policydetails[0] == "B") and (policymem == "yes")):
            Discretionary = 1000
        elif ((policydetails[0] == "C") and (('1990' <= policystartdate[6:10]) and (policymem == "yes"))):
             Discretionary = 1000
        else:
             Discretionary = 0

        return Discretionary

def caluplift(policyup):

    if (policyup != ''):
       k = int(policyup)
       upamt1 = k / 100
       upamt2 =1
       upamt =  upamt1+ upamt2
       return upamt
    else:
        return ''




