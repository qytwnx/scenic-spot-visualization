# 基于 Python 3.9 的官方镜像作为基础镜像
FROM python:3.9.10

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到容器中
COPY . /app

# 安装 Python 依赖库
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露 80 端口
EXPOSE 5000

CMD ["python3", "server.py"]