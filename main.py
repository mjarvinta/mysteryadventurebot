import time
import random

class MysteryAdventureBot:
    def __init__(self, nama_pemain):
        self.nama_pemain = nama_pemain
        self.poin = 0
        self.nyawa = 100
        self.teka_teki_selesai = []
        self.petunjuk = []
        self.penculik_asli = "Igor Molodov"
        self.lokasi_terakhir = "Gudang di Tepi Kota"
        
    def tampilkan_intro(self):
        """Menampilkan intro cerita"""
        print("\n" + "="*60)
        print("MYSTERY ADVENTURE BOT: KASUS MENGHILANGNYA WALIKOTA")
        print("="*60)
        print(f"\nSelamat datang, {self.nama_pemain}!")
        print("\nTanggal: 15 November 2024")
        print("Tempat: Kota Maharaja - sebuah kota yang ramai")
        print("\n[CERITA]")
        time.sleep(1)
        print("˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰˰")
        print("\nWalikota Kota Maharaja, Bapak Hartono Wijaya, telah menghilang!")
        time.sleep(1)
        print("\nSebelum hilangnya, dia meninggalkan catatan aneh di meja kerjanya.")
        time.sleep(1)
        print("Polisi lokal minta bantuanmu untuk menyelidiki kasus ini.")
        time.sleep(1)
        print("\nMisimu: Pecahkan teka-teki, temukan petunjuk, dan ungkap sang penculik!")
        print("\n" + "="*60)        
        print(f"\n⚕️  NYAWA AWAL: {self.nyawa}")
        print("⚠️  Setiap jawaban salah mengurangi 30 nyawa!")
        print("="*60)
        
    def tampilkan_status(self):
        """Menampilkan status nyawa dan poin saat ini"""
        status = f"💚 Nyawa: {self.nyawa} | ⭐ Poin: {self.poin}"
        print(f"\n{status}")
        return self.nyawa > 0
    
    def game_over(self):
        """Menampilkan pesan game over"""
        print("\n" + "="*60)
        print("GAME OVER - NYAWA HABIS!")
        print("="*60)
        print(f"\nInvestigator {self.nama_pemain} tidak mampu menyelesaikan kasus ini.")
        print(f"Poin akhir: {self.poin}")
        print(f"Petunjuk yang dikumpulkan: {len(self.petunjuk)}/{len(self.teka_teki_selesai)}")
        print("\nWalikota tidak dapat diselamatkan... 😢")
        print("="*60 + "\n")
        return False        
    def tebak_lokasi(self):
        """Mini-game tebak lokasi walikota terakhir dilihat"""
        print("\n[TEKA-TEKI 1: TEBAK LOKASI PERTAMA]")
        print("━" * 50)
        print("\nPolisi menemukan catatan: 'Saya terakhir bertemu dengannya di...'")
        print("Tiga orang bersaksi melihat walikota di lokasi berbeda:")
        
        lokasi_opsi = {
            "1": {"nama": "Kantor Pemerintah", "benar": False},
            "2": {"nama": "Restoran Mewah 'Golden Dragon'", "benar": False},
            "3": {"nama": "Bank Kota Maharaja", "benar": True}
        }
        
        print("\nPilihan lokasi:")
        for kunci, nilai in lokasi_opsi.items():
            print(f"{kunci}. {nilai['nama']}")
        
        guess = input("\nJawaban Anda (1/2/3): ").strip()
        
        if guess in lokasi_opsi:
            if lokasi_opsi[guess]["benar"]:
                print(f"\n✓ BENAR! Walikota terakhir dilihat di {lokasi_opsi[guess]['nama']}")
                print("Petunjuk ditemukan: Tas hitam kosong di Bank")
                self.poin += 10
                self.petunjuk.append("Tas hitam kosong di Bank")
                self.teka_teki_selesai.append("Lokasi")
                self.tampilkan_status()
                return True
            else:
                print(f"\n✗ SALAH! Orang itu berbohong.")
                print(f"Jawaban yang benar adalah: {lokasi_opsi['3']['nama']}")
                print("\n⚠️  PERINGATAN: Kesalahan investigasi! Walikota semakin jauh dari jangkauan.")
                self.nyawa -= 30
                print(f"❌ Nyawa berkurang 30 poin! Nyawa sisa: {self.nyawa}")
                self.tampilkan_status()
                return False
        else:
            print("\nPilihan tidak valid!")
            return False
    
    def tebak_penjahat(self):
        """Mini-game tebak siapa penculiknya"""
        print("\n[TEKA-TEKI 2: TEBAK SIAPA PENCULIKNYA]")
        print("━" * 50)
        print("\nAnda menemukan 3 orang yang mencurigakan di sekitar lokasi kejadian:")
        
        penjahat_opsi = {
            "1": {"nama": "Igor Molodov", "profesi": "Pesaing bisnis dari Rusia", "benar": True},
            "2": {"nama": "Siti Rahayu", "profesi": "Asisten pribadi Walikota", "benar": False},
            "3": {"nama": "Budi Santoso", "profesi": "Anggota dewan kota", "benar": False}
        }
        
        for kunci, nilai in penjahat_opsi.items():
            print(f"\n{kunci}. {nilai['nama']}")
            print(f"   Profesi: {nilai['profesi']}")
        
        guess = input("\nSiapa yang Anda curigai? (1/2/3): ").strip()
        
        if guess in penjahat_opsi:
            if penjahat_opsi[guess]["benar"]:
                print(f"\n✓ BENAR! {penjahat_opsi[guess]['nama']} adalah penculik!")
                print("Dia ingin mengambil alih kontrak proyek senilai triliunan rupiah")
                self.poin += 15
                self.petunjuk.append("Igor Molodov adalah penculik")
                self.teka_teki_selesai.append("Penjahat")
                self.tampilkan_status()
                return True
            else:
                print(f"\n✗ SALAH! {penjahat_opsi[guess]['nama']} tidak bersalah.")
                print(f"Jawaban yang benar adalah: {penjahat_opsi['1']['nama']}")
                print("\n⚠️  PERINGATAN: Anda menuduh orang yang salah! Ini merusak reputasi investigasi.")
                self.nyawa -= 30
                print(f"❌ Nyawa berkurang 30 poin! Nyawa sisa: {self.nyawa}")
                self.tampilkan_status()
                return False
        else:
            print("\nPilihan tidak valid!")
            return False
    
    def tebak_motif(self):
        """Mini-game tebak motif penculikan"""
        print("\n[TEKA-TEKI 3: TEBAK MOTIF PENCULIKAN]")
        print("━" * 50)
        print("\nAnda menemukan surat dari penculik. Apa motivnya menculik walikota?")
        
        motif_opsi = {
            "1": "Balas dendam pribadi karena ditolak usahanya",
            "2": "Ingin mengambil alih proyek infrastruktur senilai 50 triliun",
            "3": "Perintah dari organisasi kriminal internasional"
        }
        
        jawaban_benar = "2"
        
        for kunci, nilai in motif_opsi.items():
            print(f"{kunci}. {nilai}")
        
        guess = input("\nMotif apa menurut Anda? (1/2/3): ").strip()
        
        if guess == jawaban_benar:
            print("\n✓ BENAR! Igor mencuri walikota untuk memaksa penandatanganan kontrak!")
            self.poin += 12
            self.petunjuk.append("Motif: Proyek infrastruktur senilai 50 triliun")
            self.teka_teki_selesai.append("Motif")
            self.tampilkan_status()
            return True
        else:
            print("\n✗ SALAH! Motivnya lebih rumit dari itu.")
            print("Jawaban yang benar: Ingin mengambil alih proyek infrastruktur senilai 50 triliun")
            print("\n⚠️  PERINGATAN: Memahami motif penjahat sangat penting! Pertahankan fokus Anda!")
            self.nyawa -= 30
            print(f"❌ Nyawa berkurang 30 poin! Nyawa sisa: {self.nyawa}")
            self.tampilkan_status()
            return False
    
    def tebak_barang_bukti(self):
        """Mini-game tebak barang bukti kunci"""
        print("\n[TEKA-TEKI 4: TEBAK BARANG BUKTI KUNCI]")
        print("━" * 50)
        print("\nDi rumah Igor Molodov, polisi menemukan berbagai barang.")
        print("Mana yang merupakan bukti langsung penculikan?")
        
        barang_opsi = {
            "1": "Cincin emas walikota dengan inisial HW",
            "2": "Resep dokter untuk kolesterol tinggi",
            "3": "Foto liburan keluarga di pantai"
        }
        
        jawaban_benar = "1"
        
        for kunci, nilai in barang_opsi.items():
            print(f"{kunci}. {nilai}")
        
        guess = input("\nBarang bukti apa? (1/2/3): ").strip()
        
        if guess == jawaban_benar:
            print("\n✓ BENAR! Cincin dengan inisial HW adalah barang walikota!")
            print("Ini membuktikan bahwa Igor memiliki walikota.")
            self.poin += 10
            self.petunjuk.append("Cincin HW ditemukan di rumah Igor")
            self.teka_teki_selesai.append("Bukti")
            self.tampilkan_status()
            return True
        else:
            print("\n✗ SALAH! Barang itu bukan bukti yang relevan.")
            print("Jawaban yang benar: Cincin emas walikota dengan inisial HW")
            print("\n⚠️  PERINGATAN: Bukti fisik sangat krusial! Jangan asal-asalan dalam memilih!")
            self.nyawa -= 30
            print(f"❌ Nyawa berkurang 30 poin! Nyawa sisa: {self.nyawa}")
            self.tampilkan_status()
            return False
    
    def tebak_lokasi_penculikan(self):
        """Mini-game tebak di mana walikota ditahan"""
        print("\n[TEKA-TEKI 5: TEBAK LOKASI PENAHANAN WALIKOTA]")
        print("━" * 50)
        print("\nBerdasarkan petunjuk yang ada, di mana Igor menyembunyikan walikota?")
        print("\nPetunjuk yang ditemukan:")
        for i, petunjuk in enumerate(self.petunjuk, 1):
            print(f"  • {petunjuk}")
        
        lokasi_penahan_opsi = {
            "1": "Apartemen mewah di pusat kota",
            "2": "Gudang tua di tepi kota yang sudah tidak terpakai",
            "3": "Boat pribadi Igor di pelabuhan"
        }
        
        jawaban_benar = "2"
        
        for kunci, nilai in lokasi_penahan_opsi.items():
            print(f"{kunci}. {nilai}")
        
        guess = input("\nLokasi penahanan? (1/2/3): ").strip()
        
        if guess == jawaban_benar:
            print("\n✓ BENAR! Walikota disembunyikan di Gudang di Tepi Kota!")
            print("Polisi segera melakukan penggerebekan dan menyelamatkan walikota!")
            self.poin += 15
            self.teka_teki_selesai.append("Lokasi Penahanan")
            self.tampilkan_status()
            return True
        else:
            print("\n✗ SALAH! Lokasi penahanan berbeda.")
            print("Jawaban yang benar: Gudang tua di tepi kota")
            print("\n⚠️  PERINGATAN: Tim penyelamat dikirim ke lokasi yang salah! Walikota dalam bahaya!")
            self.nyawa -= 30
            print(f"❌ Nyawa berkurang 30 poin! Nyawa sisa: {self.nyawa}")
            self.tampilkan_status()
            return False
    
    def bonus_teka_teki_cepat(self):
        """Bonus: Mini teka-teki cepat untuk poin tambahan"""
        print("\n[BONUS: TEKA-TEKI CEPAT]")
        print("━" * 50)
        print("\nJawab pertanyaan cepat untuk poin bonus!")
        
        soal = [
            {
                "pertanyaan": "Berapa nomor polisi yang menangkap Igor?",
                "opsi": ["1", "2", "3"],
                "jawaban": "2"
            },
            {
                "pertanyaan": "Hari apa walikota hilang?",
                "opsi": ["Senin", "Rabu", "Jum'at"],
                "jawaban": "3"
            }
        ]
        
        soal_random = random.choice(soal)
        print(f"\n{soal_random['pertanyaan']}")
        for i, opsi in enumerate(soal_random['opsi'], 1):
            print(f"{i}. {opsi}")
        
        guess = input("\nJawaban (1/2/3): ").strip()
        if guess == soal_random['jawaban']:
            print("\n✓ BENAR! +5 poin bonus!")
            self.poin += 5
            self.tampilkan_status()
            return True
        else:
            print("\n✗ SALAH! Tidak ada poin bonus.")
            print("\n⚠️  PERINGATAN: Detail kecil pun penting dalam investigasi! Lebih teliti lagi!")
            self.nyawa -= 30
            print(f"❌ Nyawa berkurang 30 poin! Nyawa sisa: {self.nyawa}")
            self.tampilkan_status()
            return False
    
    def tampilkan_kesimpulan(self):
        """Menampilkan kesimpulan akhir game"""
        print("\n" + "="*60)
        print("INVESTIGASI SELESAI!")
        print("="*60)
        print(f"\n📋 RINGKASAN KASUS:")
        print(f"   Penyelidik: {self.nama_pemain}")
        print(f"   Total Poin: {self.poin}")
        print(f"   Nyawa Sisa: {self.nyawa}")
        print(f"   Teka-teki Terpecahkan: {len(self.teka_teki_selesai)}/5")
        
        print(f"\n📊 HASIL INVESTIGASI:")
        print(f"   ✓ Lokasi Tercakap: Bank Kota Maharaja")
        print(f"   ✓ Penculik Tertangkap: Igor Molodov")
        print(f"   ✓ Motif Terbongkar: Perebutan kontrak proyek infrastruktur")
        print(f"   ✓ Bukti Fisik: Cincin emas walikota")
        print(f"   ✓ Lokasi Penahanan: Gudang di Tepi Kota")
        
        print(f"\n👨‍⚖️ HASIL AKHIR:")
        if self.poin >= 50:
            print("★★★ LUAR BIASA! Anda adalah detektif terbaik!")
            print("Kasus diselesaikan dengan sempurna.")
        elif self.poin >= 35:
            print("★★ SANGAT BAIK! Penyelidikan berhasil.")
            print("Walikota berhasil diselamatkan dan penculik ditangkap.")
        elif self.poin >= 20:
            print("★ CUKUP BAIK. Kasus ini cukup menantang.")
            print("Setidaknya walikota telah ditemukan.")
        else:
            print("Penyelidikan masih berjalan. Coba lagi dan perhatikan setiap detail!")
        
        print(f"\n📜 PETUNJUK YANG DIKUMPULKAN:")
        for i, petunjuk in enumerate(self.petunjuk, 1):
            print(f"   {i}. {petunjuk}")
        
        print("\n" + "="*60)
        print("Terima kasih telah memainkan Mystery Adventure Bot!")
        print("="*60 + "\n")
    
    def main_game(self):
        """Jalankan game utama"""
        self.tampilkan_intro()
        
        print("\nMulai menyelidiki? (ya/tidak): ", end="")
        mulai = input().lower()
        
        if mulai != "ya":
            print("\nGim dibatalkan. Sampai jumpa lagi!")
            return
        
        # Jalankan semua teka-teki
        print("\n" + "-"*60)
        self.tebak_lokasi()
        if self.nyawa <= 0:
            return self.game_over()
        
        print("\n" + "-"*60)
        self.tebak_penjahat()
        if self.nyawa <= 0:
            return self.game_over()
        
        print("\n" + "-"*60)
        self.tebak_motif()
        if self.nyawa <= 0:
            return self.game_over()
        
        print("\n" + "-"*60)
        self.tebak_barang_bukti()
        if self.nyawa <= 0:
            return self.game_over()
        
        print("\n" + "-"*60)
        self.tebak_lokasi_penculikan()
        if self.nyawa <= 0:
            return self.game_over()
        
        print("\n" + "-"*60)
        input("\nTekan Enter untuk melanjutkan ke bonus... ")
        self.bonus_teka_teki_cepat()
        if self.nyawa <= 0:
            return self.game_over()
        
        # Tampilkan kesimpulan akhir
        self.tampilkan_kesimpulan()

def game_utama():
    print("=" * 60)
    print("MYSTERY ADVENTURE BOT")
    print("=" * 60)
    print("\nSelamat datang, penyidik!")
    
    nama = input("\nPertama-tama, siapakah namamu? ").strip()
    
    if not nama:
        nama = "Detective Anonim"
    
    game = MysteryAdventureBot(nama)
    game.main_game()
    
if __name__ == "__main__":
    game_utama()