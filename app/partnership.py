from collections import Counter


def evidence(stories, work, agreement):
    publications = Counter(row['published_by'] for row in stories)
    return {'agreement': agreement['id'], 'assigned_roles': agreement['roles'],
            'hours': work['hours'], 'work_to_review': work['review'], 'publications': dict(publications)}
