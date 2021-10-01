import requests,pprint,os,pyfiglet,json
import pandas as pd
from pandasgui import show


def state_data():
    print("\n-----State Data-------\n")
    state_name = str(input("Enter State Name:"))
    # cases = parse_json[state_name]['districtData']
    print(f"\t\tAll Cases in {state_name}\t\t\n-")
    # pprint.pprint(cases)
    url = requests.get("https://api.covid19india.org/state_district_wise").json()
    name  = state_name
    for name in url[state_name]:

        active_cases = url[state_name]["districtData"]['active']
        confirmed_cases = url[state_name]["districtData"]['confirmed']
        recovered_cases = url[state_name]["districtData"]['recovered']
        deceased_cases = url[state_name]["districtData"]['deceased']
        print(name,active_cases,confirmed_cases,recovered_cases,deceased_cases)



def perticular_state():
    print("\n------Perticular State's dictrict------\n")
    state_input = str(input('Enter State Name:'))
    state_name = state_input
    district_input = str(input("Enter Disctrict Name:"))
    district_name = district_input
    url = requests.get("https://data.covid19india.org/state_district_wise.json").json()
    active_cases = url[state_name]["districtData"][district_input]['active']
    confirmed_cases = url[state_name]["districtData"][district_input]['confirmed']
    recovered_cases = url[state_name]["districtData"][district_input]['recovered']
    deceased_cases = url[state_name]["districtData"][district_input]['deceased']
    # total_cases = active_cases + recovered_cases + deceased_cases
    df = pd.DataFrame(columns=["District","Active","Deceased","Recovered"])
    df = df.append({'District': district_name,
                "Active":active_cases,
                "confirmed":confirmed_cases,
                "Deceased":deceased_cases,
                "Recovered":recovered_cases,
                },ignore_index=True)
    show(df)
    return main_menu()


def Exit():
    print('Do you really want to exit.')
    print("if YES then type y or Y else you will be returned to the main menu.")
    i = input()
    if i=='Y'or i=="y":
        print("Exiting From Covid Tracker....")
        os._exit(0)
    else:
        main_menu()
def all_india():
    """Requesting API to get data"""
    url = requests.get("https://disease.sh/v3/covid-19/countries/India?strict=true").json()
    name  = url['country']
    active_cases = url['active']
    total_death = url["deaths"]
    total_cases = url["cases"]
    total_recovered = url["recovered"]
    critical_cases = url["critical"]

    df = pd.DataFrame(columns=["Country","Total Cases","Active","Critical","Deaths","Recovered"],)
    df = df.append({'Country':name,
                "Total Cases":total_cases,
                "Active":active_cases,
                "Critical":critical_cases,
                "Deaths":total_death,
                "Recovered":total_recovered},ignore_index=True,)
    show(df,)
    return main_menu()

    
def total_doses_in_state():
    # url = "https://api.covid19india.org/state_district_wise.json"
    # response_API = requests.get(url)
    print("fdhfufdf")


def total_doses_in_country():
    url = "https://api.covid19india.org/state_district_wise.json"
    response_API = requests.get(url)
    pprint.pprint(response_API.text)

def main_menu():
    print('-------------------------------------------------------------------------')
    print("\t  C O V I D   T R A C K E R \n\n")
    print("\t\t-MAIN MENU-")
    print("\n\t1. State's All Cases.\n\t"
    "2. Perticular Disctrict Cases.\n\t"
    "3. All India State's Cases\n\t"
    "4. total doses in state.\n\t"
    "5. total doses in Country.\n\t"
    "6. Exit.\n\t")
    print('\n-----------------------------------------------------------------------')
    choice = int(input("Enter Your Choice  :"))
    while(choice):
        if choice == 1:state_data()
        elif choice == 2: perticular_state()
        elif choice == 3: all_india()
        elif choice == 4: total_doses_in_state()
        elif choice == 5: total_doses_in_country() 
        elif choice == 6: Exit()
        else :print("Invalid Choice")
     


"""|Main Code|"""

try:
    """Requesting API to get data"""
    url = "https://api.covid19india.org/state_district_wise.json"
    response_API = requests.get(url)
    code = response_API.status_code
    if(code != 200):
        print("Server Error\n")
        os._exit(0)
    data = response_API.text
    parse_json = json.loads(data)
    main_menu()
   
except:
    print("\nCan't get Perticular data from the API")
    print("Make sure You have input the write Name of State and District.")
    print("Your State or District name's First letter should ")