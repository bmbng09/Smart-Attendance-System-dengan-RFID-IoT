 # 📡 Smart Attendance System with RFID & IoT

![IoT Attendance Banner](https://img.shields.io/badge/IoT-Smart_Attendance-blue?style=flat-square)

## Kelompok 10
- **`BAMBANG ISTIJAB - 105222007`**
- **`ATHIRAH RASHIDA NAIMA - 105222027`**

## 📘 Deskripsi Proyek

Proyek ini merupakan sistem absensi otomatis berbasis **RFID** dan **Internet of Things (IoT)** menggunakan **ESP32**, yang dirancang untuk meningkatkan efisiensi dan transparansi dalam pencatatan kehadiran siswa di lingkungan pendidikan.

Sistem ini mendukung **SDG 4: Quality Education**, dengan mengirimkan data kehadiran secara otomatis ke **Google Sheets**  menggunakan koneksi Wi-Fi dan platform seperti **IFTTT**.

## 🎯 Tujuan

> **Siswa scan RFID → data hadir dikirim otomatis ke mysql + website.**

Dengan sistem ini, guru tidak perlu lagi mencatat kehadiran secara manual, dan data dapat diakses secara real-time dari mana saja.

## 🛠️ Komponen Perangkat Keras

| Komponen       | Fungsi                                        |
|----------------|-----------------------------------------------|
| ESP32          | Mikrokontroler dengan koneksi Wi-Fi           |
| RFID RC522     | Modul pembaca kartu RFID                      |
| Kartu RFID     | Media identifikasi siswa                      |
| Buzzer         | Memberikan notifikasi bunyi saat absensi      |
| Breadboard     | Perakitan prototipe awal                      |
| Kabel Jumper   | Koneksi antar-komponen                        |

## 🧠 Arsitektur Sistem

1. Siswa menempelkan kartu RFID ke RC522.
2. ESP32 membaca UID dari kartu.
3. Buzzer berbunyi sebagai konfirmasi.
4. Data UID + Timestamp dikirim ke:
   - **Mysql**

## 🧰 Tools

- **Thony** untuk pemrograman ESP32
- **Website + mysql** untuk tampilan data


## 📊 Diagram Blok System
**Penjelasan Alur Kerja:**
1. **RFID Card & RFID RC522**: Siswa memindai kartu RFID mereka ke modul RFID RC522. Modul ini membaca UID (Unique ID) dari kartu.
2. **ESP32 Microcontroller**:
 - Menerima data UID dari RFID RC522 melalui komunikasi SPI.
 - Memproses UID tersebut.
 - Mengaktifkan Buzzer untuk memberikan feedback audio (misalnya, bunyi "beep" setelah pemindaian berhasil).
 - Menggunakan modul Wi-Fi internalnya untuk terhubung ke internet.
 - Mengirimkan data UID dan timestamp ke Cloud Platform yang dipilih 
3. **Buzzer**: Memberikan sinyal suara kepada siswa bahwa pemindaian telah terdeteksi atau memberikan indikasi error.
4. **Cloud Platform**:
 - IFTTT Webhook: Berfungsi sebagai jembatan. ESP32 mengirimkan data ke webhook IFTTT, yang kemudian memicu aksi untuk menambahkan data ke Google Sheets.
5. **Data Storage**:
Data kehadiran (UID, timestamp) disimpan dimysql
6. **User Interface**: Data yang tersimpan dapat diakses dan divisualisasikan melalui dashboard web, aplikasi mobile, atau laporan yang dibuat dari Google Sheets, memungkinkan guru atau administrator memantau kehadiran siswa secara real-time atau melihat riwayat.
![Image](https://github.com/user-attachments/assets/5bd8a331-3b2e-4ef0-87a1-eef6e6c4bf0a)

## 📊 Desain sistem hardware dan software
**I. Lapisan Hardware (Komponen Fisik)**
1. Input Fisik:
* RFID Card (Kartu Siswa): Media identifikasi fisik siswa.
* RFID RC522 Reader: Modul untuk membaca data dari kartu RFID.
* Koneksi ke ESP32: Melalui protokol SPI (Serial Peripheral Interface).
* `RC522 VCC` -> `ESP32 3.3V`
* `RC522 RST (GPIO 04)` -> `ESP32 GPIO 04`
* `RC522 GND` -> `ESP32 GND`
* `RC522 MISO (GPIO 19)` -> `ESP32 GPIO 19`
* `RC522 MOSI (GPIO 23)` -> `ESP32 GPIO 23`
* `RC522 SCK (GPIO 18)` -> `ESP32 GPIO 18`
* `RC522 SDA (SS) (GPIO 05)` -> `ESP32 GPIO 05`

2. Unit Pemrosesan:
* ESP32 Development Board: Mikrokontroler utama yang menjalankan logika sistem.
* Kemampuan: Pemrosesan data, konektivitas Wi-Fi, kontrol I/O.

3. Output Fisik / Feedback:
* Buzzer: Memberikan indikasi suara (beep) sebagai feedback kepada pengguna.
* Koneksi ke ESP32: Melalui pin GPIO digital.
* `Buzzer Positif` (+) -> `ESP32 GPIO 15`
* `Buzzer Negatif` (-) -> `ESP32 GND`

II. Lapisan Software (MicroPython di ESP32)
1. Firmware Dasar:
* MicroPython OS: Sistem operasi yang berjalan di ESP32, memungkinkan pemrograman dengan Python.

2. Modul/Library Python:
* `mfrc522.py`: Modul khusus yang berisi driver untuk berkomunikasi dengan hardware RFID RC522 (membaca UID, autentikasi, read/write blok data).
* `urequests.py`: Modul khusus yang berisi driver untuk menyediakan fungsi-fungsi dasar untuk berinteraksi dengan server web menggunakan protokol HTTP (dan HTTPS)
* `boot.py`: File Python yang dieksekusi saat ESP32 pertama kali booting. Bertanggung jawab untuk inisialisasi koneksi Wi-Fi.
* `main.py`: File Python utama yang berisi logika inti aplikasi:
* Membaca UID dari kartu RFID.
* Membunyikan buzzer untuk feedback.
* Mengambil timestamp.
* Memformat data kehadiran.
* Mengirim data kehadiran (UID & timestamp) ke cloud platform.
* (Opsional: menulis/membaca data lain ke blok kartu RFID).
* Library Standar MicroPython: `machine`, `network`, `time`, `urequests`, `os` (digunakan secara internal).

III. Lapisan Konektivitas
1. Jaringan Nirkabel:
* Wi-Fi: ESP32 terhubung ke jaringan Wi-Fi (2.4GHz) untuk mengakses internet.
* (Bisa hotspot ponsel atau Wi-Fi standar).

2. Protokol Komunikasi:
* HTTP/HTTPS: Digunakan oleh ESP32 (`urequests`) untuk mengirim data ke mysql

IV. Lapisan Cloud (Backend & Data Storage)
MySQL + CSV

Database Sederhana: Menyimpan data kehadiran dalam format tabel (kolom contoh: `UID_Kartu`, `Timestamp`, `Nama_Siswa`, `Status`).

V. Lapisan User Interface (UI) / User Experience (UX)
1. UI/UX di Hardware (On-Device Feedback):

- RFID Card:
UI: Kartu fisik sebagai identitas siswa.
UX: Mudah dibawa, cepat untuk dipindai.
- RFID RC522 Reader:
UI: Bagian fisik perangkat tempat siswa menempelkan kartu.
UX: Titik interaksi yang jelas, cukup tempelkan kartu.
- Buzzer:
UI: Perangkat audio yang terintegrasi.
UX: Memberikan feedback langsung dan instan kepada siswa:
Beep Pendek (100ms): Indikasi pemindaian berhasil / kehadiran tercatat.
Beep Panjang (500ms): Indikasi pemindaian gagal / error.

2. UI/UX di Software (Monitoring & Management Dashboard):

UI: Antarmuka spreadsheet standar Google Sheets.
Kolom data (UID, Timestamp, dll.).
Fitur filter, sort, dan pencarian bawaan.
Grafik dasar dan pivot table untuk analisis tren kehadiran.
UX: Akses mudah dari browser web, cocok untuk data sederhana. Analisis dan pelaporan mungkin sedikit manual namun fleksibel.

VI. Alur Kerja (End-to-End System Flow)
- Siswa Datang: Siswa menempelkan kartu RFID mereka ke RFID RC522 Reader.
- Deteksi & Pembacaan: RFID RC522 membaca UID dari kartu dan mengirimkannya ke ESP32.
- Pemrosesan Lokal (ESP32):
1. ESP32 menerima UID.
2. Buzzer berbunyi (misalnya, beep pendek) sebagai konfirmasi.
3. ESP32 mendapatkan timestamp saat ini.
4. ESP32 menggunakan Wi-Fi untuk terhubung ke internet (melalui `boot.py`).
- Pengiriman Data ke Mysql:
ESP32 mengirimkan UID dan timestamp melalui HTTP/HTTPS ke Mysql
- Penyimpanan Data:
Data kehadiran disimpan secara otomatis di Mysql.
- Monitoring & Pelaporan (UI/UX):
Guru, administrator, atau orang tua dapat melihat data kehadiran secara real-time atau mengakses laporan historis melalui antarmuka Google Sheets atau Aplikasi Web/Mobile khusus.

### Rencangan desain web dan spreadsheet
#### Hardware
![desain sistem hardware](https://i.imgur.com/mPjRDlp.jpeg)

#### Hardware:
![Image](https://github.com/user-attachments/assets/bd543d9a-a748-4626-b7a7-7f0be503f7f3)

#### Software
![Image](https://github.com/user-attachments/assets/5bdc5e5a-b843-4369-bac9-f8235a9d2f32)

#### Video Hardware, Software dan Demonstrasi 
[Link Drive](https://drive.google.com/file/d/19QR1zLRKZMFA8OdgfEH3-hyOMejASxhr/view?usp=drive_link)








