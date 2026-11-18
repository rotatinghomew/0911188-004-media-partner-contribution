# 联合报道协作台账

合作协议、联合稿件与工作记录。当前总览只按合作方汇总登记工时。

样例数据均为本地合成记录，不对应真实个人、媒体、机构或交易。项目使用 Python 3.11.2 标准库，数据随项目保存，不访问外部服务。

## 使用

在项目根目录运行 `python3 -m app summary` 查看按当前基础口径生成的 JSON 总览。

## 验证

运行 `python3 -m unittest discover -s tests -v` 和 `python3 -m compileall -q app tests`。

## 结构

`data/data.json` 保存领域记录与基础汇总口径；`app/storage.py` 读取并检查数据形状；`app/analysis.py` 计算基础分组统计；`app/service.py` 组合数据读取和统计；`tests/` 验证产品入口及无效数据处理。

## 工作台

续约会现在以期末协议为准核已确认工时。`roles` 显示期末角色；`worklog` 对照角色核计工时，把其余条目标到待复核；`credits` 生成续约会议用归档；`renewal` 打开归档。署名发布次数与工时本来就是不同栏目。

可用 `python3 -m app worklog --key shared-coast` 查看当前记录。协议从 `starts` 当天起生效，所列 `roles` 是整份名单。`supersedes` 列出稿件前次修订，工作记录引用实际修订；`reuse` 是编辑对沿用工作的复核，前版存在不表示一定沿用。`outcomes` 是各发布方另行收到的反馈，不是工时，在当前归档中未使用。

操作数据在 `data/workbench.json`。工作台涉及的领域代码：`agreements` 判定谁有资格承担角色, `worklog` 核定已确认工时, `partnership` 生成供续约会查阅的贡献档案。已有总览仍使用 `data/data.json`。
