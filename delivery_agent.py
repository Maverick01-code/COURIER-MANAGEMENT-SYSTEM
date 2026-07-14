import mysql.connector as sql
q = open("oldrecords.", "a")
conn = sql.connect(host='localhost', user='root', passwd='root', database='courier_service_system1')
cust1 = conn.cursor()
from import_requests import send_email_and_insert_otp
import mysql.connector as sql


def record_deletion():
    myconn = sql.connect(host='localhost', user='root', passwd='root', database='courier_service_system1')
    cust2 = myconn.cursor()
    print("Correct OTP. Please hand over the package.")
    cust2.execute("DELETE FROM asr WHERE track_id= %s;", (z,))
    fetch_and_write_to_file()
    cust2.execute("UPDATE couriers SET status = 'delivered' WHERE track_id = %s", (z,))
    cust2.execute("DELETE FROM couriers WHERE track_id = %s", (z,))
    myconn.commit()


def fetch_and_write_to_file():
    try:
        cust1.execute("SELECT * FROM couriers WHERE track_id = %s", (z,))
        with open('archive.txt', 'a') as file:
            row = cust1.fetchone()
            while row:
                file.write(f"{row}\n")
                row = cust1.fetchone()
                file.flush()
        # print("Data has been written to output.txt")
    except sql.Error as e:
        print(f"Error: {e}")
    finally:
        cust1.close()
        conn.close()


while True:
    x = input("Enter the tracking ID of the next parcel you are going to deliver or type 'exit' to end delivery for the day: ")
    if x.lower() == 'exit':
        print("Ending delivery for the day. Please return the rest of the packages to the HQ.")
        break

    try:
        z = int(x)
        cust1.execute(
            "SELECT r_name, r_mobile_number, r_address, r_landmark, r_pc, status FROM couriers WHERE track_id = %s",
            (z,)
        )

        parcel = cust1.fetchone()

        if parcel[-1] != "delivered":
            print("Receiver's name: ", parcel[0])
            print("Receiver's mobile number: ", parcel[1])
            print("Receiver's address: ", parcel[2])
            print("Receiver's landmark: ", parcel[3])
            print("Receiver's pincode: ", parcel[4])

            op = input("Have you reached the location (yes/no)? If not able to contact, enter 'no': ").lower()

            print(op)
            if op == "yes":
                cust1.execute("SELECT r_email FROM couriers WHERE track_id = %s", (z,))
                result = cust1.fetchone()

                if result:
                    k = result[-1]
                    print(f"Sending email to: {k}, with tracking ID: {z}")
                    em = send_email_and_insert_otp(k, z)
                    print(em)

                    qp = int(input("enter otp provide by customer:"))

                    if qp == em[1]:
                        record_deletion()
                        conn.close()
                    else:
                        print("Wrong OTP. Please try again or contact the HQ.")
                        cust1.execute("DELETE FROM asr WHERE track_id= %s;", (z,))
                        conn.commit()
                else:
                    print("Email not found for the given tracking ID.")
            elif op == "no":
                print("Please return the package to HQ at the end of the day.")
            elif parcel[-1] == "delivered":
                print("this parcel is already delievered so please check if it is correct tracking id")
            else:
                print("Tracking ID not found. Please check the ID and try again.")

    except ValueError:
        print("Invalid input. Please enter a valid tracking ID.")

conn.commit()
conn.close()
q.close()
