from datetime import datetime
# The module is used to calculate full time outage periods in the chosen timeframe


class Period:
    def __init__(self):
        self.start = None  # example (787513, 1543987071, 1) = (id in db, epoch time Unix, event type)
        self.end = None

    def set_start(self, _start):
        self.start = _start

    def set_end(self, _end):
        self.end = _end

    def calculate_period_length(self):
        """
        | (787513, 1543987071, 1) - example of input (id in db, epoch time Unix, event type)
        | event types:
        | 1 is start of outage
        | 0 is end of outage
        | 100 is start of searched timeframe
        " 200 is end of searched timeframe
        """

        if self.end is None:  # it is empty period in the end of list of events
            return 0

        if self.start[2] == self.end[2]:  # some event was missed from db, so we can't calculate correct outage time
            # it is not right way to calculate, but there is no other way since
            # we calculate not for the concrete customer but for all within a certain period of time
            return 0

        if self.start[2] == 100:  # when start of period =  start of searched frame
            if self.end[2] == 0:  # if outage finished event
                outage = datetime.fromtimestamp(self.end[1]) - datetime.fromtimestamp(self.start[1])
                return outage.seconds
            else:  # self.end[2] == 1
                return 0

        if self.end[2] == 200:  # when end of period =  end of searched frame
            if self.start[2] == 0:
                return 0
            else:
                outage = datetime.fromtimestamp(self.end[1]) - datetime.fromtimestamp(self.start[1])
                return outage.seconds

        if self.start[2] == 0 and self.end[2] == 1:  # not outage period
            return 0

        if self.start[2] == 1 and self.end[2] == 0:  # outage period
            outage = datetime.fromtimestamp(self.end[1]) - datetime.fromtimestamp(self.start[1])
            return outage.seconds

    def __repr__(self):
        return "Period({}, {} = {})".format(self.start, self.end, self.calculate_period_length())

    def __str__(self):
        return "Period({}, {} = {})".format(self.start, self.end, self.calculate_period_length())


def preparation(customer_name='787513', delta=0, start_event=1, end_event=0) -> Period:
    p = Period()
    p.set_start((customer_name, 1574017545, start_event))
    p.set_end((customer_name, 1574017545+delta, end_event))
    return p


def support_func():
    user_id = '787513'
    p = Period()
    p.set_start((user_id, 1574017545, 0))
    p.set_end((user_id, 1574017545 + 910, 0))
    print(p.calculate_period_length())

    p = preparation(delta=-600)
    print(p, p.calculate_period_length())



    available_values = [2, 3, 300, 400, -1, -200]
    p = Period()
    for i in available_values:
        for j in available_values:
            p.set_start(('787513', 1574017545, i))
            p.set_end(('787513', 1574017545 + 200, j))
            print(p.calculate_period_length())


def main():
    p = Period()
    p = preparation(delta=20, start_event=200, end_event=100)
    print(p.calculate_period_length(), p)



if __name__ == '__main__':
    main()
