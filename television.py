class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 0
    MAX_CHANNEL = 99

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status
        if self.__status:
            print("The TV is now ON.")
        else:
            print("The TV is now OFF.")

    def mute(self):
        self.__muted = not self.__muted
        if self.__muted:
            print("The TV is now muted.")
        else:
            print("The TV is now unmuted.")

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)
            print(f"Channel increased to {self.__channel}.")

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)
            print(f"Channel decreased to {self.__channel}.")

    def volume_up(self):
        if self.__status and not self.__muted and self.__volume < self.MAX_VOLUME:
            self.__volume += 1
            print(f"Volume increased to {self.__volume}.")

    def volume_down(self):
        if self.__status and not self.__muted and self.__volume > self.MIN_VOLUME:
            self.__volume -= 1
            print(f"Volume decreased to {self.__volume}.")

    def __str__(self):
        return f"TV Status: {'ON' if self.__status else 'OFF'}\nChannel: {self.__channel}\nVolume: {self.__volume}\nMuted: {'Yes' if self.__muted else 'No'}"

my_tv = Television()
print(my_tv)
my_tv.power()
my_tv.channel_up()
my_tv.volume_up()
my_tv.mute()
print(my_tv)