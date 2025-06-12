def solve(landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
    def earliest_finish_time(start_times, durations):
        return max(max(start + duration for start in starts) for starts, duration in zip(start_times, durations))

    # Calculate the earliest finish time for both sequences
    land_to_water = earliest_finish_time(landStartTime, landDuration)
    water_to_land = earliest_finish_time(waterStartTime, waterDuration)

    # Return the minimum of the two possible sequences
    return min(land_to_water, water_to_land)