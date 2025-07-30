def solve(s: str) -> list[str]:
    segments = []
    seen = set()
    current_segment = []

    for char in s:
        if ''.join(current_segment + [char]) not in seen:
            current_segment.append(char)
        else:
            segments.append(''.join(current_segment))
            seen.update(segments[-1])
            current_segment = [char]

    if current_segment:
        segments.append(''.join(current_segment))

    return segments