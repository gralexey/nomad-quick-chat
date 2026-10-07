import os

def requested_page():
    raw = os.environ.get("var_page", "")
    try:
        page = int(raw)
    except (TypeError, ValueError):
        return 1
    return page if page > 0 else 1

def visible_pages(page, total):
    if total <= 7:
        return list(range(1, total + 1))

    window = {1, total}
    for n in range(page - 2, page + 3):
        if 1 <= n <= total:
            window.add(n)

    ordered = sorted(window)
    result = []
    previous = 0
    for n in ordered:
        if previous and n > previous + 1:
            result.append(None)
        result.append(n)
        previous = n
    return result

def pagination_line(page, total_pages):
    if total_pages <= 1:
        return None

    def link(label, target):
        return f'`F8ff`_`[{label}`:/page/index.mu`page={target}]`_`f'

    def chip(label):
        return f'`!`F000`B8ff {label} `!`f`b'

    def dim(label):
        return f'`F555{label}`f'

    parts = []
    if page > 1:
        parts.append(link("<", page - 1))
        
    for n in visible_pages(page, total_pages):
        if n is None:
            parts.append(dim("…"))
        elif n == page:
            parts.append(chip(n))
        else:
            parts.append(link(str(n), n))
    if page < total_pages:
        parts.append(link(">", page + 1))
    return "`l" + "  ".join(parts)
