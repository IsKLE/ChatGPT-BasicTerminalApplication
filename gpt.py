import openai
import utility.my_utility as mu
import utility.data_packer as dp
import utility.configer as cfg

# 定义文件路径
config_path = "assets\\gptConfig.json"
history_path = "assets\\chatHistory.json"
# 获取配置属性
config = cfg.ConfiGer(config_path=config_path, history_path=history_path)
openai.api_key = config.get_attr("api_key")
language_type = config.get_attr("language_type")
system_prompt = config.get_attr("system_prompt") + language_type
gpt_model = config.get_attr("model")
max_token = int(config.get_attr("max_token"))
temperature = float(config.get_attr("temperature"))
print(language_type, " ", temperature)
# 定义数据存储变量
chat_index = 1
chat_list = []
chat_dic = {}  # 该变量是一次性的，只存储最新的"角色/内容"对
enter_times = 0
user_prompt = ''
# 初始化历史记录文件
json_data = dp.read_json_data(history_path)
# 开始GPT程序
while True:
    user_prompt = ''
    print("———————————", chat_index, "—————————————")
    print("请输入问题：")
    # 在用户连续输入两次回车后，正式发送数据。
    while True:
        line = input()
        if line != '':
            user_prompt = user_prompt + line + '\r'
            enter_times = 1
        else:
            enter_times = enter_times + 1
            if enter_times == 2:
                break
    print("GPT：")
    # 第一次询问，需要同时传递系统与用户的数据；之后只需要传递用户的数据
    if chat_index == 1:
        # 处理系统与用户的输入并保存
        chat_list = mu.add_chat(chat_dic, chat_list, system_prompt, "system")
        json_data = dp.add_json_data("system", system_prompt, json_data)
        chat_list = mu.add_chat(chat_dic, chat_list, user_prompt, "user")
        json_data = dp.add_json_data("user", user_prompt, json_data)
        # 获取gpt回答
        response = mu.get_first_answer(system_prompt=system_prompt,
                                       user_prompt=user_prompt,
                                       model=gpt_model,
                                       max_tokens=max_token,
                                       temperature=temperature)
        # 存储gpt回答
        try:
            chat_list = mu.add_chat(chat_dic, chat_list, response, "assistant")
            json_data = dp.add_json_data("assistant", response, json_data)
        except Exception as e:
            print(e)
    else:
        # 替换输入数据
        chat_list = mu.add_chat(chat_dic, chat_list, user_prompt, "user")
        json_data = dp.add_json_data("user" + str(chat_index), user_prompt, json_data)
        # 获取gpt回答
        response = mu.get_answer(user_prompt=chat_list,
                                 model=gpt_model,
                                 max_tokens=max_token,
                                 temperature=temperature)
        # 存储gpt回答
        chat_list = mu.add_chat(chat_dic, chat_list, response, "assistant")
        json_data = dp.add_json_data("assistant" + str(chat_index), response, json_data)

    dp.save_json_data(json_data=json_data, file_path=history_path)
    # 计数加一
    chat_index += 1
    # 输出内容
    print(response)
    # 显示历史记录，遍历列表
    # print("—————————数据———————————")
    # mu.print_out(chat_list, chat_dic, json_data)  # 由于字典只在调用函数中存在值，所以没有必要进行输出。
    # mu.print_out(chat_list,  json_data)
    # try:
    #     for item in chat_list:
    #         print(item)
    # except Exception as e:
    #     print("错误", e)
    # print("——————————————————————")
    # for num in user_prompt.split('\r'):
    #     print(num)
    # print("——————————————————————")
