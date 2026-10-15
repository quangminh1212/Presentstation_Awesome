# BUKANG PPTX Generator

Otomatisasi pengisian template PowerPoint (PPTX) Buku Angkatan dari template PDF Canva dan database Supabase / CSV.

## Struktur Direktori

```
bukang-pptx-generator/
├── database/
│   ├── mahasiswa_tc25_all.csv   # Data CSV mahasiswa
│   ├── sample_mahasiswa.csv     # Sample CSV data
│   └── Teknis Buku Angkatan...  # CSV per kelas
├── templates/
│   ├── template_bukang.pdf      # Template asli Canva
│   └── page3_clean_bg.png       # Background template bersih (hasil render)
├── .cache_photos/               # Cache foto lokal (auto-download dari Supabase)
├── output/                      # Folder output PPTX yang digenerate
├── .env.example                 # Contoh konfigurasi Supabase
├── generate.py                  # Script generator utama
├── requirements.txt             # Dependensi Python
└── README.md
```

## Fitur Utama

1. **Pixel-Perfect Canva Background**: Template PDF Canva dirender menjadi background beresolusi tinggi tanpa placeholder teks atau gambar.
2. **Proporsional / Anti-Gepeng**: Dimensi asli foto dipertahankan dengan kalkulasi aspect ratio dinamis dan dibungkus frame border hijau yang rapi.
3. **In-Memory Random First Impression**: Nilai first impression dipilih secara acak dari list pilihan (`keren`, `baik`, `jago`, `ramah`) saat pembuatan PPTX tanpa memodifikasi isi database.
4. **Auto-Resume & Checkpoint**: PPTX disimpan otomatis setelah setiap slide dibuat. Jika proses dihentikan (`Ctrl+C`), script dapat dijalankan kembali dan akan melanjutkan dari mahasiswa yang tersisa tanpa mengulang dari awal.
5. **Photo Caching**: Foto yang diunduh dari Supabase Storage otomatis disimpan di folder cache lokal (`.cache_photos/`) untuk menghindari pengunduhan ulang.
6. **Filter Default**: Secara default hanya memproses mahasiswa yang sudah memiliki status foto (`sudah_difoto = True`).

## Setup & Instalasi

### 1. Buat Virtual Environment dengan `uv`

```bash
uv venv --python /usr/bin/python3.12
source .venv/bin/activate
```

### 2. Install Dependensi

```bash
uv pip install -r requirements.txt
```

### 3. Konfigurasi Kredensial Supabase

Salin `.env.example` ke `.env` dan isi kredensial project:

```bash
cp .env.example .env
```

Isi `.env`:
```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-service-role-or-anon-key
SUPABASE_BUCKET=foto-angkatan
```

## Penggunaan

### 1. Generate dari Supabase (Default)

Menghasilkan PPTX untuk semua mahasiswa yang sudah difoto:
```bash
python generate.py
```

### 2. Generate per Kelas Tertentu

```bash
python generate.py --kelas A
```

### 3. Generate dari Data CSV Lokal

```bash
python generate.py --source csv
```

### 4. Testing (Batasi Jumlah Mahasiswa)

```bash
python generate.py --limit 10
```

### 5. Mulai Ulang dari Nol (Fresh Rebuild)

Jika ingin membuat ulang PPTX tanpa melanjutkan checkpoint sebelumnya:
```bash
python generate.py --fresh
```

### 6. Sertakan Mahasiswa yang Belum Difoto

```bash
python generate.py --all
```

