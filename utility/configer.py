import utility.json_reader as jr



# 该类用于读取配置
class ConfiGer:

    def __init__(self, config_path, history_path=None):
        try:
            # 创建config_Reader实例
            config_Reader = jr.JsonReader(file_path=config_path, instance_name="configReader")
            # 初始化传入值
            self.config_path = config_path
            if history_path is None:
                self.history_path = config_Reader.get_property("history_path")
            else:
                self.history_path = history_path
            # 定义变量(使用self才能使编译器知道这是该类的参数)
            self.language_type = config_Reader.get_property("language_type2")
            self.system_prompt = config_Reader.get_property("system_prompt1")
            self.temperature = config_Reader.get_property("temperature")
            self.max_token = config_Reader.get_property("max_token")
            self.api_key = config_Reader.get_property("api_key")
            self.model = config_Reader.get_property("model1")
        except Exception as e:
            print("读取配置失败")
            print(e)

    def show_attr(self):
        # 使用 vars() 获取对象的所有属性和属性值
        props = vars(self)
        # 使用 for 循环遍历并打印每个属性和属性值
        for prop, value in props.items():
            print(f"{prop} = {value}")

    def get_attr(self, attr_name):
        return getattr(self, attr_name)


