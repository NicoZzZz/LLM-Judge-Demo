# LLM Evaluation Demo

一个文本大模型评测项目，用于实践LLM-as-a-Judge 和人工评分对比。

## Project Overview

使用同一组文本任务测试 DeepSeek 和 Gemini，并使用 Kimi 作为 Judge 对模型回答进行自动评分。

同时保留人工评分，用于比较 Human Evaluation 和 LLM Judge 的一致性。

## Evaluation Pipeline

```text
data.xlsx
    ↓
generate_responses.py
    ↓
DeepSeek / Gemini 生成回答
    ↓
eval_v2.xlsx
    ↓
judge.py
    ↓
Kimi Judge 自动评分
    ↓
eval_v3.xlsx
    ↓
analysis.py
    ↓
Human vs Judge 一致性分析
    ↓
diff_cases.xlsx
```

## Dataset

当前测试集包含：

- 5 个 Case
- 2 个模型
- 10 个模型回答

题目来源于IFBench，并根据中文任务环境进行调整。

## Scoring

Human 和 Judge 使用相同的 0～2 分标准：

- `2`：完全满足要求
- `1`：基本完成，但存在明显问题
- `0`：未完成任务或存在严重问题

## Files

- `requirements.txt`：项目依赖
- `data.xlsx`：原始评测数据
- `generate_responses.py`：调用 DeepSeek 和 Gemini 生成回答
- `eval_v2.xlsx`：保存模型回答
- `judge.py`：使用 Kimi 进行自动评分
- `eval_v3.xlsx`：保存 Human 和 Judge 的评分结果
- `analysis.py`：计算 Human vs Judge 一致率并筛选分歧 Case
- `diff_cases.xlsx`：保存评分不一致的样本

## Limitations

当前项目数据量较小，主要用于练习文本大模型评测的基本流程。

后续可以增加更多 Case，增加更多评测方法。
