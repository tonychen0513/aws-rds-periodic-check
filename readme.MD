# AWS RDS Periodic Check Demo


## How to Run
1. Download the dependency of the python codes in the /src folder:

    pip install -r requirements.txt

2. Package all contents in the /src folder into a zip file "source.zip" and upload it to a S3 bucket.

3. Run the following command in AWS Cli to deploy the yml file:

    aws cloudformation deploy \
    --template-file mysql-sample-function.yml \
    --stack-name mysql-sample-function \
    --parameter-overrides MysqlSamplePackage=source.zip ...

