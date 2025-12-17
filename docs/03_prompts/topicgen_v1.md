# DNVA Prompt Template: Topic Generation (topicgen_v1)

## Template Identity
- prompt_template_id: topicgen_v1
- prompt_version: 1.0
- language: zh-CN
- primary_platforms: 抖音 / 小红书（兼容 B站 / 微信视频号 / YouTube）

## Purpose
基于 DNVA 的数据输入（分来源数据文件的摘要/条目），生成 5 条可用于短视频/中视频的候选选题。
每条选题必须：
- 具有清晰“标题钩子”（hook）
- 适合普通养狗人理解
- 明确视频类型（热点/辟谣/教程/深度解析/真实案例）
- 引用来源条目（source_refs）
- 给出风险提示（risk_notes）
- 默认 human_confirmed=false

## Critical Rules (Must Follow)
1) 输出必须为严格 JSON（只输出 JSON，不要输出任何解释文字）。
2) topics 数组长度必须为 5。
3) 必须写明 model_name、run_id、prompt_template_id、prompt_version。
4) 信息源分开存储但允许跨源组合选题；每条选题必须列出引用来源 source_id 列表。
5) 若任何引用来源包含 source_type=CN_REGULATORY_NEWS 或 CN_INDUSTRY_NEWS：
   - 该选题必须在 risk_notes 中明确标注“国内敏感信息：必须人工确认，不自动生成脚本”
   - 该选题 human_confirmed 仍为 false
6) 禁止输出夸张、恐吓、造谣式措辞；标题钩子必须是“吸引但克制”的表达。
7) 默认不自动进入脚本生成：所有选题都需要人工确认后才能进入下一步。

## Input (Provided by DNVA)
- run_id: {{run_id}}
- model_name: {{model_name}}
- academic_papers: {{academic_papers_json_or_summary}}
- academic_news: {{academic_news_json_or_summary}}
- cn_regulatory_news: {{cn_regulatory_news_json_or_summary}}
- cn_industry_news: {{cn_industry_news_json_or_summary}}
- manual_inputs: {{manual_inputs_json_or_summary}}
- creator_preference:
    - preferred_style: 专业、清晰、克制，不王婆卖瓜
    - content_focus: 犬营养与健康科普、鲜食实践
    - target_audience: 普通养狗人（可兼顾进阶用户）

## Output Format (Strict JSON)
{
  "run_id": "string",
  "model_name": "string",
  "prompt_template_id": "topicgen_v1",
  "prompt_version": "1.0",
  "generated_at": "ISO-8601",
  "topics": [
    {
      "topic_id": "topic_1",
      "title_hook": "string",
      "target_audience": "string",
      "content_type": "热点 | 辟谣 | 教程 | 深度解析 | 真实案例",
      "source_refs": ["source_id_1", "source_id_2"],
      "risk_notes": ["string", "string"],
      "human_confirmed": false
    }
  ]
}

## Generation Guidance
- 每条选题给出 1 句“标题钩子”，不要超过 22 个中文字符（尽量短）。
- risk_notes 至少 2 条，包含：
  - 外推风险（动物实验/样本量/是否可应用到宠物）
  - 平台风险（是否涉及国内监管、是否点名品牌等）
- 选题类型尽量多样化：5 条覆盖不同 content_type。