def current(agreements, project, day):
    candidates = [row for row in agreements if row['project'] == project and row['starts'] <= day]
    if not candidates:
        raise ValueError('当日没有有效协议')
    return max(candidates, key=lambda row: row['starts'])
