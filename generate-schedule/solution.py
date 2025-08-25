def solve(n: int) -> list[list[int]]:
    if n % 2 == 1:
        return []

    schedule = []
    teams = list(range(n))
    
    for i in range(2 * (n - 1)):
        day_schedule = []
        for j in range(n // 2):
            home = teams[j]
            away = teams[n - 1 - j]
            day_schedule.append([home, away])
        
        # Rotate the list to ensure no team plays on consecutive days
        teams.insert(1, teams.pop())
        schedule.extend(day_schedule)
    
    return schedule