import inspect

def f_find_my_function_path(function_name):
    source_file = inspect.getfile(function_name)
    print(f"Function is defined in: {source_file}")