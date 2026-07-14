import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='root', database='courier_service_system1')
cust1 = conn.cursor()

cust1.execute(
    'create table couriers(track_ID varchar(8) primary key, c_name varchar(50), '
    'c_mobile_number varchar(10), c_address varchar(99), c_landmark varchar(40), '
    'c_pc varchar(7), r_name varchar(50), r_mobile_number varchar(10), '
    'r_address varchar(99), r_landmark varchar(40), r_pc varchar(7), r_email varchar(30), '
    'date_of_sending date, status varchar(30) default "pending")'
)

cust1.execute(
    'create table couriers2(track_ID varchar(8) default null, Weight_in_kgs float default null, '
    'distance_in_km float default null, Cost_in_rupees float default null);'
)

cust1.execute('CREATE TABLE couriers3 (name CHAR(30), mobile_no CHAR(12), city varchar(30))')

cust1.execute("CREATE TABLE ASR(track_ID varchar(8) default null, OTP int)")

cust1.execute("CREATE TABLE login(name VARCHAR(50), username VARCHAR(50), passwd VARCHAR(50), ranky VARCHAR(50))")

cust1.execute('create table can(track_ID varchar(8) primary key, S_name varchar(30), S_mob varchar(30));')

cust1.execute("insert into couriers3 values('Ayush Jain',8248115633,'chennai');")
cust1.execute("insert into couriers3 values('Aiden',9884942247,'tutucorin');")
cust1.execute("insert into couriers3 values('Vikram',8619138849,'kanchipuram');")
cust1.execute("insert into couriers3 values('Lucas',984942201,'chengalpattu');")
cust1.execute("insert into couriers3 values('Noah',9842443718,'kaniyakumari');")
cust1.execute("insert into couriers3 values('Rohan',9345513772,'madurai');")
cust1.execute("insert into couriers3 values('Max',9444951564,'rameshwaram');")
cust1.execute("insert into couriers3 values('Kunal',9840090298,'mohana road,erode');")
cust1.execute("insert into couriers3 values('Raj',8610138862,'palani');")
cust1.execute("insert into couriers3 values('akash',9677028551,'dindugal');")

conn.commit()
conn.close()
