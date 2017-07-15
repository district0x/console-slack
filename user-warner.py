from slacker import Slacker

slack = Slacker('<XOXPTOKENHERE>')

def get_users():
    global slack
    return [user for user in slack.users.list().body['members'] if user['deleted'] is False]


users = get_users()

user_whitelist = []
user_blacklist = ['alexander', 'joe', 'matus', 'urgo', 'madvas', 'joeyurgz', 'district0x', 'vip', 'group', 'official', 'district', '0x', 'distrit', 'distric', 'ditrict', 'district0', 'distric0x', 'diistrict0x', 'd0x', 'disrict0x'] # truncated
id_whitelist = ['U0PDFC7EX', 'U0PF69M34']
for user in users:
    name = user['name']
    if name not in user_whitelist:
        for b in user_blacklist:
            if b in name:
                if user['id'] not in id_whitelist:
                    slack.chat.post_message('@{}'.format(name), 'Hi, in an effort to protect against scammers and fraud, please change your username to not include "district0x", "vip", "official" or be similar to "alexander", "madvas" or "joe". This is an automated message and you will be banned by end of day if your username is not changed. Thank you for understanding.', as_user=True)
                    # print(name)
                    break
