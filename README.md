# Statistical Analysis with Oracle Database, Pandas, Matplotlib, and Seaborn

This project contains Python code that utilizes the Matplotlib and Seaborn libraries for data visualization.


## Setup

This project requires the following libraries:

```
pandas
pyarrow
oracledb>=3.3
matplotlib
seaborn
```

### Clone the Github Repo

```
git clone https://github.com/oracle-quickstart/pandas-oracledb-statistical-analysis.git

cd pandas-oracledb-statistical-analysis/
```

## Running Locally

### Install Dependencies
```
python -m pip install -r requirements.txt
```

#### Set the environment variables to connect to Oracle Database
```
export ORACLE_USER=username
export ORACLE_PASSWORD=password
export ORACLE_DSN='(description=(address=(protocol=tcps)(port=1521)(host=adb.ap-melbourne-1.oraclecloud.com))(connect_data=(service_name=*******_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'
```

#### Seed the Schema
```
python create_env.py
```

Note this drops and recreates several tables and procedures.

### Run using CLI

Set the environment variables as shown above and run:

```
python pandas-data.py
```

### Run using GUI

Set the environment variables as shown above and run:

```
python pandas-charts.py
```

#### Visualization

<img width="782" alt="Screen Shot 2023-03-13 at 5 26 25 pm" src="https://user-images.githubusercontent.com/39692236/224623817-7c13012a-e5c8-460f-8b33-dbb464e32722.png">

<img width="777" alt="Screen Shot 2023-03-13 at 5 26 34 pm" src="https://user-images.githubusercontent.com/39692236/224623834-39a0d7a3-e351-427c-bbe9-2831051b335d.png">

<img width="781" alt="Screen Shot 2023-03-13 at 5 26 43 pm" src="https://user-images.githubusercontent.com/39692236/224623847-9261ed4d-863f-472e-94c9-f8d83f814fc7.png">

<img width="774" alt="Screen Shot 2023-03-13 at 5 26 51 pm" src="https://user-images.githubusercontent.com/39692236/224623880-7f34ef6f-3e6c-4628-8a1b-a3018ebcdcc0.png">


## Running in a Container

Set the environment variables as shown above and run:

```
podman build \
--build-arg ORACLE_USER=$ORACLE_USER \
--build-arg ORACLE_PASSWORD=$ORACLE_PASSWORD \
--build-arg ORACLE_DSN=$ORACLE_DSN -t oraclepandasdemo .

podman run -it \
-e ORACLE_USER=$ORACLE_USER \
-e ORACLE_PASSWORD=$ORACLE_PASSWORD \
-e ORACLE_DSN=$ORACLE_DSN oraclepandasdemo
```

**Important Note: Visualization from the Pandas dataframes works only from a local install and not in the container**

## Contributing

This project welcomes contributions from the community. Before submitting a pull request, please [review our contribution guide](./CONTRIBUTING.md)

## Security

Please consult the [security guide](./SECURITY.md) for our responsible security vulnerability disclosure process

## License

Copyright (c) 2023, 2025 Oracle and/or its affiliates.

Released under the Apache License version 2.0 as shown at
<http://www.apache.org/licenses/>.
