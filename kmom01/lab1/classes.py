""" classes for lab1 """

class Cat:
    """ Cat class for lab1 """

    nr_of_paws = 4

    def __init__(self, eye_color, name):
        """ constructor for cat object """
        self.eye_color = eye_color
        self.name = name
        self._lives_left = -1

    def get_lives_left(self):
        """ getter for lives left """
        return self._lives_left

    def set_lives_left(self, lives_left):
        """ setter for lives left """
        self._lives_left = lives_left

    def description(self):
        """ Describe a cat object """
        return (
                f"My cat's name is {self.name}, has {self.eye_color} eyes "
                f"and {self.get_lives_left()} lives left to live."
                )

class Duration:
    """ Duration class for lab1 """

    def __init__(self, hours, minutes, seconds):
        """ duration constructor """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        """ format duration to hh-mm-ss """
        hours = str(self.hours) if self.hours >= 10 else "0" + str(self.hours)
        minutes = str(self.minutes) if self.minutes >= 10 else "0" + str(self.minutes)
        seconds = str(self.seconds) if self.seconds >= 10 else "0" + str(self.seconds)
        return hours + "-" + minutes + "-" + seconds

    @staticmethod
    def duration_to_sec(formatted_duration):
        """ convert duration format to seconds """
        duration_list = formatted_duration.split("-")
        hours_in_sec = int(duration_list[0]) * 60 * 60
        minutes_in_sec = int(duration_list[1]) * 60
        seconds = int(duration_list[2])

        return seconds + minutes_in_sec + hours_in_sec

    def __add__(self, other):
        """ overwrite + operator for durations """
        return self.duration_to_sec(self.display()) + self.duration_to_sec(other.display())

    def __iadd__(self, other):
        """ overwrite += operator for durations """
        # initial addition
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

        # add extra seconds (> 59) to minutes
        self.minutes += self.seconds // 60
        self.seconds %= 60

        # add extra minutes (> 59) to hours
        self.hours += self.minutes // 60
        self.minutes %= 60

        return self

    def __lt__(self, other):
        """ overwrite < operator for durations """
        return self.duration_to_sec(self.display()) < other.duration_to_sec(other.display())
