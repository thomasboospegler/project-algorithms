def study_schedule(permanence_period, target_time):
    try:
        return len(
            [
                period
                for period in permanence_period
                if period[0] <= target_time <= period[1]
            ]
        )
    except TypeError:
        return None
