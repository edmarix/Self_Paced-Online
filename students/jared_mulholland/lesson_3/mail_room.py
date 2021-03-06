"""
SENDING A THANKYOU
If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    -If the user types ‘list’, show them a list of the donor names and re-prompt--
    -If the user types a name not in the list, add that name to the data structure and use it.--
    -If the user types a name in the list, use it.--
    -Once a name has been selected, prompt for a donation amount.--
    -Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.--
    -Once an amount has been given, add that amount to the donation history of the selected user. -- 
    -Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
    -It is fine (for now) to forget new donors once the script quits running.--
"""

def send_thankyou():
    name = input("Please Enter a Name: ")

    while name == "list":
        print("\n")
        for donor in donors:
            print(donor)
        name = input("\nPlease Enter a Name: ")

    if name not in donors:
        donors.append(name)
        new_donation = input("Enter a Donation Amount: ")
        new_donation = float(new_donation)

        #append new_donation to donations
        donations.append([new_donation])
    
    elif name in donors:
        new_donation = input("Enter a Donation Amount: ")
        new_donation = float(new_donation)

        #append new_donation to donations
        donations[donors.index(name)].insert(0, new_donation)

    thankyou = f"""\nDear {name.split()[0]}, \n\nThank you for your generous donation of ${new_donation:,.2f}. Thanks to you we will finally be able to begin construction 
on the {name.split()[1]} Memorial Children's wing at Dark Place Hospital\n\nYours Truly,\nJared Mulholland"""

    print(thankyou)
    return donors, donations


"""
CREATE A REPORT
If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
"""
import numpy as np

def takeSecond(elem):
    return elem[1]

def create_report():
    rows = []
    for donor in donors:
        rows.append([donor, sum(donations[donors.index(donor)]),len(donations[donors.index(donor)]),np.mean(donations[donors.index(donor)])])

    rows.sort(key = takeSecond, reverse = True)

    print('{:<20s} |{:>15s}|{:>12s} |{:>15s}'.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    for row in rows:
        print('{:<20s} ${:15,.2f} {:12d} ${:15,.2f}'.format(*row))



"""
PROGRAM OVERVIEW
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:\
-It should have a data structure that holds a list of your donors and a history of the amounts they have donated. 
    This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
-You can store that data structure in the global namespace.
-The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
"""

#donors = ['Bill Gates','Mark Zuckerberg','Jeff Bezos','Paul Allen','Mookie Betts']
#donations = [[10000,12000],[20000,150000],[800],[100,500,200],[1000000,1500000,1750000]]

donors = {'Bill Gates': [10000,12000],
                'Mark Zuckerberg':[80000],
                'Jeff Bezos':[30000,75000,35000],
                'Paul Allen': [100000,130000],
                'Mookie Betts': [150000,124000]}

response = input("What would you like to do (enter 'Send a Thank You', 'Create a Report' or 'Quit'): ")

while response.lower().replace(" ","") != 'quit':
    if response.lower().replace(" ","") == 'sendathankyou':
        print('\n')
        send_thankyou()
        response = input("\nWhat would you like to do (enter 'Send a Thank You', 'Create a Report' or 'Quit'): ")
    
    elif response.lower().replace(" ","") == 'createareport':
        print('\n')
        create_report()
        response = input("\nWhat would you like to do (enter 'Send a Thank You', 'Create a Report' or 'Quit'): ")


    



