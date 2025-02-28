from openai import OpenAI 
from langchain.prompts import ChatPromptTemplate

API_KEY = "sk-pgjkfvzqcsdsxskikrgmvqinofbuiefpyxggcgnthaoklmjk"

class CustomLLM_Siliconflow:
    def __call__(self, prompt:str) -> str:
        client = OpenAI(api_key=API_KEY,base_url='https://api.siliconflow.cn')
        response = client.chat.completions.create(
            model='deepseek-ai/DeepSeek-R1',
            messages=[
                {'role':'user',
                 'content':f"{prompt}"}
            ],
        )
        content = ""
        if hasattr(response,'choices') and response.choices:
            for choice in response.choices:
                if hasattr(choice,'message') and hasattr(choice.message,'content'):
                    chunk_content = choice.message.content 
                    print (chunk_content,end='')
                    content += chunk_content
            else:
                raise ValueError('unexpected response structure')
                
            return  content



llm = CustomLLM_Siliconflow()
print(llm("你是谁？"))

