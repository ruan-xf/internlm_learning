- [Tutorial/docs/L0/maas at camp4 · InternLM/Tutorial](https://github.com/InternLM/Tutorial/tree/camp4/docs/L0/maas)

# 闯关任务
| 任务 | 描述 | 时间 |
| --- | --- | --- |
| [模型下载](https://huggingface.co/internlm/internlm2-chat-1_8b) | 使用Hugging Face平台、魔搭社区平台（可选）和魔乐社区平台（可选）下载文档中提到的模型（至少需要下载config.json文件、model.safetensors.index.json文件），请在必要的步骤以及结果当中截图。 | 20min |
| 模型上传（可选） | 将我们下载好的config.json文件（也自行添加其他模型相关文件）上传到对应HF平台和魔搭社区平台，并截图。 | 10min |
| Space上传（可选） | 在HF平台上使用Spaces并把intern_cobuild部署成功，关键步骤截图。 | 10min |

## 使用huggingface下载的预训练模型进行推理

已尝试使用github codespaces，但并不如vscode ssh连接开发机好用，而且需要开发机准备好了的预训练模型

安装指定版本的库：
```
pip install transformers==4.38
pip install sentencepiece==0.1.99
pip install einops==0.8.0
pip install protobuf==5.27.2
pip install accelerate==0.33.0
```

指定model_name，使用AutoTokenizer.from_pretrained后，若未缓存将开始模型的下载
也可手动下载：
下载单个文件：
```
from huggingface_hub import hf_hub_download
hf_hub_download(
        repo_id=repo_id,
        filename=file_info["filename"],
        local_dir=local_dir
    )
```

下载整个模型仓库（注意设置huggingface代理、并发下载数、断点续传）：
- [HF-Mirror](https://hf-mirror.com/)
```
from huggingface_hub import snapshot_download
snapshot_download('internlm/internlm2_5-7b-chat', local_dir='internlm')
```


本次可直接使用开发机，已预先准备，指定model_path为
`/root/share/new_models/Shanghai_AI_Laboratory/internlm2_5-7b-chat`

加载模型尝试推理：
```py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("internlm/internlm2_5-1_8b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("internlm/internlm2_5-1_8b", torch_dtype=torch.float16, trust_remote_code=True)
model = model.eval()

inputs = tokenizer(["A beautiful flower"], return_tensors="pt")
gen_kwargs = {
    "max_length": 128,
    "top_p": 0.8,
    "temperature": 0.8,
    "do_sample": True,
    "repetition_penalty": 1.0
}

# 以下内容可选，如果解除注释等待一段时间后可以看到模型输出
# output = model.generate(**inputs, **gen_kwargs)
# output = tokenizer.decode(output[0].tolist(), skip_special_tokens=True)
# print(output)
```

原尝试使用gpu：
```py
model = model.to(device)
inputs = tokenizer(["A beautiful flower"], return_tensors="pt")
# 此时inputs是字典，值为tensor
inputs = {key: value.to(device) for key, value in inputs.items()}
```

但OutOfMemory，作罢

也可使用pipeline进一步封装，同时也清楚地说明了Transformers的推理过程
- [第四章：开箱即用的 pipelines · Transformers快速入门](https://transformers.run/c2/2021-12-08-transformers-note-1/)
