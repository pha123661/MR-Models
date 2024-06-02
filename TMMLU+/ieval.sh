# $1 should be compatible to llama2'2 format
# LinkSoul/Chinese-Llama-2-7b,[INST] <<SYS>>\n,\n,[/INST],<</SYS>>\n\n

ieval $1 "${@:2}" \
    --series=tgi \
    --sys_token="[INST] <<SYS>>\n" \
    --eos_token="\n" \
    --ast_token="[/INST]" \
    --usr_token="<</SYS>>\n\n" \
