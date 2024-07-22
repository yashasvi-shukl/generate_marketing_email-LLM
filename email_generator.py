from langchain.prompts import load_prompt
try:
    from langchain.chains.llm import LLMChain
except Exception as e:
    from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from schema import EmailSchema
import json

# Email generation logic encapsulated in a class
class EmailGenerator:
    def __init__(self, **config):
        # self.api_key = api_key
        self.prompt_template = load_prompt("prompt.yaml")
        self.prompt_template.output_parser = JsonOutputParser()
        self.model = ChatOpenAI(**config['model_param'])
        self.chain = LLMChain(llm=self.model, prompt=self.prompt_template)

    def generate(self, topic, description):
        schema = EmailSchema.schema_json()
        result = self.chain.invoke({"topic": topic, "description": description, "schema": schema})
        return json.loads(result['text'])
