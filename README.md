# CLI-Bank-Manager-on-Python
A command-line banking system built with Python as a beginner/intermediate programming project.

# 🏦 Bank Manager

A command-line banking system built with **Python** as a beginner/intermediate programming project.

The project simulates basic banking operations such as account creation, authentication, deposits, withdrawals, transfers, and transaction history while storing account data locally using **JSON**.

> 🚧 **Status:** In Development

## ✨ Features

* 👤 Create a bank account
* 🔐 Username and password authentication
* 💰 Starting balance
* 💵 Deposit money
* 💸 Withdraw money
* 🔄 Transfer money between accounts
* 📜 Transaction history
* 🚪 Login and logout system
* 💾 Persistent data storage using JSON
* 🖥️ Command-line interface

## 🛠️ Technologies

* **Python**
* **JSON**
* **Object-Oriented Programming (OOP)**
* File handling
* Exception handling
* Dictionaries and lists

## 📂 Project Structure

```text
Bank Manager/
│
├── Project 12 - Bank manager.py
│
└── data/
    └── Bank_accounts.txt
```

The `Bank_accounts.txt` file contains the account data in JSON format.

Example:

```json
{
    "username": {
        "password": "password",
        "balance": 1500,
        "history": []
    }
}
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate into the project

```bash
cd "Bank Manager"
```

### 3. Run the program

```bash
python "Project 12 - Bank manager.py"
```

## 🎮 Usage

### Main Menu

```text
===== BANK =====

1. Login
2. Create Account
3. Exit
```

After logging in:

```text
======= Welcome username =======

Balance: 1500

1. Deposit
2. Withdraw
3. Transfer
4. History
5. Logout
```

## 🧠 What I Learned

This project was created to practice concepts beyond basic Python syntax.

### Python

* Functions and classes
* Object-oriented programming
* Dictionaries and nested dictionaries
* Lists
* Input validation
* Exception handling
* File I/O
* JSON serialization/deserialization

### Programming Concepts

* Managing application state with `current_user`
* Designing menu-driven applications
* Reading and modifying persistent data
* Separating different parts of an application
* Handling user input and invalid operations

## 🔨 Planned Improvements

This project is still being developed. Planned improvements include:

* [ ] Complete transaction history system
* [ ] Better input validation
* [ ] Password security improvements
* [ ] Login attempt limits
* [ ] Better error handling
* [ ] Improved terminal UI
* [ ] Refactor the project into multiple Python modules
* [ ] Replace JSON storage with SQLite
* [ ] Add an administrator/manager system
* [ ] Add transaction timestamps

## 🎯 Future Version

The long-term goal is to evolve this project from a simple command-line application into a more structured banking application using:

```text
Python
   ↓
Object-Oriented Design
   ↓
SQLite Database
   ↓
Flask Backend
   ↓
Web Interface
```

## ⚠️ Disclaimer

This is an **educational project** and is not intended to handle real financial information or real money.

The current implementation stores passwords locally in plain text and therefore should **not** be used as a real banking system.

## 📚 Purpose

This project is part of my journey learning Python and software development. It is intended to demonstrate my progress from beginner Python programs toward larger, more structured applications.
