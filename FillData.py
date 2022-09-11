def FillData(df):
    import pandas as pd
    import numpy as np

    #occupation
    df.loc[(df["occupation"] == "SHOPPING MALL") | (df["occupation"] == "JEWELLERY SHOP") | (
                        df["occupation"] == "GOLD SHOP") | (df["occupation"] == "Business") | (
                        df["occupation"] == "BUSINESS MAN") | (df["occupation"] == "BUSINESSMAN") | (
                        df["occupation"] == "BUISNESS(FISH)") | (df["occupation"] == "H.BUSINESS") | (
                        df["occupation"] == "PHUCHKA BUSINESS") | (
                        df["occupation"] == "GOLD SHOP OWNER"), "occupation"] = "BUSINESS"
    df.loc[(df["occupation"] == "5") | (df["occupation"] == "ALLUMINIUM") | (df["occupation"] == "FOOD SERVICE") | (
                df["occupation"] == "CAR SERVICE") | (df["occupation"] == "HOSIERY") | (
                       df["occupation"] == "MARBEL SHOP") | (df["occupation"] == "Phuchka Business ") | (
                       df["occupation"] == "SAREE BUSINESS") | (df["occupation"] == "GROCERY TRANSPORT") | (
                       df["occupation"] == "FOOD BUSINESS") | (df["occupation"] == "TRAVEL BUSINESS") | (
                       df["occupation"] == "ONLINE BUISNEESS") | (df["occupation"] == "BUISNESS") | (
                       df["occupation"] == "WATER BUSINESS") | (df["occupation"] == "BUSINESS") | (
                       df["occupation"] == "HOTEL"), "occupation"] = "BUSINESS"

    df.loc[(df["occupation"] == "7") | (df["occupation"] == "NURSE") | (df["occupation"] == "DOCTOR") | (
                df["occupation"] == "3") | (df["occupation"] == "DESHBANDHU HOSPITAL") | (
                       df["occupation"] == "HEALTH") | (df["occupation"] == "DOCTOR CHAMBER") | (
                       df["occupation"] == "HOSPITAL") | (df["occupation"] == "DOCTOR ") | (
                       df["occupation"] == "DOCTOR,S HELPER") | (df["occupation"] == "DENTIST") | (
                       df["occupation"] == "MEDICAL REPRESENTATIVE") | (df["occupation"] == "HOMEOPATHY DOCTOR") | (
                       df["occupation"] == "HOMEOPATHY DOCTOR"), "occupation"] = "HEALTH PROFESSIONALS"

    df.loc[(df["occupation"] == "PO") | (df["occupation"] == "POURA SABHA") | (df["occupation"] == "KP") | (
                df["occupation"] == "15") | (df["occupation"] == "C.G.EMP") | (df["occupation"] == "BSF") | (
                       df["occupation"] == "G.S.I") | (df["occupation"] == "S.A.I") | (df["occupation"] == "SAI") | (
                       df["occupation"] == "MTS") | (df["occupation"] == "ENGINEERING SERVICE") | (
                       df["occupation"] == "CORPORATION") | (df["occupation"] == "AGRICULTURAL ENGINEER") | (
                       df["occupation"] == "CONDUCTOR") | (df["occupation"] == "BUS CONTRUCTOR") | (
                       df["occupation"] == "MUNICIPALITY") | (df["occupation"] == "LIC") | (
                       df["occupation"] == "BUS CONDUCTOR") | (df["occupation"] == "PENSION") | (
                       df["occupation"] == "INCOME TAX") | (df["occupation"] == "CRPF") | (
                       df["occupation"] == "AIR CIVIL") | (df["occupation"] == "BSNL") | (
                       df["occupation"] == "POST OFFICE JOB") | (df["occupation"] == "CBI") | (
                       df["occupation"] == "INDIAN ARMY") | (df["occupation"] == "DEFENCE") | (
                       df["occupation"] == "CPWD") | (df["occupation"] == "SURVEY OF INDIA EMPLOYEE") | (
                       df["occupation"] == "Government Job") | (df["occupation"] == "GOVERNMENT") | (
                       df["occupation"] == "GOVERNMENT JOB") | (df["occupation"] == "GOVERNMENT SERVICE") | (
                       df["occupation"] == "OFFICER") | (df["occupation"] == "POST OFFICER") | (
                       df["occupation"] == "INCOME TAX OFFICER") | (df["occupation"] == "POLICE") | (
                       df["occupation"] == "BANKER") | (df["occupation"] == "BANK") | (
                       df["occupation"] == "BANK EMPLOYEE") | (df["occupation"] == "GOVT JOB") | (
                       df["occupation"] == "BANK MANAGER") | (df["occupation"] == "BANK JOB") | (
                       df["occupation"] == "GOVT  JOB") | (df["occupation"] == "GOVT EMPLOYEE") | (
                       df["occupation"] == "CENTRAL GOVT EMP") | (df["occupation"] == "BANKS") | (
                       df["occupation"] == "GOVT") | (df["occupation"] == "GOVT. JOB") | (
                       df["occupation"] == "GOVT SERVICE") | (
                       df["occupation"] == "GOVT RETIRED OFFICER"), "occupation"] = "GOVT EMPLOYEE"

    df.loc[(df["occupation"] == "2") | (df["occupation"] == "5/R") | (df["occupation"] == "LDC") | (
                df["occupation"] == "BPO") | (df["occupation"] == "6") | (df["occupation"] == "WORK FROM HOME") | (
                       df["occupation"] == "1") | (df["occupation"] == "MANAGER") | (
                       df["occupation"] == "CHOREOGRAPHER SCHOOL") | (df["occupation"] == "JOB ( cashier)") | (
                       df["occupation"] == "COMPANY") | (df["occupation"] == "JOB") | (df["occupation"] == "LAWYER") | (
                       df["occupation"] == "TCS JOB") | (df["occupation"] == "COMPUTER PROGRAMMER") | (
                       df["occupation"] == "EMPLOYEE") | (df["occupation"] == "SERVICE CENTER JOB") | (
                       df["occupation"] == "TCS") | (df["occupation"] == "FLIPKANT") | (
                       df["occupation"] == "BATA EMPLOYEE") | (df["occupation"] == "OFFICE") | (
                       df["occupation"] == "CONTRACTER") | (df["occupation"] == "CONTRACTOR") | (
                       df["occupation"] == "PROCESS MANAGEMENT") | (df["occupation"] == "IT") | (
                       df["occupation"] == "ELECTRIC ENGINEER") | (df["occupation"] == "BUILDING CONTRACTOR") | (
                       df["occupation"] == "IT") | (df["occupation"] == "SERVICE CENTER EMPLOYEE") | (
                       df["occupation"] == "SERVICE MANAGER") | (df["occupation"] == "COGNIZANT") | (
                       df["occupation"] == "P.JOB") | (df["occupation"] == "ENGINEER") | (
                       df["occupation"] == "IT ENGINEER") | (df["occupation"] == "ADVOCATE") | (
                       df["occupation"] == "OFFICE JOB") | (df["occupation"] == "IT PROFESSIONAL") | (
                       df["occupation"] == "Private Employee") | (df["occupation"] == "PRIVATE SERVICE") | (
                       df["occupation"] == "PRIVATE JOB") | (df["occupation"] == "PVT OFFICE") | (
                       df["occupation"] == "PVT JOB") | (df["occupation"] == "PVT EMPLOYEE") | (
                       df["occupation"] == "PRIVATE COMPANY EMPLOYEE")| (
                       df["occupation"] == "P"), "occupation"] = "PVT EMPLOYEE"

    df.loc[(df["occupation"] == "B REDIMATE") | (df["occupation"] == "8") | (df["occupation"] == "SERVICE") | (
                df["occupation"] == "MARKET GD") | (df["occupation"] == "SERVICES") | (
                       df["occupation"] == "GENERAL") | (df["occupation"] == "BUILDER") | (
                       df["occupation"] == "SELF EMPLOYED") | (df["occupation"] == "SALOON") | (
                       df["occupation"] == "PRESS COMPANY") | (df["occupation"] == "CIBER CAFE") | (
                       df["occupation"] == "CYBERCAFE") | (df["occupation"] == "CATERER") | (
                       df["occupation"] == "GROCERY") | (df["occupation"] == "MARBLE") | (
                       df["occupation"] == "MARBEL ") | (df["occupation"] == "ANIMATION FREELANCING") | (
                       df["occupation"] == "BUS OWNER") | (df["occupation"] == "CANTEEN") | (
                       df["occupation"] == "SALON OWNER") | (df["occupation"] == "FISHERY BUSINESS") | (
                       df["occupation"] == "B STATIONARY") | (df["occupation"] == "WHOLESELLER") | (
                       df["occupation"] == "MEDICAL SHOP OWNER") | (df["occupation"] == "ELECTRIC SHOP") | (
                       df["occupation"] == "GROCERY SHOP OWNER") | (df["occupation"] == "CHICKEN SHOP") | (
                       df["occupation"] == "CYCLE SHOP") | (df["occupation"] == "MARBLE SHOP") | (
                       df["occupation"] == "CLOTHE SHOP") | (df["occupation"] == "FRUIT SHOP") | (
                       df["occupation"] == "BOOK SHOP") | (df["occupation"] == "SHOPKEEPER") | (
                       df["occupation"] == "PHOTOGRAPHY SHOP OWNER") | (df["occupation"] == "Medicine shop") | (
                       df["occupation"] == "FURNITURE SHOP") | (df["occupation"] == "MOBILE SHOP") | (
                       df["occupation"] == "BOOK SHOP OWNER") | (df["occupation"] == "BEAUTY PARLOUR OWNER") | (
                       df["occupation"] == "APOLLO MEDICINE SHOP") | (df["occupation"] == "FLOWER SHOP") | (
                       df["occupation"] == "FISH SHOP") | (df["occupation"] == "MEDICINE SHOP") | (
                       df["occupation"] == "TEA SHOP") | (df["occupation"] == "SHOP") | (
                       df["occupation"] == "PARLOUR") | (df["occupation"] == "GARMENT SHOP") | (
                       df["occupation"] == "GROCERY SHOP") | (df["occupation"] == "SHOP OWNER") | (
                       df["occupation"] == "FLOWER SHOP OWNER") | (df["occupation"] == "SHOP KEEPER") | (
                       df["occupation"] == "SMALL HOTEL") | (df["occupation"] == "FLOWER SHOP OWNER") | (
                       df["occupation"] == "PHOTO STUDIO") | (
                       df["occupation"] == "LABORATORY"), "occupation"] = "SMALL BUSINESS"

    df.loc[(df["occupation"] == "NGO ") | (df["occupation"] == "16") | (df["occupation"] == "14") | (
                df["occupation"] == "12") | (df["occupation"] == "13") | (df["occupation"] == "11") | (
                       df["occupation"] == "9") | (df["occupation"] == "10") | (
                       df["occupation"] == "HAND GLOVES MAKER") | (df["occupation"] == "LED MACHINE") | (
                       df["occupation"] == "HOARDING") | (df["occupation"] == "ISI HALL MARKING") | (
                       df["occupation"] == "TV REPAIR") | (df["occupation"] == "OFFICES") | (
                       df["occupation"] == "METRO BAZAR") | (df["occupation"] == "GROFFERS") | (
                       df["occupation"] == "HAWKER") | (df["occupation"] == "LABOUR") | (df["occupation"] == "AUTO") | (
                       df["occupation"] == "GUARD") | (df["occupation"] == "UBER") | (df["occupation"] == "DEALER") | (
                       df["occupation"] == "HAWKERY") | (df["occupation"] == "RECEPTION") | (
                       df["occupation"] == "SALES") | (df["occupation"] == "VEGETABLE SELLER") | (
                       df["occupation"] == "FISH MONGER") | (df["occupation"] == "SELLSMAN") | (
                       df["occupation"] == "PROMOTER") | (df["occupation"] == "RETAIL") | (
                       df["occupation"] == "MASON") | (df["occupation"] == "CLERK") | (
                       df["occupation"] == "SHOE MAKER") | (df["occupation"] == "MECHANIC") | (
                       df["occupation"] == "VEGETABLE VENDOR") | (df["occupation"] == "LABOUR(12)") | (
                       df["occupation"] == "FISH SELLER") | (df["occupation"] == "HOUSE SERVENT") | (
                       df["occupation"] == "BACK OFFICE") | (df["occupation"] == "CARE-TAKER") | (
                       df["occupation"] == "OFFICE HELPER") | (df["occupation"] == "CARETAKER") | (
                       df["occupation"] == "CARPENTER") | (df["occupation"] == "MANSON") | (
                       df["occupation"] == "SALESWORK") | (df["occupation"] == "HELPER") | (
                       df["occupation"] == "CLOTHES") | (df["occupation"] == "GS RAIL") | (
                       df["occupation"] == "TAILOR") | (df["occupation"] == "B ELECTRIC") | (
                       df["occupation"] == "BANNER MAKER") | (df["occupation"] == "GLOVE MAKER") | (
                       df["occupation"] == "HOUSE KEEPING") | (df["occupation"] == "RECEPTIONIST") | (
                       df["occupation"] == "PLUMBER") | (df["occupation"] == "AUTO MOBILE") | (
                       df["occupation"] == "CALL CENTER") | (df["occupation"] == "SCHOOL ELECTRICIAN") | (
                       df["occupation"] == "DRIVER") | (df["occupation"] == "RICKSAW DRIVER") | (
                       df["occupation"] == "RICKSHAW DRIVER") | (df["occupation"] == "VAN DRIVER") | (
                       df["occupation"] == "AUTO DRIVER") | (df["occupation"] == "CAR DRIVER") | (
                       df["occupation"] == "TOTO DRIVER") | (df["occupation"] == "TAXI DRIVER") | (
                       df["occupation"] == "RIKSHAW DRIVER") | (df["occupation"] == "AUTO RICKSHAW DRIVER") | (
                       df["occupation"] == "CAB DRIVER") | (df["occupation"] == "PIPELINE WORKER") | (
                       df["occupation"] == "MARBEL WORKER") | (df["occupation"] == "HOTEL WORKER") | (
                       df["occupation"] == "KITE WORKER") | (df["occupation"] == "HOSPPITAL WORKER") | (
                       df["occupation"] == "DELIVERY MAN") | (df["occupation"] == "DELIVERY JOB") | (
                       df["occupation"] == "FOOD DELIVERY") | (df["occupation"] == "HOME DELIVERY") | (
                       df["occupation"] == "SWIGGY DELIVERY AGENT") | (df["occupation"] == "DELIVERY BOY") | (
                       df["occupation"] == "SECURITY GUARD") | (df["occupation"] == "DELIVERY") | (
                       df["occupation"] == "K.F.C") | (df["occupation"] == "FLIPKART") | (
                       df["occupation"] == "WAITOR") | (df["occupation"] == "SALES BOY") | (
                       df["occupation"] == "SALES GIRL") | (df["occupation"] == "BARBER") | (
                       df["occupation"] == "MAID") | (df["occupation"] == "COOK") | (
                       df["occupation"] == "SHOP WORKER") | (df["occupation"] == "WORKER") | (
                       df["occupation"] == "CAR WASHER") | (df["occupation"] == "ELECTRICIAN") | (
                       df["occupation"] == "SALES WORKER") | (df["occupation"] == "FACTORY WORKER") | (
                       df["occupation"] == "FACTORY") | (df["occupation"] == "SECURITY") | (
                       df["occupation"] == "GARDENER") | (df["occupation"] == "PLUMBER(12)") | (
                       df["occupation"] == "PRESSING CLOTHES") | (df["occupation"] == "CABLE OPERATOR") | (
                       df["occupation"] == "SALESMAN") | (df["occupation"] == "MARBLE WORKER") | (
                       df["occupation"] == "AC.REPAIR") | (df["occupation"] == "COOK(16)") | (
                       df["occupation"] == "HOUSE MAID") | (df["occupation"] == "CUTTING") | (
                       df["occupation"] == "PUMP") | (df["occupation"] == "PLASTIC FACTORY WORKER") | (
                       df["occupation"] == "GLOVES MAKER") | (df["occupation"] == "SERVANT") | (
                       df["occupation"] == "FARMER") | (df["occupation"] == "WATER SERVICE") | (
                       df["occupation"] == "FERRY") | (df["occupation"] == "MARBEL") | (
                       df["occupation"] == "DOMINOS") | (df["occupation"] == "COMPANY WORKER") | (
                       df["occupation"] == "ZOMATO WORKER") | (df["occupation"] == "ZOMATO") | (
                       df["occupation"] == "ELECTRIC") | (df["occupation"] == "PAINTER") | (
                       df["occupation"] == "ZOMATO DELIVERY BOY") | (
                       df["occupation"] == "MAID SERVANT"), "occupation"] = "WORKER"

    df.loc[(df["occupation"] == "4") | (df["occupation"] == "SCHOOL") | (df["occupation"] == "EX TEACHER") | (
                df["occupation"] == "4/E") | (df["occupation"] == "TEACHER") | (df["occupation"] == "BLIND TEACHER") | (
                       df["occupation"] == "SCHOOL TEACHER") | (df["occupation"] == "MUSIC TEACHER") | (
                       df["occupation"] == "PRIVATE TUTOR") | (df["occupation"] == "HOMETUTOR") | (
                       df["occupation"] == "HOME TUTOR") | (df["occupation"] == "PRIVATE TUITOR") | (
                       df["occupation"] == "PRINCIPAL") | (df["occupation"] == "PROFFESSOR"), "occupation"] = "TEACHING PROFESSIONALS"

    df.loc[(df["occupation"] == "RETIRE") | (df["occupation"] == "RETIRED") | (df["occupation"] == "RETIRED,9") | (
                df["occupation"] == "9,RETIRED") | (df["occupation"] == "5,RETIRED") | (
                       df["occupation"] == "4,RETIRED") | (df["occupation"] == "1,RETIRED") | (
                       df["occupation"] == "12,RETIRED") | (df["occupation"] == "8,RETIRED") | (
                       df["occupation"] == "RETIRED ") | (df["occupation"] == "3,RETIRED") | (
                       df["occupation"] == "10,RETIRED") | (df["occupation"] == "14,RETIRED") |
                        (df["occupation"] == "R"), "occupation"] = "RETIRED"

    df.loc[(df["occupation"] == "17") | (df["occupation"] == "HOUSE WIFE") | (df["occupation"] == "19") | (
                df["occupation"] == "18") | (df["occupation"] == "STUDENT") | (df["occupation"] == "UNEMPLOYED") | (
                       df["occupation"] == "NOT WORKING") | (df["occupation"] == "HW") | (df["occupation"] == "H.W") | (
                       df["occupation"] == "H/W") | (df["occupation"] == "U/E") | (df["occupation"] == "UE") | (
                       df["occupation"] == "U/M"), "occupation"] = "UNEMPLOYED"

    df.loc[(df["occupation"] == "HOUSEWIFE") |
           (df["occupation"] == "HOUSEWIFEE"), 'occupation'] = 'HOUSEWIFE'

    df.loc[(df["occupation"] == "W.C.V.") |
           (df["occupation"] == "N/S") |
           (df["occupation"] == "V/E") |
           (df["occupation"] == "B") |
           (df["occupation"] == "s") |
           (df["occupation"] == "T") |
           (df["occupation"] == "OC") |
           (df["occupation"] == "R2") |
           (df["occupation"] == "CTC")|
           (df["occupation"] == "S"), 'occupation'] = 'UNDEFINED'

    df['occupation'] = df['occupation'].fillna(0)

    # total_days
    df.loc[df['edu'] == 'IL', 'occupation'] = 'UNEMPLOYED'
    df.loc[df['occupation'] == 'UNEMPLOYED', 'extra_days'] =+ 3
    df.loc[df['occupation'] == 'HOUSEWIFE', 'extra_days'] =+2
    df.loc[df['occupation'] == 'UNDEFINED', 'extra_days'] = +3
    df.loc[df['occupation'] == 'HEALTH PROFESSIONALS', 'extra_days'] = +4
    df.loc[df['occupation'] == 'GOVT EMPLOYEE', 'extra_days'] = 2
    df.loc[df['occupation'] == 'PVT EMPLOYEE', 'extra_days'] = 2
    df.loc[df['occupation'] == 'SMALL BUSINESS', 'extra_days'] = 3
    df.loc[df['occupation'] == 'WORKER', 'extra_days'] = 1
    df.loc[df['occupation'] == 'TEACHING PROFESSIONALS', 'extra_days'] = 2
    df.loc[df['occupation'] == 'RETIRED', 'extra_days'] = 4
    df.loc[df['occupation'] == '0', 'extra_days'] = 3
    df.loc[df['occupation'] == 'BUSINESS', 'extra_days'] =+ 4

    # age filter
    df = df[~df.age.str.contains("MONTHS|months|M", na=False)]
    df.age = df.age.astype(float)
    df['age'] = np.ceil(df.age)
    df.age = df.age.astype(int)
    df = df[df['age'] < 200]

    # ward filter
    df = df[df['ward'].notna()]
    df.ward = df.ward.astype(int)

    # education filter
    df['edu'] = df['edu'].replace(['IL','P','S','H','G','PG','O'],[0,1,2,3,4,5,6])

    # set 1 extra day for MEDICAL (P)
    df.loc[df['WEEKEND_activity'].str.contains('P', case=False), ['extra_days']] += 1
    # set 3 extra day for RECREATIONAL GYM PARK (R1A)
    df.loc[df['WEEKEND_activity'].str.contains('R1A', case=False), ['extra_days']] += 3
    # set 1 extra day for RECREATIONAL MOVIES SPORTS (R1B)
    df.loc[df['WEEKEND_activity'].str.contains('R1B', case=False), ['extra_days']] += 1
    # set 1 extra day for EVERYDAY SHOPPING (M2A)
    df.loc[df['WEEKEND_activity'].str.contains('M2A', case=False), ['extra_days']] += 1
    # set 1 extra day for EAT OUT (R1C)
    df.loc[df['WEEKEND_activity'].str.contains('R1C', case=False), ['extra_days']] += 1
    # set 1 extra day for RELIGIOUS ACTIVITIES (R1D)
    df.loc[df['WEEKEND_activity'].str.contains('R1D', case=False), ['extra_days']] += 1
    # set 1 extra day for SOCIAL (R2)
    df.loc[df['WEEKEND_activity'].str.contains('R2', case=False), ['extra_days']] += 1
    # set 0 extra day for IN HOME ACTIVITIES (H1)
    df.loc[df['WEEKEND_activity'].str.contains('H1', case=False), ['extra_days']] += 0
    # set 1 extra day for IN HOME ACTIVITIES (H2|I1|I2|I3|J1|J2)
    df.loc[df['WEEKEND_activity'].str.contains('H2|I1|I2|I3|J1|J2', case=False), ['extra_days']] += 2

    # work_days
    df['work_days'] = df['work_days'].fillna(0)
    #df['work_days'] = df['work_days'].astype(int)

    # extra days
    df['work_days'] = df['work_days'].replace(
        ['8:00', '7.0', '6.0', '5.0', '4.0', '3.0', '2.0', '1.0', '0.0', '0:00', '   ', 'NOT FIXED'],
        ['7', '7', '6', '5', '4', '3', '2', '1', '0', '0', '0', '5'])
    df['work_days'] = df['work_days'].fillna(0)
    df['work_days'] = df['work_days'].astype(int)

    # total work days
    df['total_days'] = df['extra_days'] + df['extra_days']

    # income filter

    df['income'] = df['income'].replace(['1.5LAC', '25,M000', '1 LAC', '30,M000', '600000', '10000 (HUSBAND PENSION)'],
                                        ['150000', '25000', '100000', '30000', '50000', '10000'])

    list = ['JAGATPUR ADARSHA BIDYA MANDIR', 'REFUSED', 'R', 'C/S', 'REFUNDED', '5', 'BALLYGUNGE', 'SEALDAH', 'U/E']
    df = df[df.income.isin(list) == False]

    df['income'] = df['income'].str.replace(',', '')
    df['income'] = df['income'].astype(float)
    df['income'] = df['income'].fillna(0)
    df['income'] = df['income'].astype(int)

    # 4 wheeler
    df['4_wheeler'] = df['4_wheeler'].fillna(0)
    df['4_wheeler'] = df['4_wheeler'].astype(int)

    # 2 wheeler
    df['2_wheeler'] = df['2_wheeler'].fillna(0)
    df['2_wheeler'] = df['2_wheeler'].astype(int)

    # cycle
    df = df[~df.cycle.str.contains('R|A|GOODS CAR|B|E|V|T|SUZUKI', na=False)]
    df['cycle'] = df['cycle'].fillna(0)

    df['cycle'] = df['cycle'].astype(int)

    return df
