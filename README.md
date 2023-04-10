

# 介绍
项目地址：[SynologyChatbotGPT](https://github.com/Jason0816/SynologyChatbotGPT)
dockerhub地址：[synology-chatgpt-bot](https://hub.docker.com/r/jason0816/synology-chatgpt-bot)
该项目Fork自[Xueheng-Li/SynologyChatbotGPT](https://github.com/Xueheng-Li/SynologyChatbotGPT) 

修改如下：
1. 只保留了chatGPT的部分，其余功能删除
2. 通过环境变量设置相关重要参数
3. 增加tokens使用统计，每次返回结果后都返回使用的tokens情况
4. 增加Dockerfile，构建docker镜像

相关环境变量如下：

| Parameter | Function |
| ------ | ------ |
| PORT | 应用运行端口 |
| OPEN_API_KEY | `必需`chatGPT的API key |
| WEBHOOK_URL | `必需`群晖chat机器人传入URL |
| WEBHOOK_TOKEN | `必需`群晖chat机器人令牌 |
| MAX_CONVERSATION_LEN | `可选`maximum conversation exchanges，默认值为10 |
| MAX_TIME_GAP | `可选`idle time gap to start a new conversation，默认值为15（分钟) |
| TEMPERATURE | `可选`a parameter in the OpenAI API that controls the randomness of the generated text. 默认值为0.5|

*最后三个参数含义请参考原项目[Xueheng-Li/SynologyChatbotGPT](https://github.com/Xueheng-Li/SynologyChatbotGPT) 注释*

# 群晖chat机器人配置

在 Synology Chat 中请按照以下步骤添加聊天机器人：

1. 用有管理员权限的账户登录 Synology Chat
2. 点击右上角你的头像，在菜单中选择`整合`Integration，点击`机器人`
3. 点击`创建`按钮，然后自定义名称和用途
4. 在`传出URL`中填入webhook地址,webhook的地址格式为：`http://SERVER_IP:PORT/webhook`。其中`SERVER_IP`为服务部署的机器的IP，`PORT`为服务运行端口
5. 记录`传入URL`和`令牌`备用(分别对应上述环境变量的`WEBHOOK_URL`和`WEBHOOK_TOKEN`)
6. 点击确定保存

# 创建docker服务

运行以下指令：
```bash
docker run --name synologychat \
-e OPEN_API_KEY=your-api-key \
-e WEBHOOK_URL=传入URL \
-e WEBHOOK_TOKEN=令牌 \
-p your-port:5008 \
jason0816/synology-chatgpt-bot:latest
```

# 注意事项
1. 请确保你的 OpenAI API 密钥和 Synology Chat 机器人详细信息已正确填写
2. 确保你的服务器可以访问OpenAI，以便与 OpenAI API 进行通信
3. 向 OpenAI API 发送请求可能会产生费用。根据你的 API 使用情况，费用可能有所不同。请参阅 OpenAI 的[定价页面](https://openai.com/pricing)了解详细信息
4. 在生产环境中部署聊天机器人时，请确保遵循最佳安全实践，例如使用 HTTPS、验证令牌等
5. 本代码的对话历史存储在内存中。在实际生产环境中，你可能需要使用持久存储（例如数据库）来存储对话历史
6. 本示例代码中未实现对输入和输出的过滤和检查。在实际应用中，请确保对输入进行验证和过滤，以防止潜在的安全问题
