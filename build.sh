#!/bin/bash
BASE_IMAGE=${BASE_IMAGE:-""}

is_valid_base_image() {
  local regex="^tensorflow/tensorflow:(2\.[0-9]+\.0|latest)$"
  [[ "$1" =~ $regex ]]
}

if ! is_valid_base_image "$BASE_IMAGE"; then
  echo "Invalid base image: $BASE_IMAGE"
  echo "Change to tensorflow/tensorflow:2.15.0"
  BASE_IMAGE=""
fi

if [ -z "$BASE_IMAGE" ]; then
  BASE_IMAGE="tensorflow/tensorflow:2.15.0" 
  if command -v nvidia-smi &> /dev/null && nvidia-smi &> /dev/null; then
    BASE_IMAGE="$BASE_IMAGE-gpu"
  fi
fi

echo "BASE_IMAGE=$BASE_IMAGE"

docker build --no-cache --build-arg TENSORFLOW_IMAGE=$BASE_IMAGE -t tensorflow-container .