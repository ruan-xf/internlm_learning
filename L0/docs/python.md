- [Tutorial/docs/L0/Python at camp4 · InternLM/Tutorial](https://github.com/InternLM/Tutorial/tree/camp4/docs/L0/Python)

## 任务
| 任务类型 | 任务内容 | 预计耗时 |
| --- |---| ---|
|闯关任务|Leetcode 383(笔记中提交代码与leetcode提交通过截图)| 20mins|
|闯关任务| Vscode连接InternStudio debug笔记 | 10mins|
|可选任务| pip安装到指定目录 | 10mins|

### 任务一
完成[Leetcode 383](https://leetcode.cn/problems/ransom-note/description/), 笔记中提交代码与leetcode提交通过截图


### 任务二
下面是一段调用书生浦语API实现将非结构化文本转化成结构化json的例子，其中有一个小bug会导致报错。请大家自行通过debug功能定位到报错原因。

**TIPS**:
- 打断点查看下LLM返回的文本结果。造成本bug的原因与LLM的输出有关，学有余力的同学可以尝试修正这个BUG。

- 作业提交时需要有debug过程的图文笔记，必须要有**打断点在debug中看到`res`变量的值的截图。**

- **避免将api_key明文写在程序中！！！** 本段demo为了方便大家使用debug所以将api_key明文写在代码中，这是一种极其不可取的行为!


```python
from openai import OpenAI
import json
def internlm_gen(prompt,client):
    '''
    LLM生成函数
    Param prompt: prompt string
    Param client: OpenAI client 
    '''
    response = client.chat.completions.create(
        model="internlm2.5-latest",
        messages=[
            {"role": "user", "content": prompt},
      ],
        stream=False
    )
    return response.choices[0].message.content

api_key = ''
client = OpenAI(base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",api_key=api_key)

content = """
书生浦语InternLM2.5是上海人工智能实验室于2024年7月推出的新一代大语言模型，提供1.8B、7B和20B三种参数版本，以适应不同需求。
该模型在复杂场景下的推理能力得到全面增强，支持1M超长上下文，能自主进行互联网搜索并整合信息。
"""
prompt = f"""
请帮我从以下``内的这段模型介绍文字中提取关于该模型的信息，要求包含模型名字、开发机构、提供参数版本、上下文长度四个内容，以json格式返回。
`{content}`
"""
res = internlm_gen(prompt,client)
res_json = json.loads(res)
print(res_json)
```

在res_json处出现异常，在vscode中可选择在res_json行下断点，亦可直接调试，会自动在异常处中断

出现的异常：

查看模型回应：

此文本很明显不是json，而需要想办法提取其中的markdown json代码块

我选择使用正则表达式提取，使用的表达式
```
```json\s*({.*?})\s*```
```

可先观察此正则匹配效果
- [Regexper](https://regexper.com/)

匹配效果：

而点号（.）默认匹配除换行符（\n）以外的任何字符，完整提取此多行json块需启用 re.DOTALL 标志，此时点号（.）会匹配包括换行符（\n）在内的任何字符。

添加处理如下：
```py
import re
matchs = re.search(r'```json\s*({.*?})\s*```', res, re.DOTALL)
res_json = json.loads(matchs.group(1))
```

处理结果：

### 任务三(可选)
使用VScode连接开发机后使用`pip install -t`命令安装一个numpy到看开发机`/root/myenvs`目录下，并成功在一个新建的python文件中引用。

为排除base环境的干扰，需要新建一个虚拟环境来进行
```sh
conda create --name myenv python=3.9
conda activate myenv

mkdir -p /root/myenvs
pip install numpy -t /root/myenvs
```

引入并使用：
```py
import sys  
  
# 你要添加的目录路径  
your_directory = '/root/myenvs'  
  
# 检查该目录是否已经在 sys.path 中  
if your_directory not in sys.path:  
    # 将目录添加到 sys.path  
    sys.path.append(your_directory)  
  
# 现在你可以直接导入该目录中的模块了  
# 例如：import your_module
import numpy as np
print(np.__version__)
print(np.random.random(5))
```

结果：
