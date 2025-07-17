#------------------------------------------------------------------------------
# Copyright (c) 2023, 2025, Oracle and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

import os
import sys

import pyarrow as pa
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import oracledb

# Set up database connection
un = os.environ.get('ORACLE_USER')
pw = os.environ.get('ORACLE_PASSWORD')
cs = os.environ.get('ORACLE_DSN')

connection = oracledb.connect(user=un, password=pw, dsn=cs)

# Read employees table
employees_sql = "SELECT * FROM employees"
odf = connection.fetch_df_all(statement=employees_sql)
df_employees = pa.table(odf).to_pandas()
print(df_employees)

# Read employees_salary table
employees_salary_sql = "SELECT * FROM employees_salary"
odf = connection.fetch_df_all(statement=employees_salary_sql)
df_employees_salary = pa.table(odf).to_pandas()
print(df_employees_salary)

print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Statistical Analysis of Bonus and Salary for Employees")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")

# Avergae Salaries by Department
merged_df = pd.merge(df_employees_salary,df_employees, on='ID')
avg_salaries = merged_df.groupby('DEPARTMENT')['SALARY'].mean()
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
output_file = "avg_salary.png"
plt.savefig(output_file, bbox_inches='tight', dpi=300)
plt.show()

# Average Bonus by Department
avg_bonuses = merged_df.groupby('DEPARTMENT')['BONUS'].mean()
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
output_file = "avg_bonus.png"
plt.savefig(output_file, bbox_inches='tight', dpi=300)
plt.show()

# Get the mean, median, standard deviation, and other statistics for the salary column in df_employees_salary
salary_stats = df_employees_salary['SALARY'].describe()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Mean, median, standard deviation, and other statistics for Salary")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(salary_stats)

# Plot distribution of Salary
plt.figure(figsize=(8,6))
sns.histplot(data=df_employees_salary, x='SALARY', kde=True)
plt.title('Distribution of Salary')
plt.xlabel('Salary')
plt.ylabel('Count')
output_file = "dist_salary.png"
plt.savefig(output_file, bbox_inches='tight', dpi=300)
plt.show()

# Calculate the correlation matrix between the salary and bonus columns in df_employees_salary
corr_matrix = df_employees_salary[['SALARY', 'BONUS']].corr()
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("Correlation matrix between the salary and bonus")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print(corr_matrix)

# Plot correlation matrix as heatmap
plt.figure(figsize=(8,6))
sns.heatmap(data=corr_matrix, cmap='coolwarm', annot=True)
plt.title('Correlation Matrix Heatmap')
output_file = "correlation_matrix.png"
plt.savefig(output_file, bbox_inches='tight', dpi=300)
plt.show()
