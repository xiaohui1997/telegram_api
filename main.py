import telebot
TOKEN='619423079:AAFPQuGFbCwH8O3jSefntGa8rd0Tr_Wq_zs'
bot=telebot.TeleBot(TOKEN)

#用户名称提取
def botinfos(message):
    # 名称提取
    if message.from_user.first_name == None:
        firstname = ''
    else:
        firstname = message.from_user.first_name
    if message.from_user.last_name == None:
        lastname = ''
    else:
        lastname = message.from_user.last_name
    # 最终名称
    name = str(firstname) + str(lastname)
    #用户id获取
    userid=message.from_user.id
    #用户群组id获取
    groupid=message.chat.id
    #来自哪里,群或者私聊
    where=message.chat.type
    #获取群组名称
    groupname=message.chat.title
    #获取具体命令
    text=message.text
    #返回 用户名称,用户id,群id,来自群或者私人,群名称
    return {'name':name,'userid':userid,'groupid':groupid,'where':where,'groupname':groupname,'text':text}

#拉代码菜单
@bot.message_handler(commands=['lacode'])
def send_menu(message):
    #获取基本信息
    botinfo=botinfos(message)
    #只处理群消息
    if botinfo['where'] == 'group':
        bot.send_message(botinfo['userid'], '你好' + botinfo['name'] + ' 如需帮助请在群里联系我谢谢！')
    else:
    #开始处理群消息
        #菜单信息
        textinfo='''
无限
        /wx_back_houtai   拉取 无线后端后台代码 
        /wx_back_houtai   拉取 无线后端后台代码
无限1
        /wx_back_houtai   拉取 无线后端后台代码 
        /wx_back_houtai   拉取 无线后端后台代码
        '''
        bot.send_message(botinfo['userid'],textinfo)
        pass

    #bot.send_message(-342008533, '你好'+name+' 有什么可以帮到您的?')

#正式拉代码
@bot.message_handler(commands=None,regexp='.*_.*')
def lacode(message):
    # 获取基本信息
    botinfo = botinfos(message)
    # 只处理群消息
    if botinfo['where'] == 'group':
        bot.send_message(botinfo['userid'], '你好' + botinfo['name'] + ' 如需帮助请在群里联系我谢谢！')
    else:
    # 开始处理群消息
        print(botinfo['text'])



if __name__ == '__main__':
    bot.polling()


exit()



#所有消息捕获
@bot.message_handler()
def echo(message):
    bot.reply_to(message, '有问题请群里@我，我不回私人消息，抱歉。。。。')
a=''
#直接发送消息
bot.send_message(-3412008533, '<b>123123</b>',parse_mode='html')
#如果要退出请用exit()强制退出
#'https://api.telegram.org/bot619423079:AAFPQuGFbCwH8O3jSefntGa8rd0Tr_Wq_zs/sendMessage?chat_id=-342008533&text=123'
#"https://core.telegram.org/bots"
#选择菜单，默认以私聊的形式回复你
from telebot import types
# markup = types.ReplyKeyboardMarkup(row_width=2)
# itembtn1 = types.KeyboardButton('a')
# itembtn2 = types.KeyboardButton('v')
# itembtn3 = types.KeyboardButton('d')
# markup.add(itembtn1, itembtn2, itembtn3)
#
# bot.send_message(-342008533, "Choose one letter:", reply_markup=markup)

keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton('12345', callback_data="getUsers"))

bot.send_message(-342008533, "Choose one letter:", reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def private_query(query):
    if(query.data=="getUsers"):                                        #'https://pastebin.com/9FmMbk3c'
        bot.send_message(-342008533, '<b>123123</b>',parse_mode='html')
