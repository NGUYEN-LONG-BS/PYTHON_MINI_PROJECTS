import os

WINDOW_WIDTH            = 600
WINDOW_HEIGHT           = 400
WINDOW_POSITION_RIGHT   = 400
WINDOW_POSITION_DOWN    = 200

COLOR_BLACK             = "#726461"
COLOR_RED               = "#ff3333"
COLOR_BLUE              = "#53D4F7"
COLOR_GREEN             = "#00b359"
COLOR_WHITE             = "#ffffff"
COLOR_PURPLE            = "#a64dff" 
COLOR_YELLOW            = "#ffff00"
COLOR_BACKGROUND        = "#E2F7B5"

Login_user_name_root = 'root'
Login_pass_root = 'Ta#9999'
Login_host = 'localhost'   # 3306

PATH_DIRECTORY          = os.path.dirname(__file__)
PATH_IMAGES             = os.path.join(PATH_DIRECTORY, 'images')
PATH_QLSV_TXT           = os.path.join(PATH_DIRECTORY, 'QLSV.txt')

#Khởi tạo database mới
code='CREATE DATABASE `DB_USER_ID` ;' # 'CREATE SCHEMA `test` ;'

#Khởi tạo bảng mới
Code_Create_Table_01 =  "CREATE TABLE `db_user_id`.`tb_list_chi_nhanh` (" + \
                            "`ID` INT NOT NULL AUTO_INCREMENT," + \
                            "`MA_CHI_NHANH` VARCHAR(45) NOT NULL," + \
                            "`TEN_CHI_NHANH` VARCHAR(45) NOT NULL," + \
                            "PRIMARY KEY (`ID`)," + \
                            "UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE);"

Code_Create_Table_02 =  "CREATE TABLE `db_user_id`.`tb_list_chi_nhanh` (" + \
                            "`ID` INT NOT NULL AUTO_INCREMENT," + \
                            "`MA_CHI_NHANH` VARCHAR(45) NOT NULL," + \
                            "`TEN_CHI_NHANH` VARCHAR(45) NOT NULL," + \
                            "PRIMARY KEY (`ID`)," + \
                            "UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE);"