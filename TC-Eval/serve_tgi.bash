# usage: serve_tgi.bash <hf-model-id> <port>
volume=$PWD/tgi_data # share a volume with the Docker container to avoid downloading weights every run
token_volume=~/.cache/huggingface/token

docker run --gpus all --shm-size 24g -p $2:80 -v $volume:/data -v $token_volume:/root/.cache/huggingface/token \
    ghcr.io/huggingface/text-generation-inference:2.0.4 \
    --model-id $1 --trust-remote-code
