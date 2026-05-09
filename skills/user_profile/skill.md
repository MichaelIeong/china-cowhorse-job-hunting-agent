---
name: user_profile
description: 采集用户信息，判断校招/社招类型，生成求职画像
---

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | str | 是 | 姓名 |
| education | str | 是 | 学历（本科/硕士/博士） |
| major | str | 是 | 专业 |
| graduation_year | int | 是 | 毕业年份 |
| work_years | int | 是 | 工作年限（应届填0） |
| skills | list[str] | 是 | 技能列表 |
| target_cities | list[str] | 是 | 目标城市 |
| target_positions | list[str] | 是 | 目标岗位 |
| phone | str | 否 | 手机号 |
| email | str | 否 | 邮箱 |

## 出参

```json
{
  "success": true,
  "data": {
    "job_type": "campus|social",
    "profile": { "用户完整画像数据" }
  },
  "message": "用户画像生成成功"
}
```

## 使用方法

```python
from skills.user_profile.script.main import main

result = main(
    name="张三",
    education="本科",
    major="计算机科学",
    graduation_year=2026,
    work_years=0,
    skills=["Python", "机器学习"],
    target_cities=["北京", "上海"],
    target_positions=["算法工程师"]
)
```
