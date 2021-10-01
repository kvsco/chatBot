import pymysql
import pandas as pd

# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_DATABASE=homestead
# DB_USERNAME=homestead
# DB_PASSWORD=secret

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='12345',
        db='test',
        charset='utf8'
    )
    print("DB 연결 성공")

    # 데이터 삭제 sql 정의
    id = 11  # 데이터 id (PK)
    sql = '''
        DELETE from tb_student where id=%d
        ''' % id

    # 데이터 삭제
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()


except Exception as e:
    print("except!!")
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB 연결 닫기 성공")