from internetspeed import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10

internetspeed = InternetSpeedTwitterBot()

internetspeed.get_internet_speed()
print(f"My download speed is at {internetspeed.down}mbps and my upload speed is at {internetspeed.up}mbps.")

if internetspeed.down < PROMISED_DOWN or internetspeed.up < PROMISED_UP:
    internetspeed.tweet_at_provider()
