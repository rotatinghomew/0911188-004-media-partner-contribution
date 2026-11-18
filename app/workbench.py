import json
from .agreements import current
from .journal import packet
from .partnership import evidence
from .worklog import accepted


def run_workbench(action, directory, key, ledger):
    project = key or 'shared-coast'
    if action == 'renewal':
        return packet(ledger, 'renewal', project)
    source = json.loads((directory / 'workbench.json').read_text())
    agreement = current(source['agreements'], project, source['date'])
    if action == 'roles':
        return agreement
    stories = [row for row in source['stories'] if row['project'] == project]
    story_ids = {row['id'] for row in stories}
    revision_ids = {row['id'] for row in source['revisions'] if row['story'] in story_ids}
    work = accepted(source['work'], revision_ids, agreement['roles'])
    if action == 'worklog':
        return work
    return packet(ledger, 'renewal', project, evidence(stories, work, agreement))
