import pyodbc
import datetime
#Define Connection String'
sqlDbConn = pyodbc.connect(
    "Driver= {SQL Server Native Client 11.0};"      # SQL Server version 2012-2014
    "Server=KSNB3\SQLEXPRESS;"
    "Database=DATABASE_USER_ID;"
    "Trusted_Connection=yes; ")

def getData(sqlDbConn):
    print("Read")
    cursor = sqlDbConn.cursor(); 
    cursor.execute("select * from TB_DS_DATABASE")
    for row in cursor:
        print(f'{row}')

getData(sqlDbConn);                 # Bước 1: Read: kết nối đến SQL Server và lấy dữ liệu về

def insertData(sqlDbConn):          # Bước 2: Create: thêm dữ liệu vào bảng
    print("Insert")
    cursor = sqlDbConn.cursor()
    cursor.execute(
        'insert into TB_DS_DATABASE (MA_DATABASE, TEN_DATABASE, TEN_SERVER, LOAI_DATABASE, XOA_DIEU_CHINH, NGAY_KHOI_TAO) values(?,?,?,?,?,?)', 
        ('LONG24', 'NGUYEN_LONG24', '', '', '', datetime.datetime(2024, 1, 4, 9, 13, 47)))
    sqlDbConn.commit()
    
insertData(sqlDbConn)   
getData(sqlDbConn)

def updateData(sqlDbConn):          # Bước 3: Update: cập nhật (sửa) dữ liệu có sẵn trong bảng
    print("Update")
    cursor = sqlDbConn.cursor();
    cursor.execute(
        'update TB_DS_DATABASE set TEN_DATABASE = ? where MA_DATABASE = ?', 
        ('NGUYEN_LONG_23_UPDATE', 'LONG24')) 
    sqlDbConn.commit()
    
updateData(sqlDbConn)   
getData(sqlDbConn)

def deleteData(sqlDbConn):          # Bước 4: Delete: Xoá dữ liệu đã có trong bảng
    print("Delete")
    cursor = sqlDbConn.cursor();
    cursor.execute(
        'delete from TB_DS_DATABASE where MA_DATABASE = ?',
        ('LONG24'))
    sqlDbConn.commit()
    
deleteData(sqlDbConn)   
getData(sqlDbConn)
