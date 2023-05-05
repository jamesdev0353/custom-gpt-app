# insall pyrogram
# install openai
import re
import asyncio
import os
import openai
# from pyrogram import filters, Client
# 


class BravoSis:
    #i'm not going through basics

    def __init__(self):
        # self.api_id = 7880410
        # self.api_hash = "72fb94902bbee2b74318b3d499c1096e"
        # self.bot_token = "" 
        # leosscreation@gmail.com
        self.openai_api_key = "" # set your own api value
        # snm20cs.muhammedroshanps@gmail.com
        # self.openai_api_key = "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" #get this value from https://beta.openai.com/.
        self.model = "text-davinci-003" # use any of these [text-davinci-002,text-davinci-001]
        self.mxtoken = 1080 #can decrese/increse with reaspect to result previlage


    def ai(self,query):
        openai.api_key = self.openai_api_key
        completion = openai.Completion.create(engine=self.model, prompt=query, max_tokens=self.mxtoken, n=1, stop=None,temperature=0.7)
        result = completion.choices[0].text
        return result


# wow = BravoSis()


# LeosBot = Client(name="XhatGpt",api_id=wow.api_id ,api_hash=wow.api_hash)

# @LeosBot.on_message(filters.text & ~filters.group)
# async def main(bot):
#     dumbchannel = -1001878347911
#     wow = await ai(ques)
#     dumb_test = f"#USER{newbie} #Q| {ques} |   `{wow}`"
#     await bot.send_message(dumbchannel,dumb_test)
#     await asyncio.sleep(1)