import json

from attr import validate
from genson import SchemaBuilder


class JsonSchema:

    @classmethod
    def generate_schema(cls, obj, file_path):
        '''
        生成json schema文件
        obj 生成schema的python对象
        '''
        builder = SchemaBuilder()
        # 把预期的响应添加到builder中
        builder.add_schema(obj)
        # 生成json schema
        schema_content = builder.to_schema()
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(schema_content, f)

    @classmethod
    def schema_validate(cls, obj, schema):
        '''
        对比python对象与生成的json schema结构是否一致
        '''
        try:
            validate(instance=obj, schema=schema)
            return True
        except Exception as e:
            print(f"schema校验异常 ====> {e}")
            return False

'''
schema_path = os.sep.join([Utils.get_frame_root_path(), "config/get_schema.json"])
Utils.generate_schema(expected, schema_path)
r = self.ins.get()
schema = json.load(open(schema_path, encoding="utf-8"))
assert Utils.schema_validate(r.json(), schema)

'''

