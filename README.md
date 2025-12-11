---

### 🏥 **Project Name:** Monta Health – Clinic Management System

### 💻 **Platform:** Terminal-based (Console Application)

### 🐍 **Language:** Python

### 📂 **Data Storage:** CSV files

---
# 🏥 Monta Health – Clinic Management System

**Monta Health** is a terminal-based clinic management system built in **Python** that helps doctors and managers organize patient data, prescriptions, and drug inventory efficiently.  
It uses simple **CSV files** for data storage and features role-based access for managers and doctors.

---

## 🚀 Features

### 👨‍💼 Manager Panel
- ➕ Add new patient records  
- ✏️ Update patient information (name or illness)  
- ❌ Delete patient data by name or ID  
- 💊 Search drugs by name  
- ➕ Add new drug information  
- 🔁 Update drug price or quantity  
- 🚪 Logout anytime  

### 🩺 Doctor Panel
- 🔍 View patient information (name, illness, etc.)  
- 💊 Add or update patient prescriptions  
- 🔙 Logout 

---

## 📂 Data Storage (CSV Files)

The system uses **five CSV files** to store and manage data:

| File Name | Description |
|------------|--------------|
| `manager_login.csv` | Stores manager login credentials |
| `doctor_login.csv` | Stores doctor login credentials |
| `drug_list.csv` | Contains drug information (name, price, quantity, etc.) |
| `patient_list.csv` | Stores patient details (name, ID, illness, etc.) |
| `patient_prescription.csv` | Stores prescriptions given by doctors |

---

## 🔐 Login System

Both **manager** and **doctor** credentials are predefined and stored securely in CSV files.  
Passwords can be hashed using the **hashlib** library for better security.

---

## ⚙️ Requirments (if built-in not available)

- os
- datetime
- time
- getpass
- platform
- hashlib
- csv

### ⚙️ **Program Flow**

1. The user is greeted with the **global menu** to choose a role (Manager or Doctor).
2. After selecting a role, the system verifies credentials from the respective CSV file.
3. Once logged in, the user interacts with the terminal through menu prompts tailored to their role.
4. Data operations (add, update, delete, search) are performed directly on CSV files, ensuring persistence.
5. The user can log out or quit the program at any time.

---

### 🧠 **Key Features**

* Role-based access control (Doctor vs Manager)
* High security (Strong password, Password while typing, dual authentication)
* Persistent data storage using CSV files
* CRUD operations (Create, Read, Update, Delete)
* Drug management and patient record tracking
* Simple, text-based user interface

---
