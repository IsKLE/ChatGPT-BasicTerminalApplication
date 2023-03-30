import json
import os.path


# 转换字符串至json格式，返回json对象
def to_json_obj(data) -> json:
    try:
        json_obj = json.loads(data)
    except json.JSONDecodeError as e:
        raise TypeError("传入数据格式/数据类型错误") from e
    return json_obj


# 转换json格式至字符串，返回字符串
def to_json_string(json_data) -> str:
    try:
        json_string = json.dumps(json_data)
    except ValueError as e:
        raise ValueError("传入数据不是json数据") from e
    return json_string


# json读取器，传入与传出都是json对象。用于：
# 读取json数据
# 获取属性
# 打印json数据
class JsonReader:

    def __init__(self, file_path):
        # 判断路径是否存在
        if not os.path.exists(file_path):
            raise ValueError("Json文件不存在")
        # 读取文件数据保存在本地变量，之后方便调用,节省内存
        with open(file_path, 'r', encoding='utf-8') as json_file:
            # json.load返回值是字典对象
            self.json_obj = json.load(json_file)

    # 获取属性
    def get_property(self, property_name) -> str:
        try:
            data = str(self.json_obj[property_name])
        except KeyError:
            raise ValueError("属性不存在")
        return data

    # 打印json数据
    def print_json_data(self):
        print(to_json_string(self.json_obj))


# json打包器，传入与传出都是json对象。用于：
# 打印json数据
# 添加json数据
# 删除json数据
# 保存json数据至本地文件
class JsonPacker:

    def __init__(self, json_obj):
        self.json_obj = json_obj

    # 添加json数据，返回json对象
    def add_property(self, key, value) -> json:
        self.json_obj[key] = value
        return self.json_obj

    # 删除json数据，返回json对象
    def del_property(self, key) -> json:
        del self.json_obj[key]
        return self.json_obj

    # 打印json数据
    def print_json_data(self):
        print(to_json_string(self.json_obj))

    # 保存json数据至文件
    def save_json_file(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.json_obj, json_file, ensure_ascii=False, indent=2, )
        except Exception as e:
            print(e)
