---
name: interview_prep
description: 根据岗位JD和公司信息生成面试准备材料
---

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| job_description | str | 是 | 岗位 JD |
| company_name | str | 是 | 公司名称 |
| resume_text | str | 否 | 用户简历（用于定制化问题） |
| interview_type | str | 否 | 面试类型：tech/hr/behavior，默认 tech |

## 出参

```json
{
  "success": true,
  "data": {
    "common_questions": [
      {"question": "问题", "suggested_answer": "建议回答", "source": "牛客/小红书"}
    ],
    "company_info": {"简要公司背景"},
    "key_points": ["要点提醒1", "要点提醒2"]
  },
  "message": "已生成面试准备材料，含 N 个高频问题"
}
```

## 使用方法

```python
from skills.interview_prep.script.main import main

result = main(
    job_description="岗位JD...",
    company_name="字节跳动",
    interview_type="tech"
)
```
