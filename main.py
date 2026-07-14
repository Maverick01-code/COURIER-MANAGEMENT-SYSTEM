import mysql.connector as sql
import string


def create_connection():
    return sql.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='courier_service_system1'
    )


def username_exists(cursor, username):
    cursor.execute("SELECT * FROM login WHERE username = %s", (username,))
    return cursor.fetchone() is not None


def check_strong_password(password):
    if (len(password) >= 8 and
        any(char.islower() for char in password) and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in string.punctuation for char in password)):
        return True
    return False


def create_account(cursor, conn):
    name = input("Please enter your name: ")
    username = input("Enter username: ")
    if username_exists(cursor, username):
        print("Username already exists. Please choose a different username.")
        return

    while True:
        password = input("Enter password: ")
        if check_strong_password(password):
            break
        else:
            print("Password is not strong enough. Please ensure it is at least 8 characters long, includes both uppercase and lowercase letters, contains at least one number, and has at least one special character.")

    while True:
        role = input("Are you (customer/delivery partner/admin)?: ").lower()
        if role in ["delivery partner", "admin"]:
            passkey = input("Enter passkey: ")
            if (role == "delivery partner" and passkey == "sics2024mo") or (role == "admin" and passkey == "sics2024admhan"):
                cursor.execute("INSERT INTO login (name, username, passwd, ranky) VALUES (%s, %s, %s, %s)", (name, username, password, role))
                conn.commit()
                break
        elif role == "customer":
            cursor.execute("INSERT INTO login (name, username, passwd, ranky) VALUES (%s, %s, %s, %s)", (name, username, password, role))
            conn.commit()
            break
        else:
            print("Something went wrong. Please try again!")
            continue
    print("Account created successfully!")


def login(cursor):
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM login WHERE username = %s AND passwd = %s", (username, password))
    account = cursor.fetchone()
    if account:
        print(" SAKURA INTERCITY COURIER SERVICES.PVT.LTD")
        if account[3] == "customer":
            print(f"Login successful! Welcome {account[0]}")
            import Customer_services
        elif account[3] == "delivery partner":
            print(f"Login successful! Welcome {account[0]}")
            import delivery_agent
        else:
            print(f"Hello {account[3]}")
            import B_COURIER_MENU1
    else:
        print("Login failed. Incorrect username or password.")


def main():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("\n SAKURA INTERCITY COURIER SERVICES.PVT.LTD")
            print("1. Create a new account")
            print("2. Login")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_account(cursor, conn)
            elif choice == 2:
                login(cursor)
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
