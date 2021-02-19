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
    policypermium =request.POST['pamt']
    policymembership = request.POST['mship']
    policyuplift = int(request.POST['percentage'])

    '''    time           '''

    date_verification = time(policystart)

    '''  policy number'''

    policynumber_verficiation = polnumber(policynumber)


    ''' policy permium'''

    permium_verficiation = polpermium(policypermium)


    '''  policy membership  '''

    membership_verfication = polmembership(policymembership)


    '''  policy uplift '''

    uplift_verficitation = poluplift(policyuplift)












def time(date1):

    inputDate = date1

    day, month, year = inputDate.split('/')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if (isValidDate):
        print("Input date is valid ..")
    else:
        print("Input date is not valid..")


def polnumber(policynumber1):


    regex = '^[0-9]+$'

    policynumber = 'A123456'

    if (policynumber[0] == 'A' and re.search(regex, policynumber[1:7])):
        print("inside")

    else:
        print("outside")
        print(re.search(regex, policynumber[1:7]))



def polpermium(policypermium):
    regex = '^[0-9]+$'

    policypermium = '10000'

    if (re.search(regex, policypermium)):
        print("inside")
    else:
        print("no")


def polmembership(policymembership1):
    y = 'yes'

    if (y == 'yes' or y == 'no'):
        print("inside")
    else:
        print("outside")


def poluplift(policyuplift):
    regex = '^[0-9]+$'

    policypermium = ''

    if (re.search(regex, policypermium)):
        print("inside")
    else:
        print("no")

    '''
        

    policy_managementfee = 0
    if (policynumber[0] == "A"):
        policy_managementfee =(calmanagement(0.03, float(policypermium)))
    elif (policynumber[0] == "B"):
        policy_managementfee =(calmanagement(0.05,float(policypermium)))
    elif (policynumber[0] == "C"):
            policy_managementfee =(calmanagement(0.07,float(policypermium)))

    polstartdate = policystart
    policy_discretionary = Discretionarybonus(polstartdate, policynumber, policymembership)

    policy_uplift_percentage = caluplift(policyuplift)

    policy_maturity = ((float(policypermium) - policy_managementfee) + policy_discretionary) * policy_uplift_percentage
    return render(request, 'home.html',
                      {'result': policynumber, 'result2': policystart, 'result3': policypermium, 'result4': policymembership,
                       'result5': policyuplift, 'result6': policy_maturity})



def calmanagement(polmanagementfee, polpermium):
    return polmanagementfee * polpermium

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
    k = int(policyup)
    upamt1 = k / 100
    upamt2 =1
    upamt =  upamt1+ upamt2

    return upamt


'''