# 数据目录结构规范 (Data Directory Specification)

每个周报对应一个独立的日期范围文件夹：`data/YYYY-MM-DD_YYYY-MM-DD/`

如果当周提供的是**多种类型、多个文件**的数据（例如：CRM系统导出、财务到账流水、运营跟进记录、沟通要点等），可直接放入当周对应的文件夹中。

---

## 推荐目录与文件命名示例

```text
data/
└── 2026-08-31_2026-09-06/                    # 单期周报数据文件夹（开始日期_结束日期）
    ├── crm_weekly_export.xlsx                # 主经营数据/CRM数据导出
    ├── finance_settlement.xlsx               # (可选) 财务到账与打款明细
    ├── high_intent_deals.xlsx                # (可选) 高意向客户跟进表
    ├── monthly_target.xlsx                   # (可选) 月度目标/KPI基准表
    └── notes.md                              # (可选) 本周主观总结、重点异常说明、下周规划等
```

---

## 常用命名标准（重命名规则）

| 文件类别 | 推荐规范文件名 | 说明 |
| :--- | :--- | :--- |
| **主经营/销售数据** | `crm_weekly_export.xlsx` | 包含线索、商机、成单、漏斗等综合数据 |
| **财务/业绩流水** | `finance_settlement.xlsx` | 实际到款、回款进度、发票开具数据 |
| **高价值商机/意向客** | `high_intent_deals.xlsx` | 重点大客户跟进情况与下步推进计划 |
| **目标进度对比** | `target_progress.xlsx` | 当月/当季目标完成率参照数据 |
| **文本说明/要点** | `notes.md` 或 `summary.txt` | 纯文本备忘、业务背景、异常原因与应对策略 |

---

## 注意事项
1. **文件夹名**统一采用 `YYYY-MM-DD_YYYY-MM-DD`（如 `2026-08-31_2026-09-06`），与生成的 `reports/YYYY-MM-DD_YYYY-MM-DD.html` 一一对应。
2. 即使你扔进来的文件是随意的中文名、系统导出带长串时间戳的名字，我也都会自动识别、标准化重命名并归档到对应的周报文件夹中。
