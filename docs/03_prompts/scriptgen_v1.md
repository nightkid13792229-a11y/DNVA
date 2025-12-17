# DNVA Prompt Template: Script Generation (scriptgen_v1)

## Template Identity
- prompt_template_id: scriptgen_v1
- prompt_version: 1.0
- language: zh-CN
- video_ratio: 9:16
- default_tone: 专业、克制、可信

## Purpose
基于已人工确认的选题与引用来源，生成可编辑的结构化视频脚本（JSON）。
脚本必须把：
- 台词（口播/字幕）
- 分镜（场景类型、镜头说明、时长）
- 素材（每段需要哪些素材、谁执行、是否需要 prompt、验收标准、当前状态）
一一对应。

## Critical Rules (Must Follow)
1) 输出必须为严格 JSON（只输出 JSON，不要输出任何解释文字）。
2) 必须写明 run_id、topic_id、model_name、prompt_template_id、prompt_version。
3) scenes 至少 6 段，且包含：
   - 口播（A_ROLL/口播）
   - 信息图（INFO_GRAPHIC/信息图）至少 1 段
4) 不得给出“诊断/治疗建议”；只做科普与一般性建议，并包含免责声明。
5) 不得使用恐吓、绝对化用语（如“必然致癌”“100%有效”）。
6) 所有素材默认需要人工审核：
   - executor=AI 或 TOOL 的素材，prompt 字段必须提供可编辑草案
   - status 默认设为“待确认”
7) 若引用来源包含国内监管/行业信息（CN_REGULATORY_NEWS 或 CN_INDUSTRY_NEWS）：
   - 脚本中必须加入“适用范围说明”和“信息来源限定说明”
   - 避免点名品牌；如必须提及，改用“某品牌/某批次（以官方通报为准）”并提示需人工复核

## Input (Provided by DNVA)
- run_id: {{run_id}}
- model_name: {{model_name}}
- topic: {{selected_topic_object}}
- referenced_sources: {{source_items_summaries}}
- creator_constraints:
    - primary_platforms: 抖音 / 小红书（兼容多平台）
    - preferred_length_sec: {{preferred_length_sec}}  (e.g., 60-180)
    - on_camera: true  (口播由创作者本人完成)
    - chinese_no_garbled: true

## Output Format (Strict JSON)
{
  "script_id": "string",
  "run_id": "string",
  "topic_id": "string",
  "model_name": "string",
  "prompt_template_id": "scriptgen_v1",
  "prompt_version": "1.0",
  "generated_at": "ISO-8601",
  "global_disclaimer": [
    "本视频仅用于犬营养科普，不构成诊断或治疗建议。",
    "如狗狗存在疾病或特殊情况，请咨询持证兽医或兽医营养师。"
  ],
  "editable_notes": "string",
  "scenes": [
    {
      "scene_id": "scene_1",
      "scene_type": "口播 | 实拍 | 信息图 | 示意图 | 动效",
      "duration_sec": 8,
      "dialogue": "string",
      "shot": "string",
      "assets": [
        {
          "asset_id": "asset_1",
          "asset_type": "图片 | 表格 | 动效 | 实拍",
          "executor": "HUMAN | AI | TOOL",
          "prompt": "string",
          "acceptance": ["string"],
          "status": "待确认 | 生成中 | 待审核 | 已通过 | 人工制作中 | 人工已上传"
        }
      ]
    }
  ]
}

## Scene Planning Guidance
- 前 10 秒：给出冲突点/反直觉点（但克制）
- 中段：解释机制与证据（引用来源的核心结论，用通俗表达）
- 结尾：给出“可执行但不绝对”的喂养建议 + 免责声明
- 信息图/示意图素材必须明确：
  - 画面文字（中文）
  - 风格（极简、清晰）
  - 尺寸（1080x1920）
  - 关键术语（必须正确）