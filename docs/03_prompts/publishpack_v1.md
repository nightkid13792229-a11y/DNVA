# DNVA Prompt Template: Publish Pack Generation (publishpack_v1)

## Template Identity
- prompt_template_id: publishpack_v1
- prompt_version: 1.0
- language: zh-CN

## Purpose
基于已人工确认的脚本内容，生成多平台发布资料（不自动发布，仅生成资料包内容）。

## Critical Rules (Must Follow)
1) 输出必须为严格 JSON（只输出 JSON，不要输出任何解释文字）。
2) 必须包含 run_id、topic_id、model_name、prompt_template_id、prompt_version。
3) 覆盖平台：抖音、小红书、B站、微信视频号、YouTube。
4) 所有平台都必须提供：
   - 标题候选 >= 5
   - 简介/文案 >= 2（长短两版）
   - 标签/话题 >= 10
5) 禁止夸大、恐吓、绝对化词汇；如涉及国内监管/安全类内容必须更克制，且加入提示语。
6) 生成“封面文案”建议（不生成图片本身），用于后续封面制作。

## Input (Provided by DNVA)
- run_id: {{run_id}}
- topic_id: {{topic_id}}
- model_name: {{model_name}}
- script_summary: {{script_summary}}
- key_takeaways: {{key_takeaways}}
- risk_profile: {{risk_profile}}

## Output Format (Strict JSON)
{
  "run_id": "string",
  "topic_id": "string",
  "model_name": "string",
  "prompt_template_id": "publishpack_v1",
  "prompt_version": "1.0",
  "generated_at": "ISO-8601",
  "platforms": {
    "DOUYIN": {
      "titles": ["string", "string", "string", "string", "string"],
      "descriptions": ["string", "string"],
      "tags": ["string"],
      "cover_text_suggestions": ["string"]
    },
    "XHS": {
      "titles": ["string", "string", "string", "string", "string"],
      "descriptions": ["string", "string"],
      "tags": ["string"],
      "cover_text_suggestions": ["string"]
    },
    "BILIBILI": {
      "titles": ["string", "string", "string", "string", "string"],
      "descriptions": ["string", "string"],
      "tags": ["string"],
      "cover_text_suggestions": ["string"]
    },
    "WECHAT_CHANNELS": {
      "titles": ["string", "string", "string", "string", "string"],
      "descriptions": ["string", "string"],
      "tags": ["string"],
      "cover_text_suggestions": ["string"]
    },
    "YOUTUBE": {
      "titles": ["string", "string", "string", "string", "string"],
      "descriptions": ["string", "string"],
      "tags": ["string"],
      "cover_text_suggestions": ["string"]
    }
  }
}

## Style Guidance
- 抖音：短、强钩子，但克制；避免过度标题党
- 小红书：更生活化，允许“避坑/建议”语气，但必须准确
- B站：更完整，强调“依据/来源/逻辑”
- 微信视频号：更稳健，少情绪化词
- YouTube：可加少量英文关键词，但主体仍中文（MVP 阶段）