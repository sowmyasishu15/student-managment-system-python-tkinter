# database.py

import mysql.connector
from mysql.connector import Error

# ⚠️ Store credentials securely in production
DB_CONFIG = {
    'host': 'localhost',
    'database': 'student_db',
    'user': 'root',
    'password': 'root' 
}

def create_connection():
    """Establish and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"[DB ERROR] Unable to connect: {e}")
    return None

def add_student(name, age, email, college, address, mobile):
    """Add a student to the database."""
    conn = create_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO students (name, age, email, college, address, mobile)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, age, email, college, address, mobile))
        conn.commit()
        return True
    except Error as e:
        print(f"[DB ERROR] Failed to add student: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_all_students():
    """Fetch all student records as a list of dictionaries."""
    conn = create_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    except Error as e:
        print(f"[DB ERROR] Failed to fetch students: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_student(student_id, name, age, email, college, address, mobile):
    """Update a student's information."""
    conn = create_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        query = """
            UPDATE students
            SET name=%s, age=%s, email=%s, college=%s, address=%s, mobile=%s
            WHERE id=%s
        """
        cursor.execute(query, (name, age, email, college, address, mobile, student_id))
        conn.commit()
        return True
    except Error as e:
        print(f"[DB ERROR] Failed to update student: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_student(student_id):
    """Delete a student by ID."""
    conn = create_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        return True
    except Error as e:
        print(f"[DB ERROR] Failed to delete student: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
