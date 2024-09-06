import telepot

# 봇 API와 사용자 ID 설정
token = '7240374983:AAFEAeYlxEFLIaUzeGRVT-OumAk7FjLbIhA'  # 봇 API 토큰 입력
mc = '7265170310'  # 텔레그램 숫자 ID 입력

# 봇 객체 생성
bot = telepot.Bot(token)

# 메시지 전송
bot.sendMessage(mc, "안녕하세요")
