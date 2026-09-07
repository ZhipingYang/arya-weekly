# Arya 个人经营周报系统 (Arya Weekly Reports)

本项目用于存放、多源数据归档与自动发布 Arya 每周经营周报的 HTML 页面，并通过 GitHub Pages 提供永久在线访问链接。

## 🌐 在线访问地址
- **周报主页（默认最新一期）**：[https://zhipingyang.github.io/arya-weekly/](https://zhipingyang.github.io/arya-weekly/)
- **历期周报归档目录**：[https://zhipingyang.github.io/arya-weekly/reports/](https://zhipingyang.github.io/arya-weekly/reports/)
- **当期周报独立链接 (2026.08.31 - 09.06 第36周)**：[https://zhipingyang.github.io/arya-weekly/reports/2026-08-31_2026-09-06.html](https://zhipingyang.github.io/arya-weekly/reports/2026-08-31_2026-09-06.html)

---

## 📁 规范项目结构

```text
arya-weekly/
├── index.html                           # 门户主页（始终重定向或展示最新一期周报）
├── reports/                             # 历期 HTML 周报存放目录
│   ├── index.html                       # 历期周报归档索引页
│   └── 2026-08-31_2026-09-06.html       # 具体某一期的周报 HTML
├── data/                                # 原始数据归档目录（一期一个独立文件夹）
│   ├── README.md                        # 数据结构与重命名规范说明
│   └── 2026-08-31_2026-09-06/           # 单期周报的多源数据包
│       ├── crm_weekly_export.xlsx       # CRM 经营主数据
│       └── ...                          # (可选其他数据：财务流水、大客进度、随手记等)
└── scripts/                             # 自动化解析与构建脚本
    └── generate_report.py               # 周报构建辅助工具
```

---

## 🚀 每周更新流程与多文件规划
1. **提供多源数据**：
   - 可以在根目录或 `data/` 下直接放入当周的一个或多个原始数据文件（如 CRM 导出表、大客户跟进表、财务流水或说明文档）。
2. **自动归档与重命名**：
   - 系统会自动创建当周专属文件夹 `data/YYYY-MM-DD_YYYY-MM-DD/`，并将文件规范化重命名（如 `crm_weekly_export.xlsx`、`high_intent_deals.xlsx` 等）。
3. **生成独立周报**：
   - 提取各文件多维数据，生成对应 `reports/YYYY-MM-DD_YYYY-MM-DD.html`。
   - 自动在顶栏下拉框及主页更新导航与链接。
4. **推送到 GitHub**：
   - 提交推送后，GitHub Pages 自动部署上线。
