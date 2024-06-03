class ModelTemplate:
    @staticmethod
    def apply(query: str, **kwargs):
        return query


class Llama2Template(ModelTemplate):
    @staticmethod
    def apply(query: str, **kwargs):
        template = "<s> [INST] <<SYS>> {sys_prompt} <</SYS>> {query} [/INST]"
        assert 'sys_prompt' in kwargs, f"sys_prompt text not found; llama2 template = {template}"
        sys_prompt = kwargs['sys_prompt']

        out_text = template.format(query=query, sys_prompt=sys_prompt)
        return out_text

class Llama3Template(ModelTemplate):
    @staticmethod
    def apply(query: str, **kwargs):
        template = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{sys_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{query}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        assert 'sys_prompt' in kwargs, f"sys_prompt text not found; llama3 template = {template}"
        sys_prompt = kwargs['sys_prompt']

        out_text = template.format(query=query, sys_prompt=sys_prompt)
        return out_text

class VicunaTemplate(ModelTemplate):
    @staticmethod
    def apply(query: str, **kwargs):
        # Taken from https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md#example-prompt-weights-v11-v13-v15
        template = "{sys_prompt} \nUSER: {query}\nASSISTANT: "
        assert 'sys_prompt' in kwargs, f"sys_prompt text not found; vicuna template = {template}"
        sys_prompt = kwargs['sys_prompt']

        out_text = template.format(query=query, sys_prompt=sys_prompt)
        return out_text


ALL_MODEL_TEMPLATE_FUNC={
    'default': ModelTemplate.apply,
    'llama2': Llama2Template.apply,
    'llama3': Llama3Template.apply,
    'vicuna': VicunaTemplate.apply,
    'openai': ModelTemplate.apply
}