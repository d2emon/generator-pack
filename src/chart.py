import math
import random


class MediaItem():
    def __init__(self, name="Unnamed", openweekend=1000000):
        self.name = name
        self.openweekend = openweekend
        self.weeks = [0, openweekend]

    def random_weekend(self, t=1):
        if t < 1:
            return 0
        box = self.openweekend * math.pow(t, -3 / 4)
        adjust = random.randint(50, 150) / 100
        # print(box, box * adjust)
        return int(box * adjust)

    def weekend(self, t=1):
        if t < 1:
            return 0
        if len(self.weeks) > t:
            return self.weeks[t]
        for w in range(len(self.weeks), t+1):
            weekend = self.random_weekend(w)
            self.weeks.append(weekend)
            # print(w, weekend, self.weeks[w])
        return self.weeks[t]

    def total(self, t=1):
        total = 0
        for w in range(0, t + 1):
            weekend = self.weekend(w)
            total += weekend
            # print(w, weekend, total)
        return total

    def weeks_in_chart(self):
        return len(self.weeks) - 1

    def last_week(self):
        return self.weeks[-1]

    def next_week(self):
        return self.weekend(self.weeks_in_chart() + 1)
