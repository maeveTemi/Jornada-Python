# Python Product Registration Automation

## Overview

A Python automation project that uses **PyAutoGUI, pandas, and time** to automate the registration of multiple products on a website.

The automation reads product information from a CSV file, opens a browser, accesses a simulated company website, and registers each product automatically. The process is repeated until all products in the dataset have been registered.

This project was developed as part of my Python learning journey, with a focus on **automation, data handling, and interaction with web interfaces**.

---

## Project Objective

The goal of this project is to automate a repetitive data-entry task that would otherwise require manually registering each product individually.

The workflow is:

1. Open the browser.
2. Access the company's website.
3. Log into the system.
4. Read the product data from a CSV file.
5. Fill in the registration form using the data from each row.
6. Submit the product registration.
7. Repeat the process until all products have been registered.

---

## Technologies Used

| Technology    | Purpose                                   |
| ------------- | ----------------------------------------- |
| **Python**    | Main programming language                 |
| **PyAutoGUI** | Automates keyboard and mouse interactions |
| **pandas**    | Reads and processes the CSV dataset       |
| **time**      | Controls pauses between automation steps  |

---

## Project Structure

```text
Jornada-Python/
│
├── Aula 1/
│   ├── codigo.py
│   └── auxiliar.py
│   └── produtos.csv
│   └── README.md
│
└── README.md
```

---

## Input Data

The products are stored in a CSV file, with each row representing a product to be registered.

The `pandas` library is used to read the CSV file and iterate through the products.

---

## How It Works

The automation follows this workflow:

```text
CSV file
   ↓
pandas reads the data
   ↓
Open browser
   ↓
Access website
   ↓
Login
   ↓
Read product data
   ↓
Fill registration form
   ↓
Submit registration
   ↓
Move to next product
   ↓
Repeat until all products are registered
```

**PyAutoGUI** handles the interaction with the website by simulating keyboard and mouse actions, while the **time** module adds pauses between actions to give the browser and website time to respond.

---

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/maeveTemi/Jornada-Python.git
cd Jornada-Python
```

### 2. Install the required libraries

```bash
pip install pyautogui pandas
```

### 3. Run the script

```bash
python codigo.py
```

> **Note:** Because this project uses PyAutoGUI to interact with the graphical interface, the script must be run in an environment where Python can control the desktop. The automation was developed and tested on Windows.

---

## What I Learned

Through this project, I practiced:

- Reading CSV files with pandas
- Iterating through rows of a dataset
- Automating keyboard and mouse interactions with PyAutoGUI
- Using Python to automate repetitive tasks
- Working with timing and delays in automation workflows
- Connecting data processing with GUI automation
- Structuring a Python script around a repeatable workflow

---

## Possible Improvements

Some possible improvements for a future version include:

- Adding error handling for failed registrations
- Using image recognition to make the automation less dependent on fixed screen positions
- Adding logging to track successful and failed registrations
- Validating the CSV data before starting the automation
- Adding a configurable delay instead of hard-coded pauses
- Providing a summary of successful and failed registrations at the end

---

## Context

This project was developed as part of my studies in Python and represents an early practical exercise in combining **data processing and automation**.
