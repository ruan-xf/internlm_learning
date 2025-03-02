- [优秀作业 1](https://juejin.cn/post/7431847699568558092)
- [Tutorial/docs/L0/git at camp4 · InternLM/Tutorial](https://github.com/InternLM/Tutorial/tree/camp4/docs/L0/git)

## **任务1: 破冰活动：自我介绍**
每位参与者提交一份自我介绍。
提交地址：https://github.com/InternLM/Tutorial 的 class 分支～

![alt text](https://github.com/random-zhou/ailabImage/blob/main/taskim1.png)


1. 命名格式为 `<id>.md`，其中 `<id>` 是您的报名问卷UID。
2. 文件路径应为 `./icamp4/`。
3. 【大家可以叫我】内容可以是 GitHub 昵称、微信昵称或其他网名。
4. 在 GitHub 上创建一个 Pull Request，提供对应的 PR 链接。


为什么要先fork？改了直接push到别人仓库会怎样？
会提示没有权限，所以应该先fork自己的副本

copy全部分支、clone到本地后可查看本地和远程的所有分支
`git branch -a`
```
* camp4
  remotes/origin/HEAD -> origin/camp4
  remotes/origin/camp1
  remotes/origin/camp2
  remotes/origin/camp2_en
  remotes/origin/camp3
  remotes/origin/camp4
  remotes/origin/class
  remotes/origin/revert-1303-camp3_2393
```

使用分支进行隔离是个好习惯，每个任务或功能都在独立分支上开发，便于代码审查和问题追踪。
如本次，自我介绍的md文件不在camp4分支，需切换到class分支下查看和提交

如果开始在camp4进行fork，而实际要修改的分支在class，就需要copy其他分支，即取消only的选项
因为无法只克隆某个分支，clone到本地有些久
或也可以在页面切换到class分支，然后只copy这个分支也都可以了

clone到本地后可以查看所有远程仓库的信息 `git remote -v`
```
origin  https://github.com/ruan-xf/Tutorial (fetch)
origin  https://github.com/ruan-xf/Tutorial (push)
upstream        https://github.com/InternLM/Tutorial.git (fetch)
upstream        https://github.com/InternLM/Tutorial.git (push)
```

如果默认是camp4分支，clone到本地只有camp4的，需要以我的远程项目的class分支创建本地的class分支
`git checkout -b class origin/class`


以class分支再建带自己id的class分支，创建并切换：`git checkout -b class_036`

添加我的文件
模板：
```
【大家可以叫我】:InternLM
【坐标】:上海
【专业/职业】:小助手
【兴趣爱好】:乒乓球
【项目技能】:cv、nlp
【组队情况】:未组队，快来一起!
【本课程学习基础】:CV、NLP、LLM
【本期活动目标】:一起学习，快乐暑假，闯关达人!
```

保存并提交到暂存区 `git add .`

我曾在错误的分支上进行了修改，尝试将先前的修改转移到正确的分支上
- `git add .` 修改进入暂存区
- `git stash` 将暂存区和工作目录的修改保存到一个存储堆栈中，且当前目录被恢复
- `git chechout class_8385` 切换到正确的分支
- `git stash pop` 将之前保存的修改恢复到当前分支的工作目录和暂存区。

无误可commit到本地仓库，添加提交信息：`git commit -m "add git_camp4_036_introduction"`

可继续push到远程仓库：`git push origin class_8385`
然后在上游项目主页下发起pull request，要求merge class和ruan-xf:class_8385


## **任务2: 实践项目：构建个人项目**


1. 创建并维护一个公开的大模型相关项目或笔记仓库。
2. 提交作业时，提供您的 GitHub 仓库链接。
3. 如果您不常使用 GitHub，您可以选择其他代码管理平台，如 Gitee，并提交相应的链接。
4. 仓库介绍中添加超链接跳转 [GitHub 仓库](https://github.com/InternLM/Tutorial)（<u>[https://github.com/InternLM/Tutorial](https://github.com/InternLM/Tutorial)</u>）
5. 将此项目报名参加第四期实战营项目评选将解锁 30% A100 和 168 团队算力点资源，报名链接：https://aicarrier.feishu.cn/wiki/JuXvwHzGni2A2Rksd8Rczpvxngb


先创建这个仓库吧
- [ruan-xf/myBot: 书生实战营项目](https://github.com/ruan-xf/myBot)
