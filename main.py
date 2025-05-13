import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# ایجاد جدول کتاب‌ها
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
''')

# افزودن کتاب
def add_book(title, author):
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()

# نمایش کتاب‌ها
def view_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")

# حذف کتاب با ID
def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()

# نمونه اجرا
while True:
    print("\n1. افزودن کتاب\n2. نمایش کتاب‌ها\n3. حذف کتاب\n4. خروج")
    choice = input("انتخاب شما: ")

    if choice == '1':
        title = input("عنوان کتاب: ")
        author = input("نام نویسنده: ")
        add_book(title, author)
    elif choice == '2':
        view_books()
    elif choice == '3':
        book_id = input("ID کتاب برای حذف: ")
        delete_book(book_id)
    elif choice == '4':
        break
    else:
        print("گزینه نامعتبر")

conn.close()
