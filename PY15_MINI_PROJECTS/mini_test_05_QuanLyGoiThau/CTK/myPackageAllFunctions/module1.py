def function1():
    print("This is function1 from module1")

def function2():
    print("This is function2 from module1")
    
# ======================================================================================
# SAVE_DEFAUL_SETTING
# ======================================================================================
def SAVE_DEFAUL_SETTING(variable_01, variable_02):
    with open(r"json\1_set_defaul.txt",'w',encoding = 'utf-8') as f:
        f.write(f"Mode: {variable_01}\n")
        f.write(f"Theme: {variable_02}")