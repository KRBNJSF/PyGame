# Install pip so you can install packages -> import requests
import requests
import time

# Message you want to send
payload = {
    'content': "test"
}

# Send message on Discord Web app, F12 -> Network -> message -> Headers -> Request Headers -> authorization
header = {
    'authorization': 'NDg5ODA2Nzk5MzQwMzA2NDM2.GsL6uS.N32nFiJobCu4t86hlYzCybPNK8dAacUBL29drM'
}

for i in range(10):
    # Send message on Discord Web app, F12 -> Network -> message -> Headers -> General -> Request URL
    request = requests.post('https://discord.com/api/v9/channels/630077690959101984/messages',
                            data=payload, headers=header)
    time.sleep(0.5)
