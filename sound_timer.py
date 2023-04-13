import winsound
import time

# Get the sound file and duration from the user
# Ses dosyasını ve süresini kullanıcıdan alın
sound_file = input("Enter the path to the sound file: ").replace('"', '')  # remove extra quotes #fazladan alıntıları kaldır
duration = int(input("Enter the duration in seconds: "))

# Keep playing the sound file indefinitely
# Ses dosyasını süresiz olarak çalmaya devam edin
while True:
    # Load the sound file and play it for the specified duration
    # Ses dosyasını yükleyin ve belirtilen süre boyunca çalın
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    time.sleep(duration)



# The time you specify for the pause interval includes the duration of the audio file and I recommend running the program in debug
# Bekleme aralığı için belirttiğiniz süreye ses dosyasının süresi dahildir ve programı hata ayıklamada çalıştırmanı tavsiye ederim






















