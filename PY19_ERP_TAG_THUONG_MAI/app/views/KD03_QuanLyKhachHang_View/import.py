
import pyodbc

def insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array):
    """
    Hàm kết nối SQL Server và chèn dữ liệu từ mảng vào bảng.
    
    :param server_name: Tên hoặc địa chỉ IP của máy chủ SQL Server.
    :param database_name: Tên cơ sở dữ liệu.
    :param login_name: Tên người dùng SQL Server.
    :param login_pass: Mật khẩu SQL Server.
    :param table_name: Tên bảng trong cơ sở dữ liệu.
    :param data_array: Mảng chứa dữ liệu cần chèn (list of lists).
    """
    # Kết nối đến SQL Server
    connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};UID={login_name};PWD={login_pass}"
    try:
        conn = pyodbc.connect(connection_string)
        # print("Kết nối thành công đến cơ sở dữ liệu.")
    except Exception as e:
        print("Lỗi khi kết nối:", e)
        return
    
    cursor = conn.cursor()
    
    # Lấy danh sách cột của bảng
    try:
        cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")
        columns = [column[0] for column in cursor.description]  # Lấy tên cột
        print("Danh sách cột trong bảng:", columns)
    except Exception as e:
        print("Lỗi khi lấy thông tin bảng:", e)
        return

    # Kiểm tra số cột trong bảng khớp với số cột trong dữ liệu
    num_columns = len(columns)
    if not all(len(row) == num_columns for row in data_array):
        print("Dữ liệu không khớp số cột của bảng.")
        return

    # Chèn dữ liệu
    try:
        placeholders = ", ".join(["?" for _ in range(num_columns)])  # Tạo chuỗi placeholder "?, ?, ?"
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        
        for row in data_array:
            cursor.execute(query, row)
        
        conn.commit()
        # print("Dữ liệu đã được chèn thành công.")
    except Exception as e:
        print("Lỗi khi chèn dữ liệu:", e)
    finally:
        cursor.close()
        conn.close()
        print("Kết nối đã được đóng.")


if __name__ == "__main__":
    server_name = "14.225.192.238, 1433"  # Địa chỉ IP của SQL Server
    database_name = "TEST_NE_TU_TD"
    login_name = "sa"
    login_pass = "Ta#9999"
    table_name = "ID_INFO"

    # Dữ liệu cần chèn (mỗi danh sách bên trong là một dòng dữ liệu)
    data_array = [
        ["4", "Alice", 25],
        ["1", "Bob", 30],
        ["2", "Charlie", 35]
    ]
    
    insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array)
