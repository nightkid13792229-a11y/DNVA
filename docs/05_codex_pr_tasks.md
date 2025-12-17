# DNVA Codex Cloud 执行任务单（PR Tasks - MVP）

本文档用于指导 Codex Cloud 按阶段提交 Pull Request。
Codex 必须严格遵守 docs/ 目录下的全部约束文档，不得自行扩展需求或功能。

参考文档（必须阅读）：
- docs/00_overview.md
- docs/01_mvp_scope.md
- docs/02_schemas.md
- docs/03_prompts/
- docs/04_acceptance_tests.md

---

## 总体执行原则（强制）

1. 严格以 MVP 为目标，不做任何未明确要求的功能
2. 不引入复杂前端框架，不做 SaaS、多用户、账号系统
3. 默认本地运行（local-first）
4. 默认所有脚本生成步骤必须人工确认
5. 所有输出必须写入 storage/runs/{run_id}/
6. 所有数据结构必须与 docs/02_schemas.md 完全一致

---

## PR-0：项目骨架与基础运行框架

目标：
建立 DNVA 最小可运行项目结构，并提供占位运行命令。

Codex 需要完成：
- 创建基础项目结构：

      dnva/
        dnva.py
        core/
        storage/
        storage/runs/
        utils/

- 提供 dnva.py，占位支持：
      python dnva.py run --step ingest
      python dnva.py run --step topicgen
      python dnva.py run --step scriptgen
      python dnva.py run --step publishpack

验收标准：
- 命令可运行
- 每个 step 会创建对应目录
- 不要求真实逻辑，仅创建占位文件

---

## PR-1：数据采集与 Ingest 模块

目标：
实现 ingest 步骤，生成符合 schemas 的数据文件。

Codex 需要完成：
- 在 ingest 步骤中支持生成以下文件（可为 mock 数据）：
      academic_papers.json
      academic_news.json
      cn_regulatory_news.json
      cn_industry_news.json
      manual_inputs.json

- 每条记录必须包含：
      region
      authority_level
      基本描述字段

- 所有文件写入：
      storage/runs/{run_id}/ingest/

验收标准：
- 文件存在
- JSON 合法
- 字段符合 docs/02_schemas.md

---

## PR-2：选题生成（Topic Generation）

目标：
调用 topicgen_v1 prompt，生成 topics_5.json。

Codex 需要完成：
- 读取 ingest 输出
- 调用（或 mock）模型生成 5 条选题
- 输出 topics_5.json 至：
      storage/runs/{run_id}/topicgen/

强制规则：
- topics 数量必须为 5
- human_confirmed 默认为 false
- 引用国内监管/行业信息时，必须生成 risk_notes

验收标准：
- topics_5.json 符合 schemas
- 不自动进入 scriptgen

---

## PR-3：人工确认机制（Human-in-the-loop）

目标：
在进入 scriptgen 前，强制要求人工确认。

Codex 需要完成：
- 提供最简人工确认方式（二选一即可）：
    - 修改 topics_5.json 中 human_confirmed 字段
    - 或提供简单 CLI 选择确认

- 未确认时：
    - 禁止生成 script.json

验收标准：
- 未确认 → scriptgen 报阻断
- 确认后 → 允许继续

---

## PR-4：脚本生成（Script Generation）

目标：
基于 scriptgen_v1 prompt 生成 script.json。

Codex 需要完成：
- 读取已确认的 topic
- 生成 script.json
- 包含：
    - 至少 6 个 scene
    - 每个 scene 至少 1 个 asset
    - asset 状态为“待确认 / 人工制作中”

输出位置：
    storage/runs/{run_id}/scriptgen/script.json

验收标准：
- JSON 合法
- 符合 docs/02_schemas.md
- 不生成任何素材文件

---

## PR-5：素材状态与占位管理

目标：
支持素材状态流转（不生成真实素材）。

Codex 需要完成：
- 在 assets/ 目录中：
    - 为每个 asset 创建占位文件或 JSON
- 支持修改状态字段：
    - 待确认
    - 生成中
    - 待审核
    - 已通过
    - 人工制作中
    - 人工已上传

强制规则：
- 所有素材未完成前：
    - 禁止进入 draft

---

## PR-6：粗剪导出（Draft Export）

目标：
在素材完成后，生成粗剪占位结果。

Codex 需要完成：
- 创建 draft/ 目录
- 生成时间线占位文件（格式不限）

验收标准：
- draft/ 目录存在
- 文件存在即可（不校验内容）

---

## PR-7：发布资料包生成（Publish Pack）

目标：
基于 publishpack_v1 prompt 生成发布资料。

Codex 需要完成：
- 生成 publish_pack/metadata.json
- 覆盖平台：
    - 抖音
    - 小红书
    - B站
    - 微信视频号
    - YouTube

验收标准：
- 每个平台 ≥5 标题
- ≥2 简介
- 标签列表存在

---

## PR-8：最终串联与回归验收

目标：
跑通一次完整流程。

Codex 需要完成：
- 从 ingest → publishpack 完整跑通
- 满足 docs/04_acceptance_tests.md 全部条件

验收标准：
- 成功生成一个完整 run_id
- 无自动越权生成脚本行为
- 所有输出可追溯

---

## 明确禁止事项（红线）

- 不得擅自增加数据库
- 不得引入复杂前端或 UI 框架
- 不得实现自动发布
- 不得修改 docs/ 中任何规范文件
- 不得合并多个 PR 为一个大 PR

---

## 完成定义

当 PR-0 至 PR-8 均被合并，且通过 docs/04_acceptance_tests.md，
DNVA MVP 即视为完成，可进入下一阶段迭代。