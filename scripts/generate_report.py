# -*- coding: utf-8 -*-
import re

def main():
    # Read the current working HTML from reports/2026-08-31_2026-09-06.html
    with open('reports/2026-08-31_2026-09-06.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update viewport
    html = html.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">'
    )

    # 2. Add full responsive CSS inside <style>
    responsive_css = """
/* Responsive table container */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
.table-scroll-hint {
  display: none;
  align-items: center;
  justify-content: center;
  gap: 4px;
  font-size: 11px;
  color: var(--text2);
  margin-bottom: 8px;
  padding: 4px 0;
  background: #f8fafc;
  border-radius: 6px;
}

/* ====================================================
   MOBILE OPTIMIZATIONS (Screen <= 768px)
   ==================================================== */
@media (max-width: 768px) {
  body {
    padding-bottom: 30px;
  }
  .nav-inner {
    padding: 8px 10px;
    gap: 6px;
    flex-wrap: nowrap;
  }
  .nav-left {
    gap: 6px;
    flex: 1;
    min-width: 0;
  }
  .nav-brand {
    font-size: 14px;
    flex-shrink: 0;
  }
  .nav-brand span {
    display: none;
  }
  .report-select {
    font-size: 11px;
    padding: 4px 6px;
    width: 100%;
    min-width: 0;
    max-width: 145px;
    text-overflow: ellipsis;
  }
  .nav-right {
    flex-shrink: 0;
  }
  .btn-action {
    padding: 4px 8px;
    font-size: 11px;
  }
  .btn-gh {
    display: none !important;
  }
  .container {
    margin: 10px auto 0;
    padding: 0 8px;
  }
  .header {
    padding: 18px 14px;
    border-radius: 12px;
    margin-bottom: 14px;
  }
  .header h1 {
    font-size: 18px;
    margin-bottom: 4px;
  }
  .header .sub {
    font-size: 11px;
    margin-bottom: 8px;
    line-height: 1.4;
  }
  .header .badge {
    font-size: 10px;
    padding: 5px 8px;
    line-height: 1.4;
    display: block;
    text-align: center;
    border-radius: 8px;
  }
  .section {
    margin-bottom: 18px;
  }
  .section-title {
    font-size: 15px;
    margin-bottom: 10px;
    padding-left: 8px;
    border-left-width: 3px;
  }
  .section-title .num {
    width: 20px;
    height: 20px;
    font-size: 10px;
  }
  .card {
    padding: 12px 10px;
    border-radius: 10px;
    margin-bottom: 10px;
  }
  .kpi-row {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 6px;
    margin-bottom: 10px;
  }
  .kpi-card {
    padding: 10px 4px !important;
    border-radius: 8px;
  }
  .kpi-val {
    font-size: 19px !important;
    margin: 3px 0 2px;
    white-space: nowrap;
    letter-spacing: -0.5px;
  }
  .kpi-val span {
    font-size: 11px !important;
  }
  .kpi-label {
    font-size: 10px;
    line-height: 1.2;
  }
  .chart-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }
  .chart-box {
    padding: 12px 8px;
    border-radius: 10px;
  }
  .chart-container {
    height: 240px !important;
  }
  #chart_sankey {
    height: 290px !important;
  }
  .table-scroll-hint {
    display: flex !important;
  }
  table {
    font-size: 11px !important;
    min-width: 480px;
  }
  th, td {
    padding: 6px 7px !important;
  }
  .tag {
    padding: 1px 5px !important;
    font-size: 9px !important;
  }
  .timeline {
    padding-left: 18px;
  }
  .timeline::before {
    left: 5px;
  }
  .timeline-item::before {
    left: -16px;
    width: 8px;
    height: 8px;
  }
  .timeline-item .day {
    font-size: 12px;
  }
  .evt {
    font-size: 10px;
    padding: 2px 5px;
  }
  .insight-card, .highlight-card, .problem-card {
    padding: 10px 12px;
    margin-bottom: 8px;
  }
  .insight-card h4, .highlight-card h4, .problem-card h4 {
    font-size: 12px;
    margin-bottom: 3px;
  }
  .insight-card p, .highlight-card p, .problem-card p {
    font-size: 11px;
    line-height: 1.5;
  }
}
"""
    # Inject CSS before </style>
    if '.table-responsive' not in html:
        html = html.replace('</style>', responsive_css + '\n</style>')

    # 3. Add table-responsive and scroll hints around tables
    hint = '<div class="table-scroll-hint">👈 左右滑动查看完整表格 👉</div>\n<div class="table-responsive">\n'
    # Wrap tables that are not yet wrapped
    html = re.sub(r'(<div class="card"[^>]*>)\s*(<table>)', r'\1\n' + hint + r'\2', html)
    html = re.sub(r'(<div class="card"[^>]*>\s*<h4[^>]*>.*?</h4>)\s*(<table>)', r'\1\n' + hint + r'\2', html, flags=re.DOTALL)
    # Close div for table-responsive before closing card
    html = re.sub(r'(</table>)\s*(</div>\s*<!--\s*模块)', r'\1\n</div>\n\2', html)

    # 4. Make KPI 52分钟 clean
    html = html.replace('52<span style="font-size:16px">分钟</span>', '52 <span style="font-size:13px;font-weight:normal">分钟</span>')
    html = html.replace('52<span style="font-size:15px">分钟</span>', '52 <span style="font-size:13px;font-weight:normal">分钟</span>')

    # 5. Fix navbar button class
    html = html.replace('<a href="https://github.com/ZhipingYang/arya-weekly" target="_blank" class="btn-action btn-primary">', '<a href="https://github.com/ZhipingYang/arya-weekly" target="_blank" class="btn-action btn-primary btn-gh">')

    # Save to reports/2026-08-31_2026-09-06.html
    with open('reports/2026-08-31_2026-09-06.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated reports/2026-08-31_2026-09-06.html')

    # Generate index.html (root version with correct relative links)
    root_html = html.replace('href="./index.html"', 'href="./index.html"')
    root_html = root_html.replace('value="./2026-08-31_2026-09-06.html"', 'value="./reports/2026-08-31_2026-09-06.html"')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(root_html)
    print('Updated index.html')

if __name__ == '__main__':
    main()
