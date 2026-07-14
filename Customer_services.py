import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='root', database='courier_service_system1')
cust1 = conn.cursor()


def track_id_customer_side():
    while True:
        q = int(input("Enter tracking ID: "))
        cust1.execute("SELECT * FROM couriers WHERE track_id = %s", (q,))
        result = cust1.fetchone()

        if result:
            print("Tracking ID: ", result[0])
            print("Customer Name: ", result[1])
            print("Receiver Name: ", result[2])
            print("Status: ", result[-1])

            if result[-1] == "pending":
                print("The parcel will reach the recipient in 2-3 buissness days.")
                print("If not yet reached, please contact our customer care number present in the provided bill.")
        elif result is None:
            o = open('archive.txt', 'a')
            q = o.readlines()
            for i in q:
                for j in i:
                    if j == str(q):
                        print("The package has already reached its destination, if not please contact our customer care number present in the provided bill.")
        else:
            print("Invalid tracking ID. Please try again.")
        x = input("Do you want to track more parcels? (yes/no): ").lower()
        if x != "yes":
            print("Exiting the tracking system.")
            break


track_id_customer_side()
