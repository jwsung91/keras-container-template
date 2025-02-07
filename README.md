# keras-container-template

```
 docker build --no-cache --build-arg GPU_ENABLED=1 -t keras-gpu .
```

```
docker run -it --rm --gpus all -p 8888:8888 keras-gpu
```