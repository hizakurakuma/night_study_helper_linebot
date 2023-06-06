from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,LocationSendMessage,StickerSendMessage,QuickReply,QuickReplyButton,MessageAction,ImageSendMessage,PostbackEvent,PostbackAction,PostbackTemplateAction,ConfirmTemplate,TemplateSendMessage,ButtonsTemplate,URIAction,CarouselTemplate,CarouselColumn,ImageCarouselTemplate,ImageCarouselColumn,FlexSendMessage
)
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(' MY_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('MY_CHANNEL_SECRET')