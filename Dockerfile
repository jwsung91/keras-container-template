ARG GPU_ENABLED=0

FROM tensorflow/tensorflow:2.15.0 AS base
FROM tensorflow/tensorflow:2.15.0-gpu AS gpu

FROM ${GPU_ENABLED:+gpu} AS final

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy pandas matplotlib scikit-learn jupyter

WORKDIR /workspace
COPY . /workspace

EXPOSE 8888

CMD ["python", "-m", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
