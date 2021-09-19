import requests,pprint,os
import pandas
import json


def state_data():
    print("\n-----State Data-------\n")
    state_name = str(input("Enter State Name:"))
    cases = parse_json[state_name]['districtData']
    print(f"\t\tAll Cases in {state_name}\t\t\n-")
    pprint.pprint(cases)


def perticular_state():
    print("\n------Perticular State's dictrict------\n")
    state_input = str(input('Enter State Name:'))
    state_name = state_input
    disctrict_input = str(input("Enter Disctrict Name:"))
    disctrict_name = disctrict_input
    cases = parse_json[state_name]['districtData'][disctrict_input]
    print(f"\t\tAll Cases in {state_name}'s {disctrict_name}\t\t\n-")
    pprint.pprint(cases)

def Exit():
    print('Do you really want to exit.')
    print("if YES then type y or Y else you will be returned to the main menu.")
    i = input()
    if i=='Y'or i=="y":
        print("Exiting From Covid Tracker....")
        os._exit(0)
    else:
        main_menu()


def main_menu():
    print('----------------------------------------------------------------------------')
    print('\t\t|---COVID TRACKER---|\n')
    print("\n\t1. Show State's All Cases.\n\t2. Show Perticular Disctrict Cases.\n\t3. Exit.\n")
    choice = int(input("Enter Your Choice  :"))
    if choice == 1:state_data()
    elif choice == 2: perticular_state()
    elif choice == 3: Exit()
    else :print("Invalid Choice")
    print('\n---------------------------------------------------------------------------') 


"""|Main Code|"""

try:
    """Requesting API to get data"""
    response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
    code = response_API.status_code
    if(code != 200):
        print("Server Error\n")
        os._exit(0)
    data = response_API.text
    parse_json = json.loads(data)
    main_menu()
   
except:
    print("\nCan't get Perticular data from the API")
    print("Make sure You have input the write Name of State and District")