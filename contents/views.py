from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
import os, sys, requests, csv
from django.http import HttpResponseForbidden, HttpResponse
import pathlib
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, FollowEvent, UnfollowEvent,
    TextSendMessage, ImageMessage, AudioMessage
)




from .management.commands import xyz

from linebot import LineBotApi, WebhookHandler
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
current_dir22 = pathlib.Path(__file__).parents[1].joinpath('config', '.env')
load_dotenv(str(current_dir22))




line_channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(line_channel_secret)

# Create your views here.

# 確認用view
def index(request):
    # pro="U4af4980629"
    # print(xyz.Gsheet_save([pro]))
    return HttpResponse(123)



#
# @handler.add(FollowEvent)
# def handle_follow(event):
#     """
#     友だち追加したときのイベント。
#     UsersDBにIDと性別、アクティビティを追加。
#     """
#     UserID = event.source.user_id
#     users_DB.add(UserID)
#     buttons_template = ButtonsTemplate(
#         title='友達追加ありがとう！', text='まず、あなたの性別を教えてください!', actions=[
#             PostbackAction(label='男', data='male'),
#             PostbackAction(label='女', data='female'),
#         ])
#     template_message = TemplateSendMessage(alt_text='友達追加ありがとう！\nまず、あなたの性別を教えてください。', template=buttons_template)
#     line_bot_api.reply_message(event.reply_token, template_message)
#


@csrf_exempt
def callback(request):
    # signatureの取得
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        # 署名の検証を行い、成功した場合にhandleされたメソッドを呼び出す
        handler.handle(body, signature)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    return HttpResponse('OK')


# フォローイベントの場合の処理
@handler.add(FollowEvent)
def handle_follow(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    print(xyz.Gsheet_save([profile.user_id]))
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=profile.user_id)
    )
    
    
# @handler.add(UnfollowEvent)
# def handle_unfollow(event):
#     """
#     ブロックされた時のイベント。
#     UsersDBのIDと性別、アクティビティを削除。
#     ＜TODO＞　QuestionDBの投稿を削除。
#     """
#     UserID = event.source.user_id
#     users_DB.remove(UserID)

# メッセージイベントの場合の処理
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # メッセージでもテキストの場合はオウム返しする
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="わっふる、わっふる")
    )