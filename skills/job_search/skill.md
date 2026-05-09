---
name: job_search
description: 根据用户画像从对应平台搜索聚合目标岗位
---

## 入参

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| job_type | str | 是 | 求职类型（campus/social） |
| keywords | list[str] | 是 | 搜索关键词 |
| cities | list[str] | 是 | 目标城市 |
| platforms | list[str] | 否 | 指定平台（默认按类型自动选择） |
| company_names | list[str] | 否 | 指定公司名称筛选 |

## 出参

```json
{
  "success": true,
  "data": [
    {
      "title": "岗位名称",
      "company": "公司名",
      "city": "城市",
      "salary": "薪资范围",
      "requirements": ["要求1", "要求2"],
      "platform": "来源平台",
      "url": "岗位链接"
    }
  ],
  "message": "共找到 N 个匹配岗位"
}
```

## 使用方法

```python
from skills.job_search.script.main import main

result = main(
    job_type="campus",
    keywords=["算法工程师", "机器学习"],
    cities=["北京", "上海"]
)
```
