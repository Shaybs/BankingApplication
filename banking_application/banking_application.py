from pymysql import connect
import os

connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4'
)

def Reset_SQL():
    global connection
    connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4'
)


def set_account(name, surname):
    deposit = '0'
    withdrawal = '0'
    balance = '0'
    
    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO Account(name, surname, deposit, withdrawal, balance) values (%s, %s, %s, %s, %s);"
            cursor.execute(query, (name, surname, deposit, withdrawal, balance))
        connection.commit()
    finally:
        connection.close()

def get_account():
    Reset_SQL()

    try:
        with connection.cursor() as cursor:
            query = "SELECT account_id FROM Account ORDER BY account_id DESC LIMIT 1;"
            cursor.execute(query)
            result = cursor.fetchall()
            account_id = result[0][0]
            print('Your Account ID is: ', account_id)
    finally:
        connection.close()


def set_deposit(amount, current_deposit, balance, account_id):
    Reset_SQL()
    deposit = current_deposit + amount
    new_balance = balance + amount
    new_id = account_id
    
    try:
        with connection.cursor() as cursor:
            query = f"UPDATE Account SET deposit = '{deposit}', balance = '{new_balance}' WHERE account_id = '{new_id}';"
            cursor.execute(query)
            connection.commit()
    finally:
        connection.close()

def set_withdrawal(amount, current_withdrawal, balance, account_id):
    Reset_SQL()
    withdrawal = current_withdrawal + amount
    new_balance = balance - amount
    new_id = account_id
    
    try:
        with connection.cursor() as cursor:
            query = f"UPDATE Account SET withdrawal = '{withdrawal}', balance = '{new_balance}' WHERE account_id = '{new_id}';"
            cursor.execute(query)
            connection.commit()
    finally:
        connection.close()

def get_balance(account_id):
    Reset_SQL()

    cust_id = account_id
    try:
        with connection.cursor() as cursor:
            query = f"SELECT balance FROM Account WHERE account_id = '{cust_id}';"
            cursor.execute(query)
            result = cursor.fetchall()
            balance = result[0][0]
            print(balance)
            return balance
    finally:
        connection.close()

def get_current_withdrawal(account_id):
    Reset_SQL()

    cust_id = account_id
    try:
        with connection.cursor() as cursor:
            query = f"SELECT withdrawal FROM Account WHERE account_id = '{cust_id}';"
            cursor.execute(query)
            result = cursor.fetchall()
            withdrawal = result[0][0]
            print(withdrawal)
            return withdrawal
    finally:
        connection.close()

def get_current_deposit(account_id):
    Reset_SQL()
    cust_id = account_id
    try:
        with connection.cursor() as cursor:
            query = f"SELECT deposit FROM Account WHERE account_id = '{cust_id}';"
            cursor.execute(query)
            result = cursor.fetchall()
            deposit = result[0][0]
            print(deposit)
            return deposit
    finally:
        connection.close()

SQLConnection_active = True

while SQLConnection_active:
    choice = int(input('Please make a selection of 1 to set up an account, 2 to set deposit, 3 to withdraw, 4 to get balance: '))
    if choice == 1:
        name = input('Please provide your given name: ')
        surname = input('Please provide your given surname: ')
        set_account(name, surname)
        get_account()
    elif choice == 2:
        deposit = int(input('How much are you depositing?: '))
        account_id = input('What is your account_id?: ')
        current_deposit = get_current_deposit(account_id)
        balance = get_balance(account_id)
        set_deposit(deposit, current_deposit, balance, account_id)
    elif choice == 3:
        withdraw = int(input('How much are you withdrawng?: '))
        account_id = input('What is your account_id?: ')
        current_withdrawal = get_current_withdrawal(account_id)
        balance = get_balance(account_id)
        set_withdrawal(withdraw, current_withdrawal, balance, account_id)
    elif choice == 4:
        account_id = input('What is your account_id?: ')
        balance = get_balance(account_id)


    userchoice = input('Do you want to continue, Yes or No? ')

    if userchoice == 'No' or userchoice == 'nO' or userchoice == 'NO' or userchoice == 'no':
        SQLConnection_active = False
        break
    
