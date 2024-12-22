import sqlite3


conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()


cursor.execute('''
DELETE FROM Users WHERE id = 6
''')

cursor.execute('''
SELECT COUNT(*) FROM Users
''')
total_records = cursor.fetchone()[0]
print(f'Общее количество записей: {total_records}')


cursor.execute('''
SELECT SUM(balance) FROM Users
''')
sum_balances = cursor.fetchone()[0]
print(f'Сумма всех балансов: {sum_balances}')


average_balance = sum_balances / total_records if total_records > 0 else 0
print(f'Средний баланс всех пользователей: {average_balance:.2f}')

# Закрываем соединение
conn.commit()
conn.close()