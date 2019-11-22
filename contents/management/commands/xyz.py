import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials



def Gsheet_base():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    # 認証情報設定
    #  ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
    #  credentials = ServiceAccountCredentials.from_json_keyfile_name('config/linebot-api-2f3180c6c407.json', scope)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('config/linebot-api-2f3180c6c407.json', scope)
    
    # OAuth2の資格情報を使用してGoogle APIにログインします。
    gc = gspread.authorize(credentials)
    
    # 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
    # https://docs.google.com/spreadsheets/d/17Fo666Y2UQkA2NRTw4eoAX51_szm1bJDA9N8fyKY0U4/edit#gid=0
    GOOGLE_SPREADSHEET_KEY = os.getenv('SPREADSHEET_KEY', None)
    
    # 共有設定したスプレッドシートのシート1を開く
    worksheet = gc.open_by_key(GOOGLE_SPREADSHEET_KEY).sheet1
    
    return worksheet
    
    # A1セルの値を受け取る
    # import_value = int(worksheet.acell('A1').value)
    
    # A1セルの値に100加算した値をB1セルに表示させる
    # cell1 = 1
    # cell2 = 2
    # for i in range(0,import_value):
    #     worksheet.update_cell(cell1,cell2,i)
    #     cell1+=1
def Gsheet_save(profile):
    # 取得した情報を対象の列に順番に入力保存
    for i in range(profile):
        # worksheet.append_row(i)"""うまく動かん"""
        xx = Gsheet_base().col_values(2)
        Gsheet_base().update_cell(len(xx) + 1, 2, i)