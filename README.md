 # 📡 Smart Attendance System with RFID & IoT

![IoT Attendance Banner](https://img.shields.io/badge/IoT-Smart_Attendance-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## Kelompok 10
- **BAMBANG ISTIJAB - 105222007**
- **ATHIRAH RASHIDA NAIMA - 105222027**

## 📘 Deskripsi Proyek

Proyek ini merupakan sistem absensi otomatis berbasis **RFID** dan **Internet of Things (IoT)** menggunakan **ESP32**, yang dirancang untuk meningkatkan efisiensi dan transparansi dalam pencatatan kehadiran siswa di lingkungan pendidikan.

Sistem ini mendukung **SDG 4: Quality Education**, dengan mengirimkan data kehadiran secara otomatis ke **Google Sheets** atau **Firebase** menggunakan koneksi Wi-Fi dan platform seperti **IFTTT**.

## 🎯 Tujuan

> **Siswa scan RFID → data hadir dikirim otomatis ke cloud (Google Sheets atau Firebase).**

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
   - **Google Sheets**

## 🧰 Tools

- **Arduino IDE** untuk pemrograman ESP32
- **Google Sheets** untuk tampilan data

## 📊 Smart Attendance System Diagram
![Smart Attendance Diagram](https://i.imgur.com/4zMSOno.png)

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
Data kehadiran (UID, timestamp) disimpan di Google Sheets 
6. **User Interface**: Data yang tersimpan dapat diakses dan divisualisasikan melalui dashboard web, aplikasi mobile, atau laporan yang dibuat dari Google Sheets, memungkinkan guru atau administrator memantau kehadiran siswa secara real-time atau melihat riwayat.
![Smart Attendance Blok Diagram system](https://i.imgur.com/Tqk1CP3.png)






