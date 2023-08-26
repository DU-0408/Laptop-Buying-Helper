import pandas as p, numpy as n, matplotlib.pyplot as pl, time
df1 = p.read_csv('Specs.csv')
df2 = p.read_csv('Customers.csv')
df3 = p.read_csv('Sales.csv')
df4 = p.read_csv('Feedbacks.csv')
while True:
    print('''
                 MENU

                 1. Admin
                 2. Customer
                 3. Exit
    ''')
    ch = input('Enter your choice: ')
    if ch not in '123':
        print('Invalid Choice. Please try again!!!')
        time.sleep(0.5)
        input('Press Enter key to continue!!!')
        print('*'*90)
    elif ch == '1':
        print('''
                 Admin Portal
                 
                 1. Display the dataframe
                 2. Adding a New Record
                 3. Delete a Existing Record
                 4. Update a Existing Record
        ''')
        ch = input('Enter your choice: ')
        if ch not in '1234':
            print('Invalid Choice. Please enter again!!!')
            time.sleep(0.5)
            input('Press Enter Key to continue!!!')
            print('*'*90)
        elif ch == '1':
            a = input('''Which dataframe you want to see?
                        1. Specs
                        2. Sales
                        3. Customers
                        4. Feedbacks''')
            if a == 'Specs':
                print(df1)
            elif a == 'Customers':
                print(df2)
            elif a == 'Sales':
                print(df3)
            elif a == 'Feedbacks':
                print(df4)
            else:
                print('Invalid choice. Please try again!!!')
                time.sleep(1)
                input('Press Enter key to continue...')
                print('*'*80)
                time.sleep(1)
        elif ch == '2':
            print('''
                In which file do you want to add the record?
                              1. Specs
                              2. Customers
                              3. Sales
                              4. Feedbacks
            ''')
            ch = input('Enter your choice: ')
            if ch not in '1234':
                print('Invalid Choice. Please try again')
                time.sleep(0.5)
                input('Press Enter Key to continue!!!')
                print('*'*90)
            elif ch == '1':
                print('''
                      Where do you want to add the record?
                      1. After the last record in the file
                      2. In between any two records
                ''')
                ch = input('Enter your choice: ')
                if ch not in '12':
                    print('Invalid Choice. Please try again!!!')
                    time.sleep(0.5)
                    input('Press Enter Key to continue!!!')
                    print('*'*90)
                elif ch == '1':
                    print('''
                       Adding a Record
                    ''')
                    LapID = input('Enter the Laptop ID:')
                    CN = input('Enter the Company Name: ')
                    Mod = input('Enter the Model: ')
                    RAM = input('Enter the amount of RAM: ')
                    St = int(input('Enter the amount of storage of the laptop: '))
                    Co = int(input('Enter the number of cores: '))
                    PC = input('Enter the Name of the Company of Processor: ')
                    PS = input('Enter the speed of Processor: ')
                    OS = input('Enter the Operating System which it has: ')
                    SS = input('Enter the size of the screen: ')
                    DT = input('Enter the type of Drive: ')
                    We = input('Enter the wheight of the laptop: ')
                    Po = int(input('Enter the number of ports: '))
                    Cond = input('Enter the condition of the laptop: ')
                    Up = input('Enter the Price of the Laptop: ')
                    a = len(df1)+1
                    df1.loc[a] = [LapID,CN,Mod,RAM,St,Co,PC,PS,OS,SS,DT,We,Po,Cond,Up]
                    print('Yay! Your record is inserted.')
                    a = input('To see the dataframe please enter Y else enter N: ')
                    if a in 'Yy':
                        print(df1)
                        time.sleep(1)
                        input('Press Enter key to continue!!!')
                        print('*'*80)
                    elif a in 'Nn':
                        print('Thank You!!!')
                        print('*'*80)
                        time.sleep(1)
                elif ch == '2':
                    LapID = input('Enter the Laptop ID:')
                    CN = input('Enter the Company Name: ')
                    Mod = input('Enter the Model: ')
                    RAM = input('Enter the amount of RAM: ')
                    St = int(input('Enter the amount of storage of the laptop: '))
                    Co = int(input('Enter the number of cores: '))
                    PC = input('Enter the Name of the Company of Processor: ')
                    PS = input('Enter the speed of Processor: ')
                    OS = input('Enter the Operating System which it has: ')
                    SS = input('Enter the size of the screen: ')
                    DT = input('Enter the type of Drive: ')
                    We = input('Enter the wheight of the laptop: ')
                    Po = int(input('Enter the number of ports: '))
                    Cond = input('Enter the condition of the laptop: ')
                    Up = input('Enter the Price of the Laptop: ')
                    a = int(input('Enter the place where you want to insert the record: '))
                    if a not in len(df1):
                        print('Invalid Input. Length is more than the length of the dataframe. Please Retry')
                    elif a in len(df1):
                        df1.iloc[a-1] = [LapID,CN,Mod,RAM,St,Co,PC,PS,OS,SS,DT,We,Po,Cond,Up]
                        print('Yay! The record is inserted')
                        a = input('To see the dataframe please enter Y else enter N: ')
                        if a in 'Yy':
                            print(df1)
                            time.sleep(1)
                            input('Press Enter key to continue!!!')
                            print('*'*80)
                        elif a in 'Nn':
                            print('Thank You!!!')
                            print('*'*80)
                            time.sleep(1)
            elif ch == '2':
                print('''
                      Where do you want to add the record?
                      1. After the last record in the file
                      2. In between any two records
                ''')
                ch = input('Enter your choice: ')
                if ch not in '12':
                    print('Invalid Choice. Please try again!!!')
                    time.sleep(0.5)
                    input('Press Enter Key to continue!!!')
                    print('*'*90)
                elif ch == '1':
                    CID = input('Enter the Customer ID: ')
                    CA = input('Enter the Customer Address: ')
                    Aa = input('Enter the Aadhar No.: ')
                    Em = input('Enter the Email ID.: ')
                    Mo = input('Enter the Mobile No.: ')
                    a = len(df2)+1
                    df2.loc[a] = [CID,CA,Aa,Em,Mo]
                    print('Yay! Your record is inserted.')
                    a = input('To see the dataframe please enter Y else enter N: ')
                    if a in 'Yy':
                        print(df2)
                        time.sleep(1)
                        input('Press Enter key to continue!!!')
                        print('*'*80)
                    elif a in 'Nn':
                        print('Thank You!!!')
                        print('*'*80)
                        time.sleep(1)
                elif ch == '2':
                    CID = input('Enter the Customer ID: ')
                    CA = input('Enter the Customer Address: ')
                    Aa = input('Enter the Aadhar No.: ')
                    Em = input('Enter the Email ID.: ')
                    Mo = input('Enter the Mobile No.: ')
                    a = int(input('Enter the place where you want to insert the record: '))
                    if a not in len(df2):
                        print('Invalid Input. Length is more than the length of the dataframe. Please Retry!!!')
                        time.sleep(1)
                    elif a in len(df2):
                        df2.iloc[a-1] = [CID,CA,Aa,Em,Mo]
                        print('Yay! Your record is inserted.')
                        a = input('To see the dataframe please enter Y else enter N: ')
                        if a in 'Yy':
                            print(df2)
                            time.sleep(1)
                            input('Press Enter key to continue!!!')
                            print('*'*80)
                        elif a in 'Nn':
                            print('Thank You!!!')
                            print('*'*80)
                            time.sleep(1)
            elif ch == '3':
                print('''
                      Where do you want to add the record?
                      1. After the last record in the file
                      2. In between any two records
                ''')
                ch = input('Enter your choice: ')
                if ch not in '12':
                    print('Invalid Choice. Please try again!!!')
                    time.sleep(1)
                    input('Press Enter Key to continue!!!')
                    print('*'*90)
                elif ch == '1':
                    BNo = input('Enter the Bill No.: ')
                    CID = input('Enter the Customer ID: ')
                    PD = input('Enter the Purchase Date: ')
                    Di = input('Enter the Discount: ')
                    GST = input('Enter the GST: ')
                    Qty = int(input('Enter the quantity: '))
                    Amt = input('Enter the amount of Laptop: ')
                    a = len(df3)+1
                    df3.loc[a] = [BNo,CID,PD,Di,GST,Qty,Amt]
                    print('Yay! Your record is inserted.')
                    a = input('To see the dataframe please enter Y else enter N: ')
                    if a in 'Yy':
                        print(df3)
                        time.sleep(1)
                        input('Press Enter key to continue!!!')
                        print('*'*80)
                    elif a in 'Nn':
                        print('Thank You!!!')
                        print('*'*80)
                        time.sleep(1)
                elif ch == '2':
                    BNo = input('Enter the Bill No.: ')
                    CID = input('Enter the Customer ID: ')
                    PD = input('Enter the Purchase Date: ')
                    Di = input('Enter the Discount: ')
                    GST = input('Enter the GST: ')
                    Qty = int(input('Enter the quantity: '))
                    Amt = input('Enter the amount of Laptop: ')
                    a = int(input('Enter the place where you want to insert the record: '))
                    if a not in len(df3):
                        print('Invalid Input. Length is more than the length of the dataframe. Please Retry!!!')
                    elif a in len(df3):
                        df3.iloc[a-1] = [BNo,CID,PD,Di,GST,Qty,Amt]
                        print('Yay! Your record is inserted.')
                        a = input('To see the dataframe please enter Y else enter N: ')
                        if a in 'Yy':
                            print(df3)
                            time.sleep(1)
                            input('Press Enter key to continue!!!')
                            print('*'*80)
                        elif a in 'Nn':
                            print('Thank You!!!')
                            print('*'*80)
                            time.sleep(1)
            elif ch == '4':
                print('''
                      Where do you want to add the record?
                      1. After the last record in the file
                      2. In between any two records
                ''')
                ch = input('Enter your choice: ')
                if ch not in '12':
                    print('Invalid Choice. Please try again!!!')
                    time.sleep(1)
                    input('Press Enter Key to continue!!!')
                    print('*'*90)
                elif ch == '1':
                    CID = input('Enter the Customer ID: ')
                    LID = input('Enter the Laptop ID: ')
                    Re = input('Enter the review of the Laptop: ')
                    BR = input('Enter the Brand Ratings: ')
                    OR = input('Enter the OS Ratings: ')
                    PR = input('Enter the Processor Ratings: ')
                    SR = input('Enter the Speed Ratings: ')
                    BaR = input('Enter the Battery Ratings: ')
                    WR = input('Enter the Weight Ratings: ')
                    DR = input('Enter the Drive Ratings: ')
                    a = len(df4)+1
                    df4.loc[a] = [CID,LID,Re,BR,OR,SR,BaR,WR,DR]
                    print('Yay! The record is inserted')
                    a = input('To see the dataframe please enter Y else enter N: ')
                    if a in 'Yy':
                        print(df4)
                        time.sleep(1)
                        input('Press Enter key to continue!!!')
                        print('*'*80)
                    elif a in 'Nn':
                        print('Thank You!!!')
                        print('*'*80)
                        time.sleep(1)
                elif ch == '2':
                    CID = input('Enter the Customer ID: ')
                    LID = input('Enter the Laptop ID: ')
                    Re = input('Enter the review of the Laptop: ')
                    BR = input('Enter the Brand Ratings: ')
                    OR = input('Enter the OS Ratings: ')
                    PR = input('Enter the Processor Ratings: ')
                    SR = input('Enter the Speed Ratings: ')
                    BaR = input('Enter the Battery Ratings: ')
                    WR = input('Enter the Weight Ratings: ')
                    DR = input('Enter the Drive Ratings: ')
                    a = int(input('Enter the place where you want to insert the record: '))
                    if a not in len(df4):
                        print('Invalid Input. Length is more than the length of the dataframe. Please Retry!!!')
                    elif a in len(df4):
                        df4.loc[a-1] = [CID,LID,Re,BR,OR,SR,BaR,WR,DR]
                        print('Yay! The record is inserted')
                        a = input('To see the dataframe please enter Y else enter N: ')
                        if a in 'Yy':
                            print(df4)
                            time.sleep(1)
                            input('Press Enter key to continue!!!')
                            print('*'*80)
                        elif a in 'Nn':
                            print('Thank You!!!')
                            print('*'*80)
                            time.sleep(1)
                    
        elif ch == '2':
            print()
            
        elif ch == '3':
            print()
            
    elif ch == '2':
        print()
        
    elif ch == '3':
        break
print('Thank you!!!')
        
            

        
