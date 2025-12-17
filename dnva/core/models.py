"""
Data models for DNVA ingest step.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class SourceDefinition:
    source_id: str
    source_name: str
    source_type: str
    region: str
    authority_level: str
    base_url: str = ""
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_id": self.source_id,
            "source_name": self.source_name,
            "source_type": self.source_type,
            "region": self.region,
            "authority_level": self.authority_level,
            "base_url": self.base_url,
            "notes": self.notes,
        }


@dataclass
class IngestItem:
    item_id: str
    source_id: str
    source_name: str
    source_type: str
    region: str
    authority_level: str
    title: str
    url: str
    published_at: str
    summary: str
    tags: List[str] = field(default_factory=list)
    has_case: bool = False
    raw_ref: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_id": self.item_id,
            "source_id": self.source_id,
            "source_name": self.source_name,
            "source_type": self.source_type,
            "region": self.region,
            "authority_level": self.authority_level,
            "title": self.title,
            "url": self.url,
            "published_at": self.published_at,
            "summary": self.summary,
            "tags": self.tags,
            "has_case": self.has_case,
            "raw_ref": self.raw_ref,
        }
