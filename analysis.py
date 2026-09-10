import pandas as pd

df = pd.read_excel("eval_v3.xlsx")

# 判断人工评分和 Judge 评分是否一致
df["consistent"] = df["human_score"] == df["judge_score"]

# 计算整体一致率
agreement = df["consistent"].mean()
print(f"Human vs Judge 一致率：{agreement:.2%}")

# 找出不一致的 Case
diff_cases = df[df["consistent"] == False]

print(diff_cases[
    [
        "case_id",
        "model",
        "human_score",
        "judge_score",
        "human_reason",
        "judge_reason"
    ]
])

# 保存分歧 Case
diff_cases.to_excel("diff_cases.xlsx", index=False)