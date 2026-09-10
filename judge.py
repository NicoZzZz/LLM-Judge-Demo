import pandas as pd
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

judge_client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.cn/v1",
)

df = pd.read_excel("eval_v2.xlsx")
df["judge_reason"] = ""
for index, row in df.iterrows():

    judge_prompt = f"""
        你是一名文本大模型评测员。

        请根据用户原始要求，对模型回答进行整体评分。

        用户原始要求：
        {row["prompt"]}

        模型回答：
        {row["output"]}

        【评分标准】
        2分：完全满足用户要求。内容正确，关键约束均满足，没有明显遗漏、格式错误或无依据补充。

        1分：基本完成任务，但存在至少一个明显问题，例如：
        - 遗漏部分要求
        - 违反部分格式或字数约束
        - 增加了用户未提供的信息
        - 内容基本正确但不够完整
        - 表达存在明显问题

        0分：未完成任务或存在严重问题，例如：
        - 明显答非所问
        - 关键要求大部分未满足
        - 存在严重事实错误
        - 输出格式严重不符合要求
        - 内容无法用于用户要求的场景

        请严格依据用户明确写出的要求评分，不要自行增加新的评分标准。

        只输出 JSON，不要输出 Markdown 代码块或其他文字。
        格式如下：
        {{
        "score": 0,
        "reason": "用一句话简要说明评分理由"
        }}
        """


    judge_response = judge_client.chat.completions.create(
        model="kimi-k2.6",
        messages=[
            {"role": "user", "content": judge_prompt}
        ]
    )

    judge_answer = judge_response.choices[0].message.content
    print(repr(judge_answer))
    judge_result = json.loads(judge_answer)
    
    df.loc[index, "judge_score"] = judge_result["score"]
    df.loc[index, "judge_reason"] = judge_result["reason"] 
    print(row["case_id"], row["model"])
    print(judge_result)
    print("------")

df.to_excel("eval_v3.xlsx", index=False)