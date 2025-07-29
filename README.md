# Student Management System

A comprehensive desktop-based application for managing student records, built with Python. This project demonstrates core software engineering principles including database management, GUI development, and Object-Oriented Programming.

## Features

- **Add New Students:** A user-friendly form to input and save new student details to the database.
- **View All Students:** Displays all student records in a clear, real-time, tabular format.
- **Update Student Information:** Select a student from the list to populate the entry fields for easy editing.
- **Delete a Student:** Remove a student record from the database with a confirmation prompt.
- **Full CRUD (Create, Read, Update, Delete) operations.**

## Technologies Used

- **Language:** Python
- **GUI Framework:** Tkinter
- **Database:** MySQL
- **Connector:** `mysql-connector-python`
- **Core Concepts:** Object-Oriented Programming (OOP), Database Integration

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Student-Management-System-Tkinter.git
    ```
    (Replace `your-username` with your actual GitHub username)

2.  **Install dependencies:**
    ```bash
    pip install mysql-connector-python
    ```
3.  **Setup the Database:**
    - Make sure you have MySQL Server running on your machine.
    - Create a database (schema) named `student_db`.
    - Execute the following SQL command to create the `students` table:
      ```sql
      CREATE TABLE `students` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(255) NULL,
        `age` INT NULL,
        `email` VARCHAR(255) NULL,
        `college` VARCHAR(255) NULL,
        `address` VARCHAR(255) NULL,
        `mobile` VARCHAR(45) NULL,
        PRIMARY KEY (`id`));
      ```
4.  **Configure Database Connection:**
    - Open the `database.py` file.
    - Find the `create_connection` function.
    - Change the `password` parameter to your own MySQL root password.

5.  **Run the application:**
    ```bash
    python main.py
    ```