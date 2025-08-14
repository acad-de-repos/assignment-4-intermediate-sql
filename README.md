# Intermediate SQL Techniques Assignment

## Problem Description

In this assignment, you will tackle more complex data analysis challenges using intermediate SQL techniques. You will work with subqueries, Common Table Expressions (CTEs), and window functions to perform advanced data manipulations and calculations. This assignment is designed to deepen your SQL expertise and prepare you for more sophisticated data engineering tasks.

## Learning Objectives

By completing this assignment, you will learn:
- How to use subqueries to filter data based on aggregate conditions
- How to structure complex queries with Common Table Expressions (CTEs)
- How to use window functions for ranking and calculating running totals
- How to solve complex analytical problems using a combination of SQL techniques

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the following packages installed:
   - pandas (>=1.3.0)
   - sqlalchemy (>=1.4.0)

## Instructions

1. Open the `assignment.py` file.
2. You will find a function definition: `perform_advanced_sql_queries(db_connection)`.
3. The function takes a database connection object as input.
4. Your tasks are to:
   *   **Task 1**: Find all employees who earn more than the company's average salary.
   *   **Task 2**: Using a CTE, find the department with the highest total salary expenditure.
   *   **Task 3**: Rank employees within each department based on their salary in descending order.
   *   **Task 4**: Calculate the running total of salaries for employees within each department, ordered by age.
   *   **Task 5**: Find the second highest-paid employee in the entire company.

## Hints

*   For Task 1, use a subquery to calculate the average salary.
*   For Task 2, use a CTE to calculate the total salary for each department, then select the department with the maximum total salary.
*   For Task 3, use the `RANK()` or `DENSE_RANK()` window function.
*   For Task 4, use the `SUM() OVER()` window function with an `ORDER BY` clause.
*   For Task 5, you can use a subquery with `LIMIT` and `OFFSET`, or a window function like `DENSE_RANK()`.

## Testing Your Solution

Run the test file to verify your implementation:
```bash
python test.py
```

The tests will check:
- That your function returns a dictionary with the correct keys
- That each returned DataFrame has the expected columns and data types
- That the query results are accurate based on the test data
- That the advanced SQL techniques are correctly applied

## Expected Output

Your function should return a dictionary of pandas DataFrames, where each key is the task number (e.g., 'task_1', 'task_2', etc.) and the value is the resulting DataFrame from the corresponding SQL query.

## Sample Data Format

The database will contain two tables: `employees` and `departments`.

### `employees` table:
- `id` (INTEGER, PRIMARY KEY)
- `name` (TEXT)
- `age` (INTEGER)
- `salary` (INTEGER)
- `department_id` (INTEGER, FOREIGN KEY)

### `departments` table:
- `id` (INTEGER, PRIMARY KEY)
- `name` (TEXT)

## Troubleshooting

### Common Errors
- `DatabaseError: execution failed on statement`: Check your SQL syntax for errors, especially with window functions and CTEs.
- `KeyError`: Ensure your returned dictionary has the correct keys ('task_1', 'task_2', etc.).
- `AssertionError`: Your query results do not match the expected output. Double-check your logic and the ordering of your results.

## Further Exploration (Optional)

*   Explore other window functions like `LEAD()`, `LAG()`, and `NTILE()`.
*   How would you find employees who have the same salary?
*   Can you write a query to calculate the difference between each employee's salary and the average salary of their department?
*   Look into recursive CTEs for hierarchical data traversal.

## Resources

- [SQL Subqueries](https://www.essentialsql.com/sql-subqueries/)
- [SQL Window Functions Explained](https://learnsql.com/blog/sql-window-functions-explained/)
- [A Guide to SQL Common Table Expressions (CTEs)](https://www.simplilearn.com/tutorials/sql-tutorial/sql-cte)
- [Intermediate SQL for Data Analysis](https://www.datacamp.com/courses/intermediate-sql)
