- [Tutorial/docs/L0/linux at camp4 · InternLM/Tutorial](https://github.com/InternLM/Tutorial/tree/camp4/docs/L0/linux)

# 关卡任务

|            | 任务描述                                      | 完成所需时间 |
| ---------- | --------------------------------------------- | ------------ |
| 闯关任务   | 完成SSH连接与端口映射并运行`hello_world.py`   | 10min        |
| 可选任务 1 | 将Linux基础命令在开发机上完成一遍             | 10min        |
| 可选任务 2 | 使用 VSCODE 远程连接开发机并创建一个conda环境 | 10min        |

## ssh连接
最好再在本机生成公钥后添加在开发机，首次连接成功后不再需要输密码
生成公钥：`ssh-keygen -t rsa`，打开保存目录下的.pub文件，复制填写

点ssh连接，复制启动命令和密码：
`ssh -p 42776 root@ssh.intern-ai.org.cn -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null`

上传hello_world.py
`scp -o StrictHostKeyChecking=no -r -P 42776 "D:\IT\Projects\AI Agent\projects\书生大模型实战营\task\L0\hello_world.py" root@ssh.intern-ai.org.cn:/root`


端口映射，访问本地端口时转发到远程开发机的端口
`ssh -p 42776 root@ssh.intern-ai.org.cn -CNg -L 7860:127.0.0.1:7860 -o StrictHostKeyChecking=no`

启动前先安装helloworld所需库
`pip install gradio==4.29.0`

启动helloworld服务
`python hello_world.py`

启动后在本机访问
