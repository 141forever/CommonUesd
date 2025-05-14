import json

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 跳过空行
                try:
                    item = json.loads(line)
                    data.append(item)
                except json.JSONDecodeError as e:
                    print(f"解析出错: {e}，内容为: {line}")
    return data

def write_jsonl(file_path,data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            json_line = json.dumps(item, ensure_ascii=False)
            f.write(json_line + '\n')
            
def write_keep_list():
    with open('.json', 'w', encoding='utf-8') as f:
        json.dump(out_list, f, indent=4, ensure_ascii=False)
    # like this:
    # [
    #   {},
    #   {},
    #   {},
    # ]
