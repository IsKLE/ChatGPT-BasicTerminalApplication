import openai
import utility.my_utility as mu
from utility.json_utility import JsonPacker
from utility.configer import Configer

# 定义文件路径
config_path = "assets\\gptConfig.json"
history_path = "assets\\chatHistory.json"
# 获取文件配置
gptConfig = Configer(config_path=config_path)
history = Configer(history_path=history_path).history_obj
# 设置API-KEY
openai.api_key = gptConfig.api_key
# 定义数据存储变量
chat_index = 0
usable_token = 4096
# 历史记录整理器
historyPacker = JsonPacker(json_obj=history)
# 开始GPT程序
while True:
    # 对话计数加一
    chat_index += 1
    user_prompt = ''
    print("———————————", chat_index, "———————————")
    print("User：")
    # 用户单独输入“end”，结束输入
    while True:
        line = input()
        if line != 'end':
            user_prompt += line + '\r'
        else:
            break
    print("GPT：")
    # 第一次询问，需要同时传递系统与用户的数据；之后只需要传递用户的数据
    if chat_index == 1:
        # 处理系统与用户的输入并保存
        historyPacker.add_property("system", gptConfig.system_prompt)
        # 获取gpt回答
        response = mu.get_first_answer(system_prompt=gptConfig.system_prompt + gptConfig.language_type,
                                       user_prompt=user_prompt,
                                       model=gptConfig.model,
                                       max_tokens=gptConfig.max_token,
                                       temperature=gptConfig.temperature
                                       )
    else:
        # 获取gpt回答
        response = mu.get_answer(user_prompt=user_prompt,
                                 model=gptConfig.model,
                                 max_tokens=gptConfig.max_token,
                                 temperature=gptConfig.temperature)
    # 存储用户输入与gpt回答
    historyPacker.add_property("user" + str(chat_index), user_prompt)
    historyPacker.add_property("assistant" + str(chat_index), response.choices[0].message.content)
    # 输出gpt回答
    print(response.choices[0].message.content)
    print("本次提示词消耗：" + str(response.usage.prompt_tokens) + "    " +
          "本次答案消耗：" + str(response.usage.completion_tokens) + "    " +
          "剩余可用token：" + str(usable_token - response.usage.total_tokens))
    # 存储聊天记录至本地文件
    historyPacker.save_json_file(history_path)
