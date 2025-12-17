# DNVA 验收标准与运行说明（Acceptance Tests - MVP）

本文档用于定义 DNVA 在 MVP 阶段的“是否算完成”的判断标准。
任何由 Codex / 人工实现的功能，必须通过本文件中定义的验收条件，才视为合格。

---

## 一、总体验收原则

1. 所有流程必须可重复运行（同样输入 → 稳定输出结构）
2. 所有关键步骤必须可人工介入与确认
3. 所有输出必须落盘为文件（JSON / 目录）
4. 系统不得在未人工确认的情况下自动生成视频脚本

---

## 二、目录结构验收

在一次完整运行结束后，项目目录中必须存在如下结构：

    storage/
      runs/
        {run_id}/
          ingest/
          topicgen/
          scriptgen/
          assets/
          draft/
          publish_pack/

验收标准：
- run_id 目录存在
- 每个子目录至少包含一个输出文件或占位文件
- 不允许将运行产物写入 docs/ 目录

---

## 三、数据采集（Ingest）验收

位置：
    storage/runs/{run_id}/ingest/

必须存在至少以下文件之一：
    academic_papers.json
    academic_news.json
    cn_regulatory_news.json
    cn_industry_news.json
    manual_inputs.json

验收标准：
- 文件内容为合法 JSON
- 每条记录包含：
  - region
  - authority_level
  - 来源名称或说明
- 国内监管/行业数据未被标记为“可自动生成脚本”

---

## 四、选题生成（Topic Generation）验收

位置：
    storage/runs/{run_id}/topicgen/topics_5.json

验收标准：
- topics 数组长度 == 5
- 每个 topic 包含：
  - topic_id
  - title_hook
  - content_type
  - source_refs
  - risk_notes
  - human_confirmed = false
- 至少 2 条选题包含明确风险提示
- 若引用国内监管/行业信息：
  - risk_notes 中必须包含“需人工确认/国内敏感信息”相关描述

---

## 五、人工确认（Human-in-the-loop）验收

验收标准：
- 在 human_confirmed=false 状态下：
  - 不得生成 script.json
- 只有当 human_confirmed=true：
  - 才允许进入脚本生成步骤
- 人工确认行为必须被记录（文件或字段即可，形式不限）

---

## 六、脚本生成（Script Generation）验收

位置：
    storage/runs/{run_id}/scriptgen/script.json

验收标准：
- 输出为合法 JSON
- 包含字段：
  - script_id
  - run_id
  - topic_id
  - model_name
  - scenes（数组，长度 >= 6）
- scenes 中必须至少包含：
  - 1 段口播
  - 1 段信息图或示意图
- 每个 scene 至少包含一个 asset
- 所有 asset 初始状态为：
  - 待确认 或 人工制作中
- 脚本中包含免责声明字段

---

## 七、素材状态流转验收

位置：
    storage/runs/{run_id}/assets/

验收标准：
- 每个 asset 至少具备以下状态之一：
  - 待确认
  - 生成中
  - 待审核
  - 已通过
  - 人工制作中
  - 人工已上传
- 任何 AI/工具生成素材：
  - 在 prompt 未人工确认前，不得进入“生成中”
- 所有素材未达“已通过 / 人工已上传”前：
  - 不得进入粗剪导出步骤

---

## 八、粗剪导出（Draft Export）验收

位置：
    storage/runs/{run_id}/draft/

验收标准：
- 目录存在
- 包含：
  - 时间线结构文件（格式不限）
  - 素材引用占位
- 不要求：
  - 精剪
  - 转场
  - 调色
  - 音频处理
- 目标仅为：
  - 能被人工用于后续剪辑

---

## 九、发布资料包（Publish Pack）验收

位置：
    storage/runs/{run_id}/publish_pack/

必须存在：
    metadata.json

metadata.json 验收标准：
- 包含平台：
  - 抖音
  - 小红书
  - B站
  - 微信视频号
  - YouTube
- 每个平台至少包含：
  - 5 条标题
  - 2 条简介
  - 标签列表
  - 封面文案建议

---

## 十、一键运行（开发态）验收

MVP 阶段允许使用占位命令。

示例（仅用于验收说明）：

    python dnva.py run --step ingest
    python dnva.py run --step topicgen
    python dnva.py run --step scriptgen
    python dnva.py run --step publishpack

验收标准：
- 每一步单独执行不报错
- 每一步执行后生成对应目录与文件
- 允许人工在步骤间修改 JSON 再继续运行

---

## 十一、失败容忍与回滚

验收标准：
- 任一步失败：
  - 不影响已有 run_id 目录
  - 不覆盖历史运行结果
- 允许重新执行某一步生成新的文件版本

---

## 十二、MVP 完成判定

当且仅当满足以下条件，DNVA MVP 视为完成：

- 完成一次完整 run_id 流程
- 人工成功确认至少 1 条选题并生成脚本
- 成功生成发布资料包
- 全流程无“自动越权生成脚本”行为

---

## 十三、明确不在 MVP 验收范围内

- 性能优化
- 多用户支持
- 自动发布到平台
- 商业化计费
- 权限与账号系统