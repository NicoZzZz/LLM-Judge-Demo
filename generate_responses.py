import pandas as pd
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

deepseek_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

df = pd.read_excel("data.xlsx")
#deepseek回答
deepseek_df = df[df["model"] == "DeepSeek"]
df["output"] = df["output"].astype("string")

for index, row in deepseek_df.iterrows():
    prompt = row["prompt"]
    response = deepseek_client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    df.loc[index, "output"] = answer
    
    
    print(row["case_id"])
    print(answer)
    print("------")
df.to_excel("eval_v2.xlsx", index=False)

##Gemini回答
Gemini_df = df[df["model"] == "Gemini"]
Gemini_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

for index, row in Gemini_df.iterrows():
    prompt = row["prompt"]

    response = Gemini_client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    df.loc[index, "output"] = answer
    print(row["case_id"])
    print(answer)
    print("------")
df.to_excel("eval_v2.xlsx", index=False)



