from openai import OpenAI
import os  # 安全读取环境变量

class CustomLLM_Siliconflow:
    def __call__(self, prompt: str) -> str:
        # 从环境变量获取API密钥
        client = OpenAI(
            api_key='sk-pgjkfvzqcsdsxskikrgmvqinofbuiefpyxggcgnthaoklmjk',
            base_url='https://api.siliconflow.cn'
        )

        try:
            # 调用API
            response = client.chat.completions.create(
                model='deepseek-ai/DeepSeek-R1',
                messages=[{'role': 'user', 'content': prompt}]
            )
        except Exception as e:
            raise RuntimeError(f"API请求失败: {str(e)}")

        content = ""
        # 检查响应结构
        if not (hasattr(response, 'choices') and response.choices):
            raise ValueError("响应缺少choices字段")

        # 遍历并提取内容
        for choice in response.choices:
            if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
                chunk_content = choice.message.content
                print(chunk_content, end='')
                content += chunk_content
            else:
                raise ValueError("响应结构不符合预期")

        return content

# 测试调用
if __name__ == "__main__":
    llm = CustomLLM_Siliconflow()
    print(llm("你是谁？"))