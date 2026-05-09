---
name: resume_optimizer
description: 针对目标岗位分析简历匹配度，给出优化修改建议
---

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| resume_text | str | 是 | 简历文本内容 |
| job_description | str | 是 | 目标岗位 JD |
| job_requirements | list[str] | 否 | 岗位要求关键词列表 |

## 出参

```json
{
  "success": true,
  "data": {
    "match_score": 72.5,
    "suggestions": ["建议1", "建议2"],
    "keyword_analysis": {
      "matched": ["Python", "机器学习"],
      "missing": ["TensorFlow", "分布式系统"]
    }
  },
  "message": "简历匹配度 72.5%，有 2 条优化建议"
}
```

## 使用方法

```python
from skills.resume_optimizer.script.main import main

result = main(
    resume_text="简历全文...",
    job_description="岗位JD全文...",
    job_requirements=["Python", "深度学习", "3年经验"]
)
```
