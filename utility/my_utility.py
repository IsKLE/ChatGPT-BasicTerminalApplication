import openai


# 用于第一次查询，同时传递system与用户的信息，返回GPT的回答内容
def get_first_answer(system_prompt, user_prompt, model, temperature=0.1, max_tokens=30):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response


# 用于普通查询，传递用户的信息，返回GPT的回答内容
def get_answer(user_prompt, model, temperature=0.1, max_tokens=30):
    response = openai.ChatCompletion.create(
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        model=model,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response


# 添加至列表，返回添加后的列表
def add_chat(chat_list, role="", data=""):
    dic = {role, data}
    chat_list.append(dic)
    return chat_list


def print_out(list1, dictionary1, data):
    print(list1)
    print(dictionary1)
    print(data)
