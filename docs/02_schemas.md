# DNVA 数据结构定义（Schemas - MVP）

本文件定义 DNVA 在 MVP 阶段使用的核心数据结构（JSON 规范）。
所有数据仅用于内部处理与 UI 展示，不对外作为公共 API。

---

## 一、总原则（强制）

1. 不同信息来源分开存储
2. 所有信息源默认不自动生成视频脚本
3. 所有脚本生成步骤必须经过人工确认
4. 所有数据必须标注：
   - 地区
   - 权威程度
   - 是否需要人工审核

---

## 二、地区枚举（Region）

    CN_MAINLAND    中国大陆
    CN_HKMO_TW     港澳台
    INTL           国外

---

## 三、信息源类型（Source Type）

    ACADEMIC_PAPER        学术论文（国外为主）
    ACADEMIC_NEWS         学术新闻 / 科研通稿（国外）
    CN_REGULATORY_NEWS    国内安全 / 监管信息（官方）
    CN_INDUSTRY_NEWS      国内行业新闻
    MANUAL_INPUT          人工输入的热点 / 观察

---

## 四、权威程度（Authority Level）

    OFFICIAL    官方来源
    HIGH        高度权威
    MEDIUM      一般可靠
    LOW         参考价值有限

---

## 五、运行记录（run.json）

    {
      "run_id": "string",
      "created_at": "ISO-8601",
      "step": "INGEST | TOPIC | SCRIPT | ASSET | DRAFT | PUBLISH",
      "sources_used": [
        {
          "source_id": "string",
          "source_type": "ACADEMIC_NEWS",
          "region": "INTL",
          "authority_level": "HIGH"
        }
      ],
      "human_confirmed": true,
      "outputs": {
        "topics": "topics_5.json",
        "script": "script.json",
        "publish_pack": "publish_pack/"
      }
    }

---

## 六、学术论文数据（academic_papers.json）

    {
      "papers": [
        {
          "paper_id": "string",
          "title": "string",
          "abstract": "string",
          "journal": "string",
          "published_at": "ISO-8601",
          "region": "INTL",
          "authority_level": "HIGH",
          "tags": ["canine", "nutrition"],
          "notes": "string"
        }
      ]
    }

---

## 七、学术新闻数据（academic_news.json）

    {
      "news": [
        {
          "news_id": "string",
          "title": "string",
          "summary": "string",
          "source_name": "string",
          "published_at": "ISO-8601",
          "region": "INTL",
          "authority_level": "HIGH",
          "related_paper_ids": ["paper_id"],
          "notes": "string"
        }
      ]
    }

---

## 八、国内监管 / 安全信息（cn_regulatory_news.json）

    {
      "news": [
        {
          "news_id": "string",
          "title": "string",
          "summary": "string",
          "issuing_body": "string",
          "published_at": "ISO-8601",
          "region": "CN_MAINLAND",
          "authority_level": "OFFICIAL",
          "notes": "string"
        }
      ]
    }

---

## 九、国内行业新闻（cn_industry_news.json）

    {
      "news": [
        {
          "news_id": "string",
          "title": "string",
          "summary": "string",
          "source_name": "string",
          "published_at": "ISO-8601",
          "region": "CN_MAINLAND",
          "authority_level": "MEDIUM",
          "notes": "string"
        }
      ]
    }

---

## 十、人工输入内容（manual_inputs.json）

    {
      "inputs": [
        {
          "input_id": "string",
          "title": "string",
          "description": "string",
          "created_at": "ISO-8601",
          "notes": "string"
        }
      ]
    }

---

## 十一、选题结果（topics_5.json）

    {
      "topics": [
        {
          "topic_id": "string",
          "title_hook": "string",
          "target_audience": "string",
          "content_type": "热点 | 辟谣 | 教程 | 深度解析 | 真实案例",
          "source_refs": ["source_id"],
          "risk_notes": ["string"],
          "human_confirmed": false
        }
      ]
    }

---

## 十二、视频脚本（script.json）

    {
      "script_id": "string",
      "topic_id": "string",
      "model_name": "deepseek-v3.2",
      "global_disclaimer": ["string"],
      "editable_notes": "string",
      "scenes": [
        {
          "scene_id": "string",
          "scene_type": "口播 | 实拍 | 信息图 | 示意图 | 动效",
          "duration_sec": 6,
          "dialogue": "string",
          "shot": "string",
          "assets": [
            {
              "asset_id": "string",
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

---

## 十三、发布资料包元信息（publish_pack/metadata.json）

    {
      "run_id": "string",
      "topic_id": "string",
      "platforms": ["抖音", "小红书", "B站", "微信视频号", "YouTube"],
      "model_name": "deepseek-v3.2",
      "generated_at": "ISO-8601",
      "notes": "string"
    }