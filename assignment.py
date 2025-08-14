import pandas as pd

def perform_advanced_sql_queries(db_connection):
  """
  Executes advanced SQL queries using intermediate techniques.

  This function challenges your understanding of:
  1. Subqueries for filtering
  2. Common Table Expressions (CTEs) for modularity
  3. Window functions for ranking and aggregation
  4. Complex analytical problem-solving

  Args:
    db_connection: An active database connection object.

  Returns:
    A dictionary of pandas DataFrames, where each key is the task number.
  """
  results = {}

  # Task 1: Find employees earning more than the company average salary
  # Hint: Use a subquery to find the average salary first
  # Think about: How can you compare each employee's salary to the overall average?
  results['task_1'] = None
  # Your code here

  # Task 2: Find the department with the highest total salary
  # Hint: Use a CTE to calculate total salary per department
  # Think about: First calculate totals per department, then find the maximum
  results['task_2'] = None
  # Your code here

  # Task 3: Rank employees by salary within each department
  # Hint: Use the RANK() or DENSE_RANK() window function
  # Think about: You need to partition by department and order by salary
  results['task_3'] = None
  # Your code here

  # Task 4: Calculate the running total of salaries by age within each department
  # Hint: Use SUM() OVER() with an ORDER BY clause
  # Think about: This is similar to ranking but you're summing instead
  results['task_4'] = None
  # Your code here

  # Task 5: Find the second highest-paid employee
  # Hint: Use a subquery with LIMIT and OFFSET, or a window function
  # Think about: How can you skip the first result to get the second?
  results['task_5'] = None
  # Your code here

  return results
