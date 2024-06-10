# Thông tin kết nối SQL-Server
# VAR_SQL_DRIVER = "{SQL Server Native Client 11.0}"                          # SQL Server version 2012-2014
# VAR_SERVER_NAME = "KSNB3\SQLEXPRESS"
# VAR_DATABASE_NAME = "DATABASE_USER_ID"
# VAR_UID_SQL_SERVER = "sa"
# VAR_PWD_SQL_SERVER = "Ta#9999"

VAR_SQL_DRIVER = "{SQL Server Native Client 11.0}"                          # SQL Server version 2012-2014
VAR_SERVER_NAME = "KSNB3\SQL2014"
VAR_DATABASE_NAME = "TBD_2024_240409"
VAR_UID_SQL_SERVER = "ketoantonghop"
VAR_PWD_SQL_SERVER = "Phamthikimanh1989"
VAR_UID_SQL_SERVER = "sa"
VAR_PWD_SQL_SERVER = "_!d96KjXvw'\\"

VAR_CONNECTION_STRING_TO_SQL_SERVER_WITH_WINDOWS_AUTHENTICATION = ("Driver= " + VAR_SQL_DRIVER + ";"       
                                                                    "Server=" + VAR_SERVER_NAME +";"
                                                                    "Database=" + VAR_DATABASE_NAME +";"
                                                                    "Trusted_Connection=yes; ")

VAR_CONNECTION_STRING_TO_SQL_SERVER_WITH_SQL_SERVER_AUTHENTICATION = ("Driver= " + VAR_SQL_DRIVER + ";"       
                                                                    "Server=" + VAR_SERVER_NAME +";"
                                                                    "Database=" + VAR_DATABASE_NAME +";"
                                                                    "UID=" + VAR_UID_SQL_SERVER +";"
                                                                    "PWD=" + VAR_PWD_SQL_SERVER +";"
                                                                    "Trusted_Connection=no; ")


# Câu lệnh query
VAR_SQL_QUERY_01 = "select * from TB_DS_DATABASE"
VAR_SQL_QUERY_02 = "select * from BADepositDetail"