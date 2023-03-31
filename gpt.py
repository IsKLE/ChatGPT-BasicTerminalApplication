import openai
import utility.gpt_utility as gu
from utility.json_utility import JsonPacker
from utility.configer import Configer

# 定义文件路径
config_path = "assets\\gptConfig.json"
history_path = "assets\\chatHistory.json"
# 获取文件配置
gptConfig = Configer(config_path=config_path)
gptConfig.show_attr()
history = Configer(history_path=history_path).history_obj
# 设置API-KEY
openai.api_key = gptConfig.api_key
# 定义数据存储变量
chat_list = []
chat_index = 0
usable_token = 4096
# 历史记录整理器
historyPacker = JsonPacker(json_obj=history)
# 开始GPT程序
while True:
    # 对话计数加一
    chat_index += 1
    print("———————————", chat_index, "———————————")
    user_prompt = gu.user_input(chat_list)
    # 第一次询问，需要同时传递系统与用户的数据；之后只需要传递用户的数据
    if chat_index == 1:
        # 处理系统与用户的输入并保存
        historyPacker.add_property("system", gptConfig.system_prompt + gptConfig.language_type)
        # 获取gpt回答
        response = gu.get_first_answer(system_prompt=gptConfig.system_prompt + gptConfig.language_type,
                                       user_prompt=user_prompt,
                                       model=gptConfig.model,
                                       max_tokens=gptConfig.max_token,
                                       temperature=gptConfig.temperature
                                       )
    else:
        # 获取gpt回答
        response = gu.get_answer(chat_list=chat_list,
                                 model=gptConfig.model,
                                 max_tokens=gptConfig.max_token,
                                 temperature=gptConfig.temperature)
    # 保存gpt回答至聊天列表
    chat_dic = {"role": "assistant", "content": response.choices[0].message.content}
    chat_list.append(chat_dic)
    # 存储用户输入与gpt回答
    historyPacker.add_property("user" + str(chat_index), user_prompt)
    historyPacker.add_property("assistant" + str(chat_index), response.choices[0].message.content)
    # 输出gpt回答
    print(response.choices[0].message.content)
    print("本次提示词消耗：" + str(response.usage.prompt_tokens) + "    " +
          "本次答案消耗：" + str(response.usage.completion_tokens) + "    " +
          "可用token：" + str(usable_token - response.usage.total_tokens) + "    " +
          "本次消耗：$" + str(response.usage.total_tokens / 1000 * 0.002)
          )
    # 存储聊天记录至本地文件
    historyPacker.save_json_file(history_path)
