import json


class JsonReader:
    def __init__(self, file_path=None, instance_name=None):
        self.file_path = file_path
        self.instance_name = instance_name
        if self.instance_name is None:
            self.instance_name = '未命名'
        if self.file_path is None:
            raise ValueError("Json路径不可为空！")

    def get_property(self, property_name):
        # 使用with语句协助管理内存
        with open(self.file_path, encoding='utf-8', mode='r') as json_file:
            # json_data赋值后是字典对象
            json_data = json.load(json_file)
            data = str(json_data[property_name])
            # print(self.instance_name + " 读取 " + property_name + "：" + data)
            return data
