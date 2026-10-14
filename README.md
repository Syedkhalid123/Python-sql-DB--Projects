# Retail Sales Data Processing Pipeline

## 📌 Project Overview

The **Retail Sales Data Processing Pipeline** is a Python-based data engineering project that processes retail sales data from CSV files, validates data quality, removes duplicate records, and loads clean data into a MySQL database.

The project simulates a real-world ETL (Extract, Transform, Load) workflow and demonstrates fundamental data engineering concepts using Python and SQL.

## 🎯 Objectives

- Read retail sales data from CSV files.
- Validate records and identify data quality issues.
- Filter invalid records based on business rules.
- Remove duplicate order IDs.
- Load clean records into MySQL.
- Handle database connections and SQL operations using Python.
- Prepare the foundation for processing larger datasets.

## 🛠️ Technologies Used

- **Python** — Data ingestion, validation, transformation, and database operations.
- **MySQL** — Relational database for storing clean sales records.
- **CSV** — Input data format.
- **mysql-connector-python** — Python-to-MySQL connectivity.
- **Git & GitHub** — Version control and project hosting.

## 🏗️ Project Architecture

```text
CSV Sales Files
      |
      v
Python CSV Reader
      |
      v
Data Validation
      |
      v
Duplicate Removal
      |
      v
Clean Sales Records
      |
      v
MySQL Database
      |
      v
Sales Table
```

## 📂 Project Structure

```text
1st_Retail_sales_processing_pipeline/
│
├── data/
│   ├── sales_day1.csv
│   ├── sales_day2.csv
│   └── sales_day3.csv
│
├── venv/
│
├── config.py
├── generate_sales.py
├── main.py
├── .gitignore
└── README.md
```

**Note:** The `venv/` directory is created locally and should not be committed to GitHub.

## ⚙️ Features

### 1. CSV Data Ingestion
Reads sales records from CSV files using Python's built-in `csv` module and `csv.DictReader`.

### 2. Data Validation
Validates records using business rules:

- `customer_id` must not be empty.
- `quantity` must be a valid integer greater than zero.
- `unit_price` must be a valid number and cannot be negative.

Invalid records are excluded from the clean dataset.

### 3. Duplicate Removal
Uses Python sets to identify duplicate `order_id` values and retain only the first occurrence within the processed dataset.

### 4. MySQL Integration
Connects Python to MySQL and loads clean records into the `sales` table using parameterized SQL queries.

### 5. Duplicate-Safe Database Loading
Uses MySQL's `ON DUPLICATE KEY UPDATE` clause to update an existing order when its primary key already exists.

### 6. Synthetic Data Generation
Uses `generate_sales.py` to generate a larger sample dataset for testing data processing and validation logic.

## 🗄️ Database Schema

Database: `retail_sales`

Table: `sales`

| Column | Data Type | Description |
|---|---|---|
| `order_id` | INT | Unique order identifier |
| `order_date` | DATE | Date of the order |
| `customer_id` | VARCHAR(20) | Customer identifier |
| `product_name` | VARCHAR(100) | Product name |
| `quantity` | INT | Number of units purchased |
| `unit_price` | DECIMAL(10,2) | Price per unit |

### Create the Database and Table

```sql
CREATE DATABASE retail_sales;

USE retail_sales;

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    CHECK (quantity > 0),
    CHECK (unit_price >= 0)
);
```

## 🚀 Getting Started

### Prerequisites

Install the following before running the project:

- Python 3.x
- MySQL Server
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Syedkhalid123/Python-sql-DB--Projects.git
```

Navigate to the project directory:

```bash
cd Python-sql-DB--Projects
```

If this project is stored in a subfolder of the repository, navigate into that subfolder before continuing.

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv
```

On Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
pip install mysql-connector-python
```

### Step 4: Configure MySQL Credentials

Configure `config.py` to use your local MySQL connection and database.

Set the `MYSQL_PASSWORD` environment variable before running the script.

Windows Command Prompt:

```cmd
set MYSQL_PASSWORD=your_mysql_password
```

Replace the placeholder with your actual MySQL password. Never commit real credentials to GitHub.

### Step 5: Create the Database

Run the SQL commands in the database section using MySQL Workbench or your MySQL client.

### Step 6: Run the Pipeline

```bash
python main.py
```

The script reads the configured CSV file, validates records, removes duplicates, and loads the resulting records into MySQL.

### Optional: Generate a Larger Dataset

```bash
python generate_sales.py
```

This generates a sample sales dataset for additional testing. Update the configured input file if you want to process the generated file.

## 📊 Data Quality Rules

| Validation | Expected Rule |
|---|---|
| Customer ID | Must not be empty |
| Quantity | Must be an integer greater than zero |
| Unit price | Must be a valid number greater than or equal to zero |
| Order ID | Duplicate IDs are filtered within the processed dataset |

## 🧠 Key Learning Outcomes

Through this project, I practiced:

- Python file handling and CSV processing.
- Dictionaries, lists, sets, loops, and functions.
- Data quality checks and error handling.
- SQL table creation and constraints.
- Python–MySQL connectivity.
- Parameterized SQL queries and database transactions.
- Git and GitHub version control.
- Building a basic ETL pipeline.

## 🔮 Future Improvements

- Process multiple CSV files automatically.
- Store invalid records in a separate rejected-data file.
- Add structured logging and error reporting.
- Track inserted, updated, rejected, and duplicate record counts.
- Add automated tests for validation logic.
- Improve database loading for larger datasets.
- Add incremental processing and configurable input paths.

## 👨‍💻 Author

**Syed Khalid**

GitHub: [@Syedkhalid123](https://github.com/Syedkhalid123)

---

*This project is part of my hands-on journey in Python, SQL, and data engineering.*
