import smtplib
import random
import mysql.connector as sql


def create_connection():
    return sql.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='courier_service_system1'
    )


def generate_otp():
    otp = random.randint(1000, 9999)
    return otp


def send_email_and_insert_otp(email, track_id):
    conn = create_connection()
    cursor = conn.cursor()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("saikrishchen001@gmail.com", "nonv zkna pzkm narl")
    motp = generate_otp()

    message = f"""A PARCEL IS DUE TO ARRIVE TODAY AND IS SHIPPED BY SAKURA INTERNATIONAL COURIER SERVICES.
    PLEASE PROVIDE THIS OTP TO OUR DELIVERY AGENT: {motp}"""

    s.sendmail("saikrishchen001@gmail.com", email, message)
    print("OTP sent successfully!")
    cursor.execute("insert into asr(track_id,otp) values (%s,%s)", (track_id, motp))
    print(f"Track ID: {track_id}, OTP: {motp}")
    s.quit()

    return (track_id, motp)
