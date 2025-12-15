FROM python:3.11-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install jupyterlab

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
