 # 📡 Smart Attendance System with RFID & IoT

![IoT Attendance Banner](https://img.shields.io/badge/IoT-Smart_Attendance-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

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

## Skema
![Smart Attendance Diagram](https://imgur.com/4zMSOno)





