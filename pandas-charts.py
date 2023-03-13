import os
import sys

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

import oracledb

oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb

# Set up database connection
user = os.environ['ORACLE_USER']
password = os.environ['ORACLE_PASSWORD']
dsn = os.environ['ORACLE_DSN']

engine_cloud = create_engine(f'oracle://{user}:{password}@{dsn}')

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

   # Plot Average Salaries per Department
   plt.figure(figsize=(8,6))
   sns.barplot(x=avg_salaries.index, y=avg_salaries.values)
   plt.title('Average Salaries per Department')
   plt.xlabel('Department')
   plt.ylabel('Average Salary')
   plt.show()

   # Average Bonus by Department
   avg_bonuses = merged_df.groupby('department')['bonus'].mean()
   print("++++++++++++++++++++++++++++")
   print("Avergae Bonus Per Department")
   print("++++++++++++++++++++++++++++")
   print(avg_bonuses)

   # Plot Average Bonus per Department
   plt.figure(figsize=(8,6))
   sns.barplot(x=avg_bonuses.index, y=avg_bonuses.values)
   plt.title('Average Bonus per Department')
   plt.xlabel('Department')
   plt.ylabel('Average Bonus')
   plt.show()

   # Get the mean, median, standard deviation, and other statistics for the salary column in df_employees_salary
   salary_stats = df_employees_salary['salary'].describe()
   print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   print("Mean, median, standard deviation, and other statistics for Salary")
   print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   print(salary_stats)

   # Plot distribution of Salary
   plt.figure(figsize=(8,6))
   sns.histplot(data=df_employees_salary, x='salary', kde=True)
   plt.title('Distribution of Salary')
   plt.xlabel('Salary')
   plt.ylabel('Count')
   plt.show()

   # Calculate the correlation matrix between the salary and bonus columns in df_employees_salary
   corr_matrix = df_employees_salary[['salary', 'bonus']].corr()
   print("+++++++++++++++++++++++++++++++++++++++++++++++")
   print("Correlation matrix between the salary and bonus")
   print("+++++++++++++++++++++++++++++++++++++++++++++++")
   print(corr_matrix)

   # Plot correlation matrix as heatmap
   plt.figure(figsize=(8,6))
   sns.heatmap(data=corr_matrix, cmap='coolwarm', annot=True)
   plt.title('Correlation Matrix Heatmap')
   plt.show()

except SQLAlchemyError as e:
   print(e)
