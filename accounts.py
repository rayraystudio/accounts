import time

text = input("請輸入帳號：")
text = text.split("----")


account = text[0]
password = text[1]  

if text[3].isdigit():
    locate = 4

else:
    locate = 3

email = text[locate][3:]
email_pass = text[locate+1]
email_link = text[locate+2][5:]
print(f"""
-------------------------------------
您好，感謝您購買本店商品
以下為您的帳號資訊：
帳號：{account}
密碼：{password}
信箱：{email}
信箱密碼：{email_pass}
信箱網址：{email_link}
購買後請盡速更改綁定信箱及密碼並綁上手機，如出現帳號密碼錯誤，購買遊戲封鎖，請回報給客服
Discord客服：Ray Ray#0228
Discord官方售後群組：https://discord.gg/WdKC62836C
購買指定額度即可成為會員!享有各種限時折價活動、帳號抽獎，滿額會員還可領取免費帳號!
立即加入伺服器申請會員吧!
-------------------------------------
""")

time.sleep(10)

#839321116----xx7758520----ssfn895090427336812694----76561198357607321----邮箱：7zae6qyb@1688mail.online----6324FEF5----邮箱地址：www.618mail.com
#839321116----xx7758520----ssfn895090427336812694----邮箱：7zae6qyb@1688mail.online----6324FEF5----邮箱地址：www.618mail.com