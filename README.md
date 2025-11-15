# Expense Management System

This project is an expense management system where the the expense data against some categories(Rent, Food, Shopping, Entertainment, Other) are maintained base on particular dates.
It consists of a frontend Streamlit server and backend FastAPI server connected to MySQL database.

![](project_expense_management_archi_diagram.png?raw=true)
## Project Structure
- **frontend/**: Contains Streamlit application code
- **backend/**: Contains FastAPI backend server code
- **tests/**: Contains the test cases for backend
- **requirements.txt**: Contains the required Python packages
- **README.md**: Contains an overview of the project

## Setup Instructions
1. **Clone the repository**:
    ```bash
   git clone 
   cd expense-anagement-system
    ```
2. **Install dependencies:**:
    ```commandline
    pip install -r .\requirements.txt
    ```
3. **Run the FastAPI server:**:
    ```commandline
    uvicorn server:app --reload
    ```
4. **Run the Streamlit server:**:
    ```commandline
   streamlit run .\app.py
    ```