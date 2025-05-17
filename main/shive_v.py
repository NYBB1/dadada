import configparser
import re
import json
import os
import mysql.connector
from django.http import JsonResponse
from hdfs import InsecureClient
from pyhive import hive
import csv
from util.configread import config_read
from util.CustomJSONEncoder import CustomJsonEncoder
from util.codes import normal_code, system_error_code
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format
import shutil
# 获取当前文件路径的根目录
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

m_username = "Administrator"
hadoop_client = InsecureClient('http://localhost:9870', user='hadoop')

dbtype, host, port, user, passwd, dbName, charset,hasHadoop = config_read(os.path.join(parent_directory,"config.ini"))

#将mysql里的相关表转成hive库里的表
def migrate_to_hive():

    mysql_conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=passwd,
        database=dbName
    )
    cursor = mysql_conn.cursor()

    hive_conn = hive.Connection(
        host='localhost',
        port=10000,
        username=m_username,
    )
    hive_cursor = hive_conn.cursor()
    #创建Hive数据库（如果不存在）
    hive_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbName}")
    hive_cursor.execute(f"USE {dbName}")

    examresults_table_path=f'/user/hive/warehouse/{dbName}.db/examresults'
    #删除已有的hive表
    if hadoop_client.status(examresults_table_path,strict=False):
        hadoop_client.delete(examresults_table_path, recursive=True)
    # 在Hive中删除表
    examresults_drop_table_query = f"""DROP TABLE examresults"""
    hive_cursor.execute(examresults_drop_table_query)
    cursor.execute("SELECT * FROM examresults")
    examresults_column_info = cursor.fetchall()
    #将数据写入 CSV 文件
    examresults_path = os.path.join(parent_directory, "examresults.csv")
    with open(examresults_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入数据行
        for row in examresults_column_info:
            writer.writerow(row)
    examresults_spakr_clear(examresults_path)
    cursor.execute("DESCRIBE examresults")
    examresults_column_info = cursor.fetchall()
    create_table_query = "CREATE TABLE IF NOT EXISTS examresults ("
    for column, data_type, _, _, _, _ in examresults_column_info:
        match = re.match(r'(\w+)(\(\d+\))?', data_type)
        mysql_type = match.group(1)
        hive_data_type = get_hive_type(mysql_type)
        create_table_query += f"{column} {hive_data_type}, "
    examresults_create_table_query = create_table_query[:-2] + ") row format delimited fields terminated by ','"
    hive_cursor.execute(examresults_create_table_query)
    # 上传映射文件
    examresults_hdfs_csv_path = f'/user/hive/warehouse/{dbName}.db/examresults'
    hadoop_client.upload(examresults_hdfs_csv_path, examresults_path)
    cursor.close()
    mysql_conn.close()
    hive_cursor.close()
    hive_conn.close()

#转换成hive的类型
def get_hive_type(mysql_type):
    type_mapping = {
        'INT': 'INT',
        'BIGINT': 'BIGINT',
        'FLOAT': 'FLOAT',
        'DOUBLE': 'DOUBLE',
        'DECIMAL': 'DECIMAL',
        'VARCHAR': 'STRING',
        'TEXT': 'STRING',
    }
    if isinstance(mysql_type, str):
        mysql_type = mysql_type.upper()
    return type_mapping.get(str(mysql_type), 'STRING')

#执行hive查询
def hive_query():
    # 连接到Hive服务器
    conn = hive.Connection(host='localhost', port=10000, username=m_username,database=dbName)
    # 创建一个游标对象
    cursor = conn.cursor()
    try:

        #定义Hive查询语句
        gender_query = "SELECT COUNT(*) AS total, gender FROM examresults GROUP BY gender"
        # 执行Hive查询语句
        cursor.execute(gender_query)
        # 获取查询结果
        gender_results = cursor.fetchall()
        gender_json_list=[]
        for row in gender_results:
            gender_json_list.append({"gender":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "examresults_groupgender.json"), 'w', encoding='utf-8') as f:
            json.dump(gender_json_list, f, ensure_ascii=False, indent=4)


        #定义Hive查询语句
        learningattitude_query = "SELECT COUNT(*) AS total, learningattitude FROM examresults GROUP BY learningattitude"
        # 执行Hive查询语句
        cursor.execute(learningattitude_query)
        # 获取查询结果
        learningattitude_results = cursor.fetchall()
        learningattitude_json_list=[]
        for row in learningattitude_results:
            learningattitude_json_list.append({"learningattitude":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "examresults_grouplearningattitude.json"), 'w', encoding='utf-8') as f:
            json.dump(learningattitude_json_list, f, ensure_ascii=False, indent=4)


        #定义Hive查询语句
        teachingmethod_query = "SELECT COUNT(*) AS total, teachingmethod FROM examresults GROUP BY teachingmethod"
        # 执行Hive查询语句
        cursor.execute(teachingmethod_query)
        # 获取查询结果
        teachingmethod_results = cursor.fetchall()
        teachingmethod_json_list=[]
        for row in teachingmethod_results:
            teachingmethod_json_list.append({"teachingmethod":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "examresults_groupteachingmethod.json"), 'w', encoding='utf-8') as f:
            json.dump(teachingmethod_json_list, f, ensure_ascii=False, indent=4)


        #定义Hive查询语句
        grade_query = "SELECT COUNT(*) AS total, grade FROM examresults GROUP BY grade"
        # 执行Hive查询语句
        cursor.execute(grade_query)
        # 获取查询结果
        grade_results = cursor.fetchall()
        grade_json_list=[]
        for row in grade_results:
            grade_json_list.append({"grade":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "examresults_groupgrade.json"), 'w', encoding='utf-8') as f:
            json.dump(grade_json_list, f, ensure_ascii=False, indent=4)

        where = ' WHERE 1 = 1 '
        studentid_query = f'''SELECT `studentid`, ROUND(SUM(`attendancerate`), 2) AS `total`
            FROM examresults {where} GROUP BY `studentid`'''
        #执行Hive查询语句
        cursor.execute(studentid_query)
        # 获取查询结果
        studentid_results = cursor.fetchall()
        studentid_json_list=[]
        for row in studentid_results:
            studentid_json_list.append({"studentid":row[0],"total":row[1]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "examresults_valuestudentidattendancerate.json"), 'w', encoding='utf-8') as f:
            json.dump(studentid_json_list, f, ensure_ascii=False, indent=4)
        pass
    except Exception as e:
         print(f"An error occurred: {e}")
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()

#spark数据清洗和预处理
def examresults_spakr_clear(csvpath):
    try:
        #创建Spark会话
        spark = SparkSession.builder.appName("django1qp26v7n").getOrCreate()
        df = spark.read.csv(csvpath, header=False, inferSchema=True)
        df = df.toDF(
            "id",
            "addtime",
            "studentid",
            "timeofenrollment",
            "examtime",
            "gender",
            "age",
            "politicalachievements",
            "chinesescores",
            "mathematicsgrades",
            "foreignlanguagescore",
            "achievement",
            "chemistrygrades",
            "geographyscore",
            "historicalachievements",
            "totalscore",
            "averagescore",
            "attendancerate",
            "homeworkcompletionrate",
            "learningattitude",
            "familybackground",
            "teachingmethod",
            "parentseducationallevel",
            "extracurriculartutoringsituation",
            "grade",
        )
        #显示原始数据
        df.show()
        #1.删除空值
        df_cleaned = df.dropna()
        #2.去除重复行
        df_cleaned = df_cleaned.dropDuplicates()
        df_cleaned = df_cleaned.withColumn("addtime", date_format(col("addtime"), 'yyyy-MM-dd HH:mm:ss'))
        df_cleaned = df_cleaned.withColumn("timeofenrollment", date_format(col("timeofenrollment"), 'yyyy-MM-dd'))
        df_cleaned = df_cleaned.withColumn("examtime", date_format(col("examtime"), 'yyyy-MM-dd'))
        #显示清洗后的数据
        df_cleaned.show()
        #保存清洗后的数据
        print(type(df_cleaned))
        output_path = 'examresults_output_dir'  # 输出的目录
        df_cleaned.coalesce(1).write.csv(output_path, header=False, mode="overwrite")
        #手动移动生成的 CSV 文件到目标路径，并重命名
        for filename in os.listdir(output_path):
            if filename.startswith("part-") and filename.endswith(".csv"):
                shutil.move(os.path.join(output_path, filename), csvpath)
        #清理临时目录
        shutil.rmtree(output_path)
        #停止Spark会话
        spark.stop()
    except Exception as e:
        print("e:",e)
    # hive分析
def shive_analyze(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        try:
            migrate_to_hive()
            hive_query()
            return JsonResponse(msg, encoder=CustomJsonEncoder)
        except Exception as e:
            msg['code'] = system_error_code
            msg['msg'] = f"发生错误：{e}"
            return JsonResponse(msg, encoder=CustomJsonEncoder)



