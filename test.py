import unittest
import pandas as pd
from sqlalchemy import create_engine, text
from sample_submission import perform_advanced_sql_queries

class TestAdvancedSQL(unittest.TestCase):
    def setUp(self):
        """Set up a temporary in-memory SQLite database for testing"""
        self.engine = create_engine('sqlite:///:memory:')
        self.connection = self.engine.connect()

        # Create tables
        self.connection.execute(text("""
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        """))
        self.connection.execute(text("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            salary INTEGER,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments (id)
        );
        """))

        # Insert sample data
        self.connection.execute(text("INSERT INTO departments (id, name) VALUES (1, 'IT'), (2, 'HR'), (3, 'Finance');"))
        self.connection.execute(text("""
        INSERT INTO employees (id, name, age, salary, department_id) VALUES
        (1, 'Alice', 30, 80000, 1),
        (2, 'Bob', 45, 95000, 2),
        (3, 'Charlie', 28, 72000, 1),
        (4, 'David', 52, 120000, 3),
        (5, 'Eve', 38, 110000, 1),
        (6, 'Frank', 41, 60000, 2),
        (7, 'Grace', 35, 150000, 3),
        (8, 'Henry', 48, 90000, 1);
        """))
        self.connection.commit()

    def tearDown(self):
        """Close the database connection after each test"""
        self.connection.close()

    def test_perform_advanced_sql_queries_returns_dict(self):
        """Test that the function returns a dictionary"""
        results = perform_advanced_sql_queries(self.connection)
        self.assertIsInstance(results, dict)

    def test_task_1_above_average_salary(self):
        """Test that task 1 finds employees with salaries above the average"""
        results = perform_advanced_sql_queries(self.connection)
        df = results.get('task_1')
        self.assertIsInstance(df, pd.DataFrame)
        avg_salary = 97125.0
        self.assertTrue(all(df['salary'] > avg_salary))
        self.assertEqual(len(df), 3)

    def test_task_2_department_with_highest_salary(self):
        """Test that task 2 finds the department with the highest total salary"""
        results = perform_advanced_sql_queries(self.connection)
        df = results.get('task_2')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df['name'].iloc[0], 'IT')
        self.assertEqual(df['total_salary'].iloc[0], 352000)

    def test_task_3_rank_employees(self):
        """Test that task 3 correctly ranks employees by salary within each department"""
        results = perform_advanced_sql_queries(self.connection)
        df = results.get('task_3')
        self.assertIsInstance(df, pd.DataFrame)
        it_df = df[df['department_id'] == 1].sort_values(by='salary', ascending=False)
        self.assertEqual(it_df.iloc[0]['salary_rank'], 1)
        self.assertEqual(it_df.iloc[0]['name'], 'Eve')

    def test_task_4_running_total(self):
        """Test that task 4 calculates the running total of salaries correctly"""
        results = perform_advanced_sql_queries(self.connection)
        df = results.get('task_4')
        self.assertIsInstance(df, pd.DataFrame)
        it_df = df[df['department_id'] == 1].sort_values(by='age')
        self.assertEqual(it_df.iloc[0]['running_total'], 72000)
        self.assertEqual(it_df.iloc[1]['running_total'], 152000)

    def test_task_5_second_highest_salary(self):
        """Test that task 5 finds the second highest-paid employee"""
        results = perform_advanced_sql_queries(self.connection)
        df = results.get('task_5')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df['name'].iloc[0], 'David')
        self.assertEqual(df['salary'].iloc[0], 120000)

if __name__ == '__main__':
    unittest.main()
