import urequests
import ujson
from machine import Pin
from mfrc522 import MFRC522
import time
import network

# Koneksi WiFi
ssid = 'hihihihi'
password = 'bams987654321'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass  # Tunggu koneksi WiFi
print("WiFi Connected:", sta_if.ifconfig())

# Inisialisasi RFID dan buzzer
rdr = MFRC522(sck=18, mosi=23, miso=19, rst=4, cs=5)
buzzer = Pin(15, Pin.OUT)
buzzer.off()

# Dictionary UID ke Nama
daftar_nama = {
    '4328ad30f6': 'Athirah.R.N',
    '535b7a0577': 'Bambang Istijab',
    'd493babf42': 'Akiwra',
    'e4fabbbf1a': 'algip',
    'd3883a9afb': 'banana',
    '09f1a90051': 'mas jawa'
}

print("Letakkan kartu RFID di dekat reader...")

try:
    while True:
        (status, tag_type) = rdr.request(rdr.REQIDL)
        if status == rdr.OK:
            (status, uid) = rdr.anticoll()
            if status == rdr.OK:
                uid_str = ''.join('{:02x}'.format(i) for i in uid)
                nama = daftar_nama.get(uid_str, "Tidak Dikenal")

                # ✅ Tambahan print UID
                print("UID Kartu Terdeteksi:", uid_str, "| Nama:", nama)

                # Nyalakan buzzer
                buzzer.on()
                time.sleep(0.3)
                buzzer.off()

                # Kirim data ke Google Sheet
                url = "http://192.168.138.83:5050/absen"
#                 url = "http://http://127.0.0.1:5500/absen"
                headers = {"Content-Type": "application/json"}
                payload = {
                    "uid": uid_str,
                    "nama": nama
                }

                try:
                    response = urequests.post(url, headers=headers, data=ujson.dumps(payload))
                    print("✅ Dikirim ke Sheet:", payload, "| Respon:", response.text)
                    response.close()
                except Exception as e:
                    print("⚠️ Gagal mengirim:", e)

                time.sleep(1.5)  # Hindari double scan
except KeyboardInterrupt:
    print("Berhenti oleh pengguna")

