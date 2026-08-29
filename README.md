# Lahanay — Landing Page Madu Klanceng

Landing page jualan madu klanceng/meliponin, siap hosting gratis di
**GitHub + Cloudflare Pages**, dengan folder `/artikel/` untuk konten
SEO yang diisi rutin.

---

## Struktur folder

```
lahanay/
├── index.html              ← landing page utama
├── sitemap.py               ← generate sitemap.xml + robots.txt
├── artikel/
│   ├── index.html            ← daftar semua artikel
│   └── template-artikel.html ← duplikat file ini tiap bikin artikel baru
├── assets/
│   └── css/style.css         ← semua styling (dipakai semua halaman)
└── images/                  ← taruh semua foto produk di sini
    └── artikel/               ← gambar khusus untuk artikel
```

---

## Setup awal (sekali saja)

### 1. Isi konten dulu

Sebelum push, ganti semua teks yang ditandai `[ ]` (kurung siku) di:

- `index.html` — harga produk, testimoni, lokasi
- `artikel/index.html` dan `artikel/template-artikel.html` — placeholder tanggal/lokasi

Masukkan foto produk ke folder `images/`. Nama file bebas, tinggal update
`src="images/nama-file.jpg"` di HTML-nya.

### 2. Push ke GitHub

```bash
cd lahanay
git init
git add .
git commit -m "initial commit — landing page lahanay"
git branch -M main
git remote add origin https://github.com/USERNAME/lahanay.git
git push -u origin main
```

> Sama seperti Bacaan Terpilih: push pakai **Personal Access Token (PAT)**,
> bukan password akun biasa. Kalau token untuk repo Bacaan Terpilih masih
> aktif dan scope-nya mencakup repo baru, token yang sama bisa dipakai lagi
> — tidak perlu bikin token baru tiap repo.

### 3. Connect ke Cloudflare Pages

1. Buka [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. Pilih repo `lahanay`
3. Build settings: kosongkan semua (ini situs statis, tidak perlu build command / framework preset — pilih "None")
4. **Penting soal nama domain:** Cloudflare otomatis membuat subdomain dari
   **nama project** yang kamu ketik saat setup (bukan dari nama repo).
   Supaya jadi `lahanay.pages.dev`, ketik nama project persis `lahanay`.
   Nama ini rebutan sesama pengguna Cloudflare secara global — kalau sudah
   dipakai orang lain, kamu perlu variasi lain (mis. `lahanaymadu`).
5. Deploy. Setiap `git push` berikutnya otomatis re-deploy.

---

## Workflow tambah artikel baru (rutin)

1. **Duplikat** `artikel/template-artikel.html`, ganti nama file sesuai judul,
   misalnya `artikel/manfaat-madu-klanceng.html`
2. **Isi konten** — ganti semua `[teks dalam kurung siku]`, termasuk:
   - `<title>`, meta description, canonical URL (samakan dengan nama file)
   - Judul, kategori, tanggal
   - Isi artikel di `<div class="article-body">`
3. **Tambahkan link** artikel baru di `artikel/index.html` — copy satu blok
   `<a class="article-list-item">`, taruh paling atas (artikel terbaru duluan),
   isi judul/ringkasan/tanggal, dan ganti `href` ke file artikel barunya
4. **Jalankan sitemap.py**:
   ```bash
   python sitemap.py
   ```
5. **Push ke GitHub**:
   ```bash
   git add .
   git commit -m "tambah artikel: [judul artikel]"
   git push
   ```
   Cloudflare otomatis re-deploy dalam 1-2 menit.

---

## Tips SEO & biar disukai AI search (ChatGPT, Perplexity, dll.)

- Paragraf pembuka tiap artikel harus langsung menjawab pertanyaan utama —
  AI search sering mengambil 2-3 kalimat pertama sebagai ringkasan.
- Satu artikel = satu topik jelas. Jangan campur banyak topik dalam satu halaman.
- Judul artikel sebaiknya berupa pertanyaan atau frasa yang orang benar-benar
  ketik di Google (mis. "Cara Membedakan Madu Klanceng Asli dan Palsu", bukan
  "Tips Seputar Madu").
- Isi `alt` di setiap `<img>` dengan deskripsi jelas, bukan nama file.
- Konsisten publish — 1-2 artikel per minggu lebih baik untuk SEO jangka
  panjang daripada 10 artikel sekaligus lalu berhenti.

---

## Catatan teknis

- Semua styling ada di satu file (`assets/css/style.css`) supaya konsisten
  di semua halaman — kalau ganti warna/font, cukup edit di satu tempat
  (bagian `:root` paling atas file).
- Tombol WhatsApp pakai format `https://wa.me/6289621566266?text=...` —
  kalau mau ganti pesan default, edit teks setelah `?text=` (harus di-encode
  URL, spasi jadi `%20`).
- Disclaimer kesehatan di footer sengaja dipertahankan — hindari klaim medis
  berlebihan ("menyembuhkan", "obat kanker", dll.) di isi artikel maupun
  landing page, karena berisiko kena tegur platform iklan/marketplace.
