import os
import sys

import pandas as pd

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

import oracledb

oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb

user = os.environ['ORACLE_USER']
password = os.environ['ORACLE_PASSWORD']
dsn = os.environ['ORACLE_DSN']

engine_cloud = create_engine(f'oracle://:@',
                             connect_args={
                                 "user": user,
                                 "password": password,
                                 "dsn": dsn
                             }
                            )

try:
   # Read employees table
   employees_sql = "SELECT * FROM employees"
   df_employees = pd.read_sql(employees_sql,engine_cloud)
   print(df_employees)

   # Read employees_salary table
   employees_salary_sql = "SELECT * FROM employees_salary"
   df_employees_salary = pd.read_sql(employees_salary_sql, engine_cloud)
   print(df_employees_salary)

   print("")
   print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   print("Statistical Analysis of Bonus and Salary for Employees")
   print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   print("")

   # Avergae Salaries by Department
   merged_df = pd.merge(df_employees_salary,df_employees, on='id')
   avg_salaries = merged_df.groupby('department')['salary'].mean()
   print("+++++++++++++++++++++++++++++++")
   print("Avergae Salaries Per Department")
   print("+++++++++++++++++++++++++++++++")
   print(avg_salaries)

   # Average Bonus by Department
   avg_bonuses = merged_df.groupby('department')['bonus'].mean()
   print("++++++++++++++++++++++++++++")
   print("Avergae Bonus Per Department")
   print("++++++++++++++++++++++++++++")
   print(avg_bonuses)

   # Get the mean, median, standard deviation, and other statistics for the salary column in df_employees_salary
   salary_stats = df_employees_salary['salary'].describe()
   print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   print("Mean, median, standard deviation, and other statistics for Salary")
   print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   print(salary_stats)

   # Calculate the correlation matrix between the salary and bonus columns in df_employees_salary
   corr_matrix = df_employees_salary[['salary', 'bonus']].corr()
   print("+++++++++++++++++++++++++++++++++++++++++++++++")
   print("Correlation matrix between the salary and bonus")
   print("+++++++++++++++++++++++++++++++++++++++++++++++")
   print(corr_matrix)


except SQLAlchemyError as e:
   print(e)
