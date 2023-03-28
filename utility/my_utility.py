import openai


# 用于第一次查询，同时传递system与用户的信息，返回GPT的回答内容
def get_first_answer(system_prompt, user_prompt, model, temperature=0.1, max_tokens=30):
    # print("输入是系统")
    response = openai.ChatCompletion.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content


# 用于普通查询，传递用户的信息，返回GPT的回答内容
def get_answer(user_prompt, model, temperature=0.1, max_tokens=30):
    # print("输入是用户")
    response = openai.ChatCompletion.create(
        messages=user_prompt,
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content


# 添加至列表，返回添加后的列表
def add_chat(dictionary, chat_list, data="", role=""):
    # 通过拷贝释放对原来字典的依赖
    dictionary = dictionary.copy()
    dictionary.update({"role": role, "content": data})
    chat_list.append(dictionary)
    return chat_list


def print_out(list1, dictionary1, data):
    print(list1)
    print(dictionary1)
    print(data)
