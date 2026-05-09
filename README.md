# 中国牛马求职 Agent

> 基于大模型 Skill 机制的智能求职辅助工具集，帮助中国求职者高效完成求职全流程。

## 项目简介

本项目为中国求职者提供自动化求职辅助能力，以 **Python 脚本** 形式实现，通过大模型 Skill 调用执行。覆盖**校招**和**社招**两大场景，根据用户身份自动适配不同的求职策略和平台。

## 设计理念

- **Skill 驱动** - 所有功能以独立 Python 脚本实现，由大模型作为 Skill 调用
- **对话式交互** - 通过大模型对话采集用户信息，判断校招/社招场景
- **无前端、无数据库、无部署** - 纯脚本工具集，发布至 GitHub 即可使用
- **严谨可靠** - 输入校验、异常处理、数据本地存储

## 适用场景

| 场景 | 说明 | 典型平台 |
|------|------|----------|
| 校招 | 应届生/实习生求职，固定招聘季，流程标准化 | 牛客、企业官网校招页、实习僧 |
| 社招 | 社会招聘，常年进行，岗位要求和流程差异大 | Boss直聘、拉勾、猎聘、脉脉 |

## 核心功能（Skills）

| Skill | 功能 | 说明 |
|-------|------|------|
| `user_profile` | 用户画像采集 | 采集身份信息，判断校招/社招，生成求职画像 |
| `job_search` | 职位搜索聚合 | 根据用户画像从对应平台抓取目标岗位 |
| `job_shortlist` | 心仪岗位整理 | 整理筛选后的心仪岗位，含薪资区间分析、匹配度评估 |
| `resume_optimizer` | 简历优化 | 针对目标岗位分析简历匹配度，给出修改建议 |
| `interview_prep` | 面试准备 | 根据岗位 JD 和公司信息生成面试准备材料 |

## 技术栈

- **语言**: Python 3.10+
- **依赖管理**: pip + requirements.txt
- **执行方式**: 大模型 Skill 机制调用
- **数据存储**: 本地文件（JSON）
- **发布方式**: GitHub 仓库

## 项目结构

```
cowhorse/
├── README.md                   # 项目说明
├── requirements.txt            # Python 依赖
├── config/
│   ├── __init__.py
│   └── settings.py             # 全局配置（平台URL、参数等）
├── skills/
│   ├── user_profile/           # 用户画像采集与求职类型判断
│   │   ├── skill.md
│   │   └── script/main.py
│   ├── job_search/             # 职位搜索与聚合
│   │   ├── skill.md
│   │   └── script/main.py
│   ├── job_shortlist/          # 心仪岗位整理与薪资分析
│   │   ├── skill.md
│   │   └── script/main.py
│   ├── resume_optimizer/       # 简历优化建议
│   │   ├── skill.md
│   │   └── script/main.py
│   └── interview_prep/         # 面试准备
│       ├── skill.md
│       └── script/main.py
├── data/
│   ├── user_data.json          # 用户配置数据
│   └── shortlist.json          # 心仪岗位列表
├── utils/
│   ├── __init__.py
│   ├── exceptions.py           # 自定义异常类
│   ├── platform_adapter.py     # 招聘平台+大厂官网适配器
│   ├── parser.py               # 数据解析工具
│   └── validator.py            # 输入校验
├── tests/
│   └── ...
└── docs/
    └── development_workflow.md  # 开发流程文档
```

## 校招 vs 社招 差异

### 校招特点
- 招聘季集中（秋招 8-10月，春招 2-4月）
- 流程：网申 → 笔试 → 面试 → Offer
- 平台：企业官网校招页、牛客网、应届生求职网
- 侧重：学历、实习经历、项目经验、算法能力

### 社招特点
- 全年招聘，随时投递
- 流程：投递 → 面试（2-4轮） → Offer
- 平台：Boss直聘、拉勾、猎聘、脉脉、LinkedIn
- 侧重：工作经验、项目成果、技能匹配度

## Skill 调用流程

```
用户与大模型对话
    │
    ├─→ 大模型判断意图
    │       │
    │       ├─→ 首次使用 → 调用 user_profile skill → 采集信息 → 判断校招/社招
    │       ├─→ 找工作   → 调用 job_search skill → 返回匹配岗位列表
    │       ├─→ 整理岗位 → 调用 job_shortlist skill → 整理心仪岗位+薪资分析
    │       ├─→ 改简历   → 调用 resume_optimizer skill → 返回优化建议
    │       └─→ 准备面试 → 调用 interview_prep skill → 返回面试准备材料
    │
    └─→ 大模型整合结果返回用户
```

## 注意事项

- 本项目仅提供求职辅助工具，不保证求职结果
- 请遵守各招聘平台的使用条款和爬虫政策
- 个人数据仅存储在本地，不上传至任何服务器
- 部分功能可能因平台接口变动而需要更新适配器

## 贡献指南

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/xxx`)
3. 提交更改 (`git commit -m 'feat: 添加xxx功能'`)
4. 推送分支 (`git push origin feature/xxx`)
5. 提交 Pull Request

## License

MIT License
