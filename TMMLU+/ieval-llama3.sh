# $1 should be compatible to llama2'2 format
# LinkSoul/Chinese-Llama-2-7b,[INST] <<SYS>>\n,\n,[/INST],<</SYS>>\n\n

ieval $1 "${@:2}" \
    --series=tgi \
    --sys_token="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n" \
    --usr_token="<|start_header_id|>user<|end_header_id|>\n\n" \
    --eos_token="<|eot_id|>" \
    --ast_token="<|start_header_id|>assistant<|end_header_id|>" \