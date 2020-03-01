from ress_db import RessDb, db_Read_Endpoint, db_Write_Endpoint


def lambda_handler(request, _):
    try:
        with RessDb.readwrite() as db:
            print("Successfully connected to write DB endpoint " + db_Write_Endpoint)
    except Exception as error:
        print("Exception raised in connecting to write DB endpoint " + str(error))

    try:
        with RessDb.readonly() as db:
            print("Successfully connected to read DB endpoint " + db_Read_Endpoint)
    except Exception as error:
        print("Exception raised in connecting to read DB endpoint " + str(error))
