# Statistical Analysis with Oracle Database, Pandas, Matplotlib and Seaborn

This project contains Python code that utilizes the Matplotlib and Seaborn libraries for data visualization.

# Usage

This project requires the following libraries:

```
pandas
sqlalchemy<2.0
oracledb
matplotlib
seaborn
```

## Run without GUI

### Clone the Github Repo

```
git clone https://github.com/oracle-quickstart/pandas-oracledb-statistical-analysis.git

cd pandas-oracledb-statistical-analysis/
```

### Set the environment variables to connect to Oracle Database
```
export ORACLE_USER=username
export ORACLE_PASSWORD=password
export ORACLE_DSN='(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.ap-melbourne-1.oraclecloud.com))(connect_data=(service_name=*******_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'
```

### Seed the Schema
```
sql $ORACLE_USER/$ORACLE_PASSWORD@$ORACLE_DSN

@schema.sql
```

### Generate Sample Employee Data
```
BEGIN
    add_employees(5000); -- generate 5k random employees
END;
/
```

### Generate Sample Employee Salary Data
```
BEGIN
  generate_employees_salary(5000); -- generate 5k random employee salary/bonus records
END;
/
```


### Build from Source

```
podman build -t oraclepandasdemo .

podman run -it \
-e ORACLE_USER=admin \
-e ORACLE_PASSWORD=YourPassword234#_ \
-e ORACLE_DSN="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.ap-melbourne-1.oraclecloud.com))(connect_data=(service_name=****_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))" oraclepandasdemo

```


## Run using GUI


# Install Dependencies
```
pip3 install -r requirements.txt
```

# Set the environment variables to connect to Oracle Database
```
export ORACLE_USER=username
export ORACLE_PASSWORD=password
export ORACLE_DSN='(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.ap-melbourne-1.oraclecloud.com))(connect_data=(service_name=*******_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'
```

# Execute Python Script
```
python3 pandas-charts.py
```

## Visualization 

<img width="782" alt="Screen Shot 2023-03-13 at 5 26 25 pm" src="https://user-images.githubusercontent.com/39692236/224623817-7c13012a-e5c8-460f-8b33-dbb464e32722.png">

<img width="777" alt="Screen Shot 2023-03-13 at 5 26 34 pm" src="https://user-images.githubusercontent.com/39692236/224623834-39a0d7a3-e351-427c-bbe9-2831051b335d.png">

<img width="781" alt="Screen Shot 2023-03-13 at 5 26 43 pm" src="https://user-images.githubusercontent.com/39692236/224623847-9261ed4d-863f-472e-94c9-f8d83f814fc7.png">

<img width="774" alt="Screen Shot 2023-03-13 at 5 26 51 pm" src="https://user-images.githubusercontent.com/39692236/224623880-7f34ef6f-3e6c-4628-8a1b-a3018ebcdcc0.png">


#### Important Note : Visualization of the Pandas dataframes currently work only from Python3 and not Docker

## Contributing

This project welcomes contributions from the community. Before submitting a pull request, please [review our contribution guide](./CONTRIBUTING.md)

## Security

Please consult the [security guide](./SECURITY.md) for our responsible security vulnerability disclosure process

## License

Copyright (c) 2023 Oracle and/or its affiliates.

Released under the Apache License version 2.0 as shown at
<http://www.apache.org/licenses/>.
