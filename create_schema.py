#------------------------------------------------------------------------------
# Copyright (c) 2025, Oracle and/or its affiliates.
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

import oracledb

un = os.environ.get('ORACLE_USER')
pw = os.environ.get('ORACLE_PASSWORD')
cs = os.environ.get('ORACLE_DSN')

def run_sql_script(conn, script_name):
    statement_parts = []
    cursor = conn.cursor()
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_name = os.path.join(script_dir, script_name)
    for line in open(file_name):
        if line.strip() == "/":
            statement = "".join(statement_parts).strip()
            if statement:
                try:
                    cursor.execute(statement)
                except:
                    print("Failed to execute SQL:", statement)
                    raise
            statement_parts = []
        else:
            statement_parts.append(line)

connection = oracledb.connect(user=un, password=pw, dsn=cs)

run_sql_script(connection, "cleanup.sql")
run_sql_script(connection, "schema.sql")
