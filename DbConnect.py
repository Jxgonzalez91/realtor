import psycopg2
try:
    conn = psycopg2.connect(
        database="Cohort2",
        user="postgres",
        password="6108",
        host="127.0.0.1",
        port="5432"
    )

    def retrieveUserInfo(user, passW):
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM auth where username='{user}' and pass='{passW}'"
        )
        rows = cursor.fetchall()
        if(rows):
            print(f"{user}, has been authenticated.")

        else:
            print("Your database is empty")

    userNameInput = (input("Enter the username:"))
    passwordInput = (input("Enter password:"))
    retrieveUserInfo(userNameInput, passwordInput)
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
