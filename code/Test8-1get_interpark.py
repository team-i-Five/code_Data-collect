from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
import random

with DAG(
    # DAG 아이디 설정 
    dag_id="get_rank",
    # 하루마다 실행
    schedule_interval="@daily",
    # DAG 시작 시간 11월 15일에서 16로 넘어가는 새벽 1시에 시작.
    start_date=pendulum.datetime(2023, 11, 16, 1, 0, 0, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    # 첫번째 함수
    def get_rank():
    
        import os
        import pymysql
        import sqlalchemy
        from sqlalchemy import create_engine

        import requests
        from bs4 import BeautifulSoup
        import json
        import pandas as pd
        import time
        import datetime
        from datetime import datetime
        
        tmp_list = [] # 합칠 리스트 생성

        interpark_url = "https://tickets.interpark.com/contents/ranking?genre=musical"
        r_i = requests.get(url=interpark_url)
        html_i = r_i.content
        soup_i = BeautifulSoup(html_i, 'html.parser')

        # TOP3는 가장 위에 가로로 배열 -> tag_v
        # TOP4~10은 그 아래라 세로로 배열 -> tag_h
        tag_v = soup_i.findAll('div', class_="ranking-vertical-item_rankingItem__llUL_")
        tag_h = soup_i.findAll('ul', class_='ranking-horizontal-item_rankingContents__z3wFG')

        # 가로 TOP 3 리스트
        for i in range(len(tag_v)):
            name_v = tag_v[i].find('li', class_='ranking-vertical-item_rankingGoodsName__m0gOz').text
            date_v =tag_v[i].find('div', class_='ranking-vertical-item_dateWrap__uZGMU').text
            location_v = tag_v[i].find('li', class_='ranking-vertical-item_placeName__4sHRS').text
            img_v = tag_v[i].find('div', class_='ranking-vertical-item_imageWrap__R6lkF').find('img')["src"]
            id_v = img_v.split('%')[8].split('_')[0].split('F')[1]
            goods_v = f"https://tickets.interpark.com/goods/{id_v}"
            img_url_v = f"https://tickets.interpark.com{img_v}"
            
            v_dict = {
                'name': name_v,
                'date' : date_v,
                'location' : location_v,
                'img_url' : img_url_v,
                'goods' : goods_v
            }
            tmp_list.append(v_dict)

        # 세로 TOP 4~10 리스트
        for j in range(7):
            name_h = tag_h[j].find('li', class_='ranking-horizontal-item_rankingTicketTitle__omJYh').text
            date_h = date_h = tag_h[j].find('div', class_='ranking-horizontal-item_dateWrap__tRsWh').text
            location_h = tag_h[j].find('li', class_='ranking-horizontal-item_placeName__zb9kN').text
            img_h = tag_h[j].find('div', class_='ranking-horizontal-item_imageWrap__owTl6').find('img')['src']
            id_h = img_h.split('%')[8].split('_')[0].split('F')[1]
            goods_h = f"https://tickets.interpark.com/goods/{id_h}"
            img_url_h = f"https://tickets.interpark.com{img_h}"
            
            h_dict = {
                'name': name_h,
                'date' : date_h,
                'location' : location_h,
                'img_url' : img_url_h,
                'goods' : goods_h
            }
            tmp_list.append(h_dict)

        interpark_df = pd.DataFrame(tmp_list)

        # rank, site_name, update_date 컬럼 추가 및 컬럼 순서 변경
        interpark_df['rank'] = range(1, len(interpark_df) + 1)
        interpark_df['site_name'] = '인터파크'
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
        interpark_df['update_date'] = current_datetime
        interpark_df = interpark_df[['site_name', 'update_date', 'rank', 'name', 'date', 'location', 'img_url', 'goods']]
        
        # db 연결
        username = 'admin' 
        password = 'ifive1234'
        host='ifive-db.ckteh9hwnkjf.ap-northeast-2.rds.amazonaws.com'
        port = '3306' 
        database='ifive'

        engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
        
        interpark_df.to_sql(name='ranking', con=engine, if_exists='replace', index=False)
        
            
    # 첫번째 task
    
    py_t1 = PythonOperator(
            task_id='rank_t231113', #taskid
            python_callable=get_rank #task에서 실행할 파이썬 함수 설정
        )
    
    # 두번째 함수
    
    # 두번째 task
    
    # 세번쨰 함수
    
    # 세번째 task

    #py_t1 실행 후 py_t2 실행
    py_t1