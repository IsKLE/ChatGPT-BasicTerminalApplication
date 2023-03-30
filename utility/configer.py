from utility.json_utility import JsonReader


# 该类用于读取并保存配置，传入文件路径，返回“文件的json对象”、“部分属性的值”。用于：
# 获取对应文件的数据,保存至自己的属性
# 打印所有属性
class Configer:

    def __init__(self, config_path=None, history_path=None):
        try:
            if config_path is not None:
                gptConfig = JsonReader(file_path=config_path)
                self.config_obj = gptConfig.json_obj
                self.api_key = gptConfig.get_property("api_key")
                max_token = gptConfig.get_property("max_token")
                self.max_token = int(max_token)
                temperature = gptConfig.get_property("temperature")
                self.temperature = float(temperature)
                self.system_prompt = gptConfig.get_property("system_prompt")
                self.language_type = gptConfig.get_property("language_type")
                self.model = gptConfig.get_property("model")
            if history_path is not None:
                self.history_obj = JsonReader(file_path=history_path).json_obj
        except Exception as e:
            print(e)

    def show_attr(self):
        # 使用 vars() 获取对象的所有属性和属性值
        props = vars(self)
        # 使用 for 循环遍历并打印每个属性和属性值
        for prop, value in props.items():
            print(f"{prop} = {value}")
