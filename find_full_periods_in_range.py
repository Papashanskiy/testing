from datetime import datetime, timedelta
import calendar


def find_full_month_in_period(_start: datetime, _end: datetime) -> list:
    """
    |This function takes two arguments start of period and end of the period
    |It returns list of tuples: month start date, month end date, 'year.month' string
    """

    def find_month_cells(start: datetime, end: datetime) -> list:
        """
        |This function takes two arguments start of period and and of period
        |It is used to find number of separate month in the provided timespan
        |It make 28 days (week) steps to find 'year cell'
        |'week cells' then ae used in another function to find start and end
        |dates of the months
        """
        result = [start]
        cur = start

        while True:
            cur = cur + timedelta(days=27)
            if cur > end:
                break
            if cur.month != result[-1].month:
                result.append(cur)
        if result[-1].month != end.month:
            result.append(end)

        return result

    if _start > _end:
        raise ValueError(f"end date {_end} should be later then start date: {_start}")

    if (_start.month == _end.month) and (_start.year == _end.year):
        return [(_start, _end, _start.strftime("%Y.%m"),)]

    m_cells = find_month_cells(_start, _end)
    result = []
    for cell in m_cells:
        _, m_end = calendar.monthrange(cell.year, cell.month)
        m_start = datetime(cell.year, cell.month, 1)
        m_end = datetime(cell.year, cell.month, m_end)
        if m_start <= _start:
            m_start = _start
        if m_end >= _end:
            m_end = _end
        result.append((m_start, m_end + timedelta(seconds=86399), m_start.strftime("%Y.%m"),))
    return result


def find_full_days_in_period(_start: datetime, _end: datetime) -> list:
    """
    | This function takes two arguments, start of the period and end of the period
    | The function returns list of dates between start date and end date
    """
    if _start > _end:
        raise ValueError(f"end date {_end} should be later then start date: {_start}")
    result = [(_start, _start + timedelta(seconds=86399), _start.strftime("%Y.%m.%d"),)]
    if _start == _end:
        return result
    cur = _start
    while True:
        cur += timedelta(days=1)
        if cur == _end:
            break
        result.append((cur, cur + timedelta(seconds=86399), cur.strftime("%Y.%m.%d"),))

    result.append((_end, _end + timedelta(seconds=86399), _end.strftime("%Y.%m.%d")))
    return result


def find_full_weeks_in_period(_start: datetime, _end: datetime) -> list:
    """
    | This function takes two arguments start of period and end of period
    | It returns list of tuples (start_week, end_week, string = 'year/week number')
    """

    def _find_weeks_cells(start: datetime, end: datetime) -> list:
        """
        |This function takes two arguments start of period and and of period
        |It is used to find number of separate weeks in the provided timespan
        |It make 7 days (week) steps to find 'week cell'
        |'week cells' then are used in another function to find start and end
        | dates of the weeks
        """
        _dates = [start]
        cur = start
        while True:
            cur = cur + timedelta(days=7)
            if cur >= end:
                break
            _dates.append(cur)
        if _dates[-1].isocalendar()[1] != end.isocalendar()[1]:
            _dates.append(end)
        return _dates

    if _end < _start:
        raise ValueError(f"end date {_end} should be later then start date: {_start}")

    if _start.isocalendar()[1] == _end.isocalendar()[1]:    # the error is here
        return [(_start, _end + timedelta(seconds=86399), str(_start.year) + "/" + str(_start.isocalendar()[1]),)]

    cells = _find_weeks_cells(_start, _end)
    result = []
    for cell in cells:
        w_start = cell - timedelta(days=cell.weekday())
        w_end = w_start + timedelta(days=6)
        if w_start <= _start:
            w_start = _start
        if w_end >= _end:
            w_end = _end
        result.append(
            (w_start, w_end + timedelta(seconds=86399), str(w_start.year) + "/" + str(w_start.isocalendar()[1]),))
    return result


if __name__ == "__main__":

    result = find_full_weeks_in_period(datetime(1892, 6, 1), datetime(1893, 6, 7))
    print("Total weeks: {}".format(len(result)))
    print(" {:^30} | {:^30} | {:^50}".format("start", "end", ""))
    for i in result:
        print(" {:^30} | {:^30} | {:50}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))
    print(type(result))
