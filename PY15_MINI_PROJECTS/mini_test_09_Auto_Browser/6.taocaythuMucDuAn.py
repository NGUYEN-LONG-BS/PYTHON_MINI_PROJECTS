import os

def create_project_structure(base_path, structure):
    """
    Hàm tạo cây thư mục dựa trên cấu trúc đã định nghĩa.
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # Nếu là dictionary, tạo thư mục
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)  # Đệ quy để tạo cấu trúc con
        else:  # Nếu không phải dictionary, tạo file
            os.makedirs(os.path.dirname(path), exist_ok=True)  # Đảm bảo thư mục cha tồn tại
            with open(path, "w") as f:
                f.write(content)  # Viết nội dung file (nếu có)


# Cấu trúc cây thư mục
project_structure = {
    "my_project": {
        "main.py": "# Entry point of the application\n\nif __name__ == '__main__':\n    print('Application started!')",
        "requirements.txt": "# List of required libraries\ncustomtkinter\npyodbc",
        "app": {
            "__init__.py": "# App module initialization",
            "models": {
                "__init__.py": "# Models module initialization",
                "database.py": "# Database connection and logic",
            },
            "views": {
                "__init__.py": "# Views module initialization",
                "gui.py": "# GUI logic using CustomTkinter or Tkinter",
            },
            "controllers": {
                "__init__.py": "# Controllers module initialization",
                "app_controller.py": "# Main application logic controller",
            },
            "services": {
                "__init__.py": "# Services module initialization",
                "api_service.py": "# API and background services",
            },
            "utils": {
                "__init__.py": "# Utilities module initialization",
                "helpers.py": "# Shared utility functions",
            },
        },
        "tests": {
            "__init__.py": "# Test module initialization",
            "test_app.py": "# Test cases for the application",
        },
        "README.md": "# Project Documentation\n\nThis is a sample project structure for a Python application.",
    }
}

# Thư mục gốc nơi bạn muốn tạo cây thư mục
base_path = r"C:\Users\ADMIN\Desktop"  # Đường dẫn tuyệt đối

# Tạo cây thư mục
create_project_structure(base_path, project_structure)
print(f"Project structure created at: {base_path}")
