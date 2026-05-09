---
name: job_shortlist
description: 整理筛选心仪岗位，含薪资区间分析和匹配度评估
---

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| jobs | list[dict] | 是 | 待筛选岗位列表（来自 job_search） |
| preferences | dict | 否 | 用户偏好（薪资范围、公司规模等） |
| sort_by | str | 否 | 排序方式：salary/match/company，默认 match |

## 出参

```json
{
  "success": true,
  "data": {
    "shortlist": [{"岗位信息 + 匹配度评分"}],
    "salary_analysis": {"min": 15000, "max": 30000, "avg": 22000},
    "total": 10
  },
  "message": "已整理 N 个心仪岗位"
}
```

## 使用方法

```python
from skills.job_shortlist.script.main import main

result = main(
    jobs=search_results,
    preferences={"min_salary": 15000, "company_size": "大型"},
    sort_by="match"
)
```
