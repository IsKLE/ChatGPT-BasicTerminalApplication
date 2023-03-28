import json


# 读取json数据并返回
def read_json_data(file_path):
    with open(file_path, "r") as file:
        file_data = json.load(fp=file)
    return file_data


# 向json对象中添加数据
def add_json_data(key_name, new_data, json_data):
    json_data[key_name] = new_data
    return json_data


# 保存json数据
def save_json_data(file_path, json_data):
    with open(file_path, "w") as file:
        # 设置indent=2可以获得”一个键值对一行“的效果
        json.dump(json_data, file, indent=2)

# print(read_json_data("C:\\Users\\ooihr\\OneDrive\\CProject\\Python\\GPT\\assets\\chatHistory.json"))
