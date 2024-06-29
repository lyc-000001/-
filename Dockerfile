FROM python:3.8

COPY requirements.txt ./
RUN #/usr/local/bin/python -m pip install pip==22.2.2
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir
COPY . /usr/local/bin/
WORKDIR /usr/local/bin/
RUN chmod +x /usr/local/bin/*.py
ENTRYPOINT ["/usr/local/bin/run.py"]