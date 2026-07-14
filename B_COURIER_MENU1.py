import random
from datetime import date
from distance import *
import mysql.connector as sql
from datetime import datetime
from prettytable import PrettyTable

conn = sql.connect(host='localhost', user='root', passwd='root', database='courier_service_system1')
cust1 = conn.cursor()


def print_bill(track_ID, c_name, c_mobile_number, c_address, c_landmark, c_pc,
                r_name, r_mobile_number, r_address, r_pc, r_email, date_of_sending, price):
    print("====================================================")
    print("            BILL RECEIPT            ")
    print(" SAKURA INTERCITY COURIER SERVICES.PVT.LTD")
    print("====================================================")
    print(f"Tracking ID    : {track_ID}")
    print("----------------------------------------")
    print("Sender Details:")
    print(f"Name           : {c_name}")
    print(f"Mobile Number  : {c_mobile_number}")
    print(f"Address        : {c_address}")
    print(f"Landmark       : {c_landmark}")
    print(f"Pincode        : {c_pc}")
    print("----------------------------------------")
    print("Receiver Details:")
    print(f"Name           : {r_name}")
    print(f"Mobile Number  : {r_mobile_number}")
    print(f"Address        : {r_address}")
    print(f"Pincode        : {r_pc}")
    print(f"Email          : {r_email}")
    print("----------------------------------------")
    print(f"Date of Sending : {date_of_sending}")
    print("                                            =======")
    print("                         TOTAL PAYABLE AMOUNT :", price)
    print("                                            =======")
    print("====================================================")


def unique_track_id():
    random_number = generate_random_number()
    cust1.execute("select track_id from couriers")
    eor = cust1.fetchall()
    for i in eor:
        if i == random_number:
            random_number = generate_random_number()
        else:
            continue
    return random_number


def generate_random_number():
    return ''.join(random.choices('0123456789', k=8))


z = unique_track_id()


def calculate_shipping_cost(weight, distance):
    distance = float(distance)

    if weight <= 50:
        if distance == 0:
            return 10
        elif distance <= 200:
            return 35
        elif distance <= 1000:
            return 35
        elif distance <= 2000:
            return 35
        else:
            return 35
    elif weight <= 200:
        if distance <= 0:
            return 10
        elif distance <= 200:
            return 35
        elif distance <= 1000:
            return 40
        elif distance <= 2000:
            return 60
        else:
            return 70
    elif weight <= 500:
        if distance <= 0:
            return 13
        elif distance <= 200:
            return 50
        elif distance <= 1000:
            return 60
        elif distance <= 2000:
            return 80
        else:
            return 90
    else:
        additional_weight = weight - 500
        additional_cost = ((additional_weight + 499) // 500) * 10
        if distance <= 0:
            return 15
        elif distance <= 200:
            return 50 + additional_cost
        elif distance <= 1000:
            return 60 + additional_cost * 2
        elif distance <= 2000:
            return 80 + additional_cost * 3
        else:
            return 90 + additional_cost * 5


def track_ID_assigning(z):
    fetch31 = cust1.fetchall()
    L = []
    for num in fetch31:
        L.append(num[-1])
    z = random.randint(0, len(L) - 1)
    z1 = L[z]
    cust1.execute("UPDATE couriers3 SET track_ID = '%s' WHERE mobile_no = '%s'" % (z, z1))
    cust1.execute("UPDATE couriers3 SET status = 'Pending' WHERE mobile_no = '%s'" % z1)
    conn.commit()


while True:
    print()
    print('1.Courier_order and customer_details')
    print('2.Cancel a placement')
    print('3.courier_service_partner')
    print('4.All courier placement')
    print('5.Particular detail of courier placement')
    print('6.exit')
    choice = int(input('enter the section you want to access:....(1,2,3or4)........:'))

    if choice == 1:
        print('A.courier placement')
        print('B.courier order list')
        sect = str(input('enter the section that you want to access:'))

        if sect == "A":
            print('COURIER-ORDER')
            print("Sender details:\n")
            a = input('enter the name:')
            b = input('enter the mobile number:')
            c1 = input('enter the address:')
            c2 = input('enter the landmark: ')
            c5 = int(input('enter the PinCode:'))
            print("Reciever details:\n")
            d = input('enter the name:')
            e = input('enter the mobile number:')
            f1 = input('enter the address:')
            f2 = input('enter the landmark: ')
            f5 = int(input('enter the PinCode:'))
            f6 = input("enter reciever's email id: ")
            z = unique_track_id()
            print("Courier details:")
            g = float(input('enter the weight in kgs.'))

            now = datetime.now()
            current_date = now.date()
            s = calculate_distance(c5, f5)
            qwwq = calculate_shipping_cost(g, s)
            cust1.execute(f"INSERT INTO couriers2 VALUES({z},{g},{s},{qwwq})")
            cust1.execute(
                "INSERT INTO couriers (track_ID, c_name, c_mobile_number, c_address, c_landmark, c_pc, "
                "r_name, r_mobile_number, r_address, r_landmark, r_pc, r_email, date_of_sending, status) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (z, a, b, c1, c2, c5, d, e, f1, f2, f5, f6, current_date, 'pending')
            )
            print("printing final bill!!!!!!!")
            conn.commit()
            print_bill(track_ID=z, c_name=a, c_mobile_number=b, c_address=c1, c_landmark=c2, c_pc=c5,
                       r_name=d, r_mobile_number=e, r_address=f1, r_pc=f5, r_email=f6,
                       date_of_sending=current_date, price=qwwq)
            print("courier placed successfully!")
            print('================================================================================')

        elif sect == "B":
            S = str(input(r'do you want to see your courier_order"(yes\no):'))
            if S == "yes":
                a = input('enter the customer mob number:')
                cust1.execute('select * from couriers where customer_mobile_number="{}"'.format(a))
                order = cust1.fetchall()
                print('customer name,', 'customer mob no,', 'customer address,',
                      'receiver name,', 'receiver mob no,', 'receiver address:')
                for j in order:
                    print(j)
                print('========================================================================')
            else:
                print('REDIRECTING BACK TO MAIN MENU')
                print('========================================================================')

    elif choice == 2:
        w = int(input("ENTER THE TRACKING ID OF THE COURIER PLACEMENT:"))
        cust1.execute("select * from couriers where track_ID = %s", (w,))
        f = cust1.fetchone()

        if f is None:
            print("No courier found with that tracking ID.")
        elif f[-1] == 'pending':
            print("the package is still in transit process do u want to cancel deliver(yes/no):")
            if input() == "yes":
                print("the order is being cancelled.")
                cust1.execute("DELETE FROM couriers WHERE track_ID = %s", (w,))
                cust1.execute("INSERT INTO can(track_ID, S_name, S_mob) VALUES (%s, %s, %s)", (f[0], f[1], f[2]))
                conn.commit()
                print("the package will arrive here within the next 2 days")
            else:
                print("Cancellation aborted. Order remains active.")
                print('REDIRECTING BACK TO MAIN MENU')
                print('========================================================================')
                continue
        else:
            print("We are sorry, the package is already delivered.")
            print('REDIRECTING BACK TO MAIN MENU')
            print('========================================================================')

    elif choice == 3:
        cust1.execute("select name,mobile_no,city from couriers3")
        data = cust1.fetchall()
        table = PrettyTable()
        table.field_names = ["Name", "Mobile Number", "City"]
        for row in data:
            table.add_row(row)
        print(table)

    elif choice == 4:
        cust1.execute("select track_ID,c_name,c_mobile_number,r_name,r_mobile_number,r_address,r_pc,status from couriers")
        data1 = cust1.fetchall()
        table = PrettyTable()
        table.field_names = ["Track ID", "Customer Name", "Customer Mobile Number", "Recipient Name",
                              "Recipient Mobile Number", "Recipient Address", "Recipient Postal Code", "Status"]
        for row in data1:
            table.add_row(row)
        print(table)

    elif choice == 5:
        w = int(input("enter tracking id to check:"))
        cust1.execute(
            "SELECT track_ID, c_name, c_mobile_number, r_name, r_mobile_number, r_address, r_pc, status "
            "FROM couriers WHERE track_ID = %s", (w,)
        )
        rows = cust1.fetchall()
        table = PrettyTable()
        table.field_names = ["Track ID", "Customer Name", "Customer Mobile Number", "Recipient Name",
                              "Recipient Mobile Number", "Recipient Address", "Recipient Postal Code", "Status"]
        for row in rows:
            table.add_row(row)
        print(table)

    elif choice == 6:
        print("LOGGINNG YOU OUT !")
        break

conn.commit()
conn.close()