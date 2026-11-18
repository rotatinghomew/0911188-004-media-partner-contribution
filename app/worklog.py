from collections import Counter


def accepted(work, revision_ids, active_roles):
    amounts = Counter()
    awaiting = []
    for row in work:
        if row['revision'] not in revision_ids:
            continue
        if row['state'] == 'confirmed' and row['partner'] in active_roles:
            amounts[row['partner']] += row['hours']
        else:
            awaiting.append(row['id'])
    return {'hours': dict(amounts), 'review': awaiting}
