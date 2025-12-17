"""
Ingest module for DNVA.

PR-1 implements a minimal ingest flow that emits structured,
region-tagged items into storage/runs/{run_id}/ingest/.
"""

import json
import os
from typing import Dict, List

from dnva.core.models import IngestItem, SourceDefinition


def _write_json(path: str, data) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _write_jsonl(path: str, items: List[IngestItem]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item.to_dict(), ensure_ascii=False))
            f.write("\n")


def _build_item(
    source: SourceDefinition,
    suffix: int,
    title: str,
    url: str,
    summary: str,
    published_at: str,
    tags: List[str],
    raw_ref: str,
) -> IngestItem:
    return IngestItem(
        item_id=f"{source.source_id}-{suffix}",
        source_id=source.source_id,
        source_name=source.source_name,
        source_type=source.source_type,
        region=source.region,
        authority_level=source.authority_level,
        title=title,
        url=url,
        published_at=published_at,
        summary=summary,
        tags=tags,
        has_case=False,
        raw_ref=raw_ref,
    )


SOURCE_DEFINITIONS: List[SourceDefinition] = [
    SourceDefinition(
        source_id="cn_food_safety_alerts",
        source_name="CN Pet Food Safety Alerts",
        source_type="regulatory",
        region="CN_MAINLAND",
        authority_level="HIGH",
        base_url="https://example.cn/alerts",
        notes="Mocked regulatory bulletins focusing on pet food safety.",
    ),
    SourceDefinition(
        source_id="cn_industry_watch",
        source_name="CN Pet Nutrition Industry Watch",
        source_type="industry",
        region="CN_MAINLAND",
        authority_level="MEDIUM",
        base_url="https://example.cn/industry",
        notes="Mocked trade association updates and product advisories.",
    ),
    SourceDefinition(
        source_id="global_academic_digest",
        source_name="Global Canine Nutrition Academic Digest",
        source_type="academic",
        region="GLOBAL",
        authority_level="HIGH",
        base_url="https://example.org/academic",
        notes="Mocked summaries of peer-reviewed studies.",
    ),
    SourceDefinition(
        source_id="global_health_news",
        source_name="Global Veterinary Health Newswire",
        source_type="news",
        region="GLOBAL",
        authority_level="MEDIUM",
        base_url="https://example.org/healthnews",
        notes="Mocked press releases and lab statements.",
    ),
]


STUB_ITEMS: Dict[str, List[Dict[str, object]]] = {
    "cn_food_safety_alerts": [
        {
            "title": "农业农村部发布犬用零食抽检结果，2 批次氧化值超标",
            "url": "https://example.cn/alerts/2024-11-15-oxidation",
            "summary": "官方抽检发现两款进口犬用零食氧化值超出安全阈值，要求下架并复检。",
            "published_at": "2024-11-15T08:00:00+08:00",
            "tags": ["pet food", "safety", "oxidation"],
            "raw_ref": "CN-MARA-2024-11-15-A1",
        },
        {
            "title": "北京市场监管局通报犬主粮标签核查，要求标明钙磷比",
            "url": "https://example.cn/alerts/2024-12-02-labeling",
            "summary": "监管部门抽查发现部分犬主粮未标注关键营养比，已责令整改。",
            "published_at": "2024-12-02T10:30:00+08:00",
            "tags": ["labeling", "calcium-phosphorus", "regulatory"],
            "raw_ref": "BJ-AMR-2024-12-02-L2",
        },
        {
            "title": "上海发布宠物食品召回提醒：单批次维生素 D 超标",
            "url": "https://example.cn/alerts/2024-12-10-vitd",
            "summary": "召回批次为 20241012，提醒经销商暂停销售并通知消费者。",
            "published_at": "2024-12-10T09:15:00+08:00",
            "tags": ["recall", "vitamin D", "safety"],
            "raw_ref": "SH-MARKET-2024-12-10-R3",
        },
    ],
    "cn_industry_watch": [
        {
            "title": "华东宠食协会发布鲜粮冷链指南，强调 4 小时内入冷藏",
            "url": "https://example.cn/industry/2024-11-coldchain",
            "summary": "指南建议鲜粮配送全程留痕，温控不达标需重做批次。",
            "published_at": "2024-11-08T14:20:00+08:00",
            "tags": ["fresh food", "cold chain", "guideline"],
            "raw_ref": "CNSA-GUIDE-2024-11-08",
        },
        {
            "title": "国产单一蛋白犬粮新品发布，强调对敏感犬的适口性试验",
            "url": "https://example.cn/industry/2024-12-single-protein",
            "summary": "企业披露 6 周适口性与消化耐受性小样本测试数据。",
            "published_at": "2024-12-05T16:00:00+08:00",
            "tags": ["single protein", "digestibility", "product launch"],
            "raw_ref": "CNSA-PROD-2024-12-05",
        },
    ],
    "global_academic_digest": [
        {
            "title": "北欧多中心研究：高纤维鲜粮可改善犬胆汁酸代谢",
            "url": "https://example.org/academic/2024-fiber-bile-acids",
            "summary": "42 只犬为期 12 周的随机对照试验显示高纤维饮食降低胆汁酸盐堆积。",
            "published_at": "2024-10-28T11:00:00Z",
            "tags": ["academic", "fiber", "microbiome"],
            "raw_ref": "DOI:10.1234/dog.fiber.2024",
        },
        {
            "title": "加拿大团队发表犬慢性肠炎与短链脂肪酸相关性研究",
            "url": "https://example.org/academic/2024-ce-scfa",
            "summary": "粪便代谢组分析显示丁酸盐水平与症状缓解呈正相关。",
            "published_at": "2024-09-12T09:30:00Z",
            "tags": ["SCFA", "IBD", "canine"],
            "raw_ref": "DOI:10.5678/canine.ibd.2024",
        },
        {
            "title": "日本兽医大学：蛋白质过敏犬的水解配方双盲试验",
            "url": "https://example.org/academic/2024-hydrolyzed-diet",
            "summary": "试验组在 8 周内瘙痒评分下降 35%，未见严重不良事件。",
            "published_at": "2024-11-01T07:45:00Z",
            "tags": ["allergy", "hydrolyzed protein", "clinical trial"],
            "raw_ref": "DOI:10.9101/canine.allergy.2024",
        },
    ],
    "global_health_news": [
        {
            "title": "欧盟食品安全局提醒家庭自制宠粮需关注铜摄入上限",
            "url": "https://example.org/healthnews/2024-10-efsa-copper",
            "summary": "EFSA 在简报中引用近 3 年病例，建议遵循 NRC 铜摄入指导。",
            "published_at": "2024-10-05T12:00:00Z",
            "tags": ["EFSA", "copper", "home-cooked"],
            "raw_ref": "EFSA-NOTE-2024-10-05",
        },
        {
            "title": "美国 FDA：未验证的关节保健补剂勿替代正规处方",
            "url": "https://example.org/healthnews/2024-12-fda-joint-supplement",
            "summary": "FDA 指出部分网售补剂含量与标签不符，提醒宠主咨询兽医。",
            "published_at": "2024-12-03T15:10:00Z",
            "tags": ["FDA", "supplement", "joint health"],
            "raw_ref": "FDA-ALERT-2024-12-03",
        },
    ],
}


def run_ingest(run_id: str, base_path: str) -> Dict[str, str]:
    """
    Generate deterministic mock ingest outputs for a run.
    """
    ingest_dir = os.path.join(base_path, "ingest")
    os.makedirs(ingest_dir, exist_ok=True)

    items: List[IngestItem] = []
    for source in SOURCE_DEFINITIONS:
        payloads = STUB_ITEMS.get(source.source_id, [])
        for idx, payload in enumerate(payloads, start=1):
            items.append(
                _build_item(
                    source=source,
                    suffix=idx,
                    title=payload["title"],
                    url=payload["url"],
                    summary=payload["summary"],
                    published_at=payload["published_at"],
                    tags=payload.get("tags", []),
                    raw_ref=payload["raw_ref"],
                )
            )

    items_path = os.path.join(ingest_dir, "items.jsonl")
    sources_path = os.path.join(ingest_dir, "sources.json")

    _write_jsonl(items_path, items)
    _write_json(sources_path, [s.to_dict() for s in SOURCE_DEFINITIONS])

    return {
        "items_path": items_path,
        "sources_path": sources_path,
        "item_count": len(items),
    }
