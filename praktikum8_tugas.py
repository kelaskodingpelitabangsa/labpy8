import os

mahasiswa_template = {
    'nama':'nama',
    'nim':'000000000',
    'uts':0,
    'uas':0,
    'tugas':0,
    'nilai_akhir':0
}

data_mahasiswa = {}

class d_mahasiswa():
    def tambah_data(self):
        print("Silahkan isi data di bawah ini,")
        mahasiswa = dict.fromkeys(mahasiswa_template.keys())

        mahasiswa['nama'] = input("Nama           : ")
        mahasiswa['nim'] = int(input("NIM            : "))
        mahasiswa['uts'] = int(input("Nilai UTS      : "))
        mahasiswa['uas'] = int(input("Nilai UAS      : "))
        mahasiswa['tugas'] = int(input("Nilai Tugas    : "))
        NAMA = mahasiswa['nama']
        NIM = mahasiswa['nim']
        UTS = mahasiswa['uts']
        UAS = mahasiswa['uas']
        TUGAS = mahasiswa['tugas']
        mahasiswa['nilai_akhir'] = TUGAS*0.30 + UTS*0.35 + UAS*0.35
        NILAI_AKHIR = mahasiswa['nilai_akhir']

        KEY = mahasiswa['nim']
        data_mahasiswa.update({KEY:mahasiswa})
        
        print("-"*70)
        print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
        print("="*70)
        print(f"|{NAMA:^15}|{NIM:^10}|{UTS:^8}|{UAS:^8}|{TUGAS:^8}|{NILAI_AKHIR:^14.2f}|")
        print("-"*70)

    def lihat_data(self):
        if data_mahasiswa.items():
            os.system("clear")
            print("-"*70)
            print(f"|{'DAFTAR MAHASISWA':^68}|")
            print("-"*70)
            print(f"|{'No':^4}|{'Nama':^15}|{'NIM':^10}|{'UTS':^7}|{'UAS':^7}|{'Tugas':^7}|{'Nilai Akhir':^12}|")
            print("="*70)
            
            no = 1
            for mahasiswa in data_mahasiswa.items():
                print(f"|{no:^4}|{mahasiswa[1]['nama']:^15}|{mahasiswa[1]['nim']:^10}|{mahasiswa[1]['uts']:^7}|{mahasiswa[1]['uas']:^7}|{mahasiswa[1]['tugas']:^7}|{mahasiswa[1]['nilai_akhir']:^12.2f}|")
                no += 1
            print("-"*70)

        else:
            print("-"*70)
            print(f"|{'DAFTAR MAHASISWA':^68}|")
            print("-"*70)
            print(f"|{'No':^4}|{'Nama':^15}|{'NIM':^10}|{'UTS':^7}|{'UAS':^7}|{'Tugas':^7}|{'Nilai Akhir':^12}|")
            print("="*70)
            print(f"|{'TIDAK ADA DATA':^68}|")
            print("="*70)

    def ubah_data(self):
        print("Silahkan masukkan NIM yang akan di ubah datanya,")
        nim_input = int(input("NIM            : "))
        if nim_input in data_mahasiswa.keys():
            data_mahasiswa[nim_input]['uts'] = int(input("Nilai UTS      : "))
            data_mahasiswa[nim_input]['uas'] = int(input("Nilai UAS      : "))
            data_mahasiswa[nim_input]['tugas'] = int(input("Nilai Tugas    : "))
            UTS_ = data_mahasiswa[nim_input]['uts']
            UAS_ = data_mahasiswa[nim_input]['uas']
            TUGAS_ = data_mahasiswa[nim_input]['tugas']
            data_mahasiswa[nim_input]['nilai_akhir']= UTS_*0.35 + UAS_*0.35 + TUGAS_*0.30
            NILAI_AKHIR_ = data_mahasiswa[nim_input]['nilai_akhir']
            
            print("-"*70)
            print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
            print("="*70)
            print(f"|{data_mahasiswa[nim_input]['nama']:^15}|{data_mahasiswa[nim_input]['nim']:^10}|{UTS_:^8}|{UAS_:^8}|{TUGAS_:^8}|{NILAI_AKHIR_:^14.2f}|")
            print("-"*70)

        else:
            print(f"NIM {nim_input} tidak ditemukan!!!")

    def hapus_data(self):
        print("Silahkan masukkan NIM yang akan di hapus,")
        nim_input = int(input("NIM            : "))
        if nim_input in data_mahasiswa.keys():
            del data_mahasiswa[nim_input]
            print(f"Data NIM {nim_input} berhasil di hapus")

        else:
            print(f"NIM {nim_input} tidak ditemukan!!!")

    def cari_data(self):
        print("Silahkan masukkan NIM yang akan di cari,")
        nim_input = int(input("NIM           : "))
        if nim_input in data_mahasiswa.keys():
            print("-"*70)
            print(f"|{'DAFTAR MAHASISWA':^68}|")
            print("-"*70)
            print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
            print("="*70)
            print(f"|{data_mahasiswa[nim_input]['nama']:^15}|{data_mahasiswa[nim_input]['nim']:^10}|{data_mahasiswa[nim_input]['uts']:^8}|{data_mahasiswa[nim_input]['uas']:^8}|{data_mahasiswa[nim_input]['tugas']:^8}|{data_mahasiswa[nim_input]['nilai_akhir']:^14.2f}|")
            print("-"*70)

        else:
            print(f"NIM {nim_input} tidak ditemukan!!!")

    def is_done(self):
        x = input("Tekan tombol enter untuk melanjutkan!!! ")
    
dm = d_mahasiswa()

while True:
    os.system("clear")
    print(f"{'PROGRAM NILAI MAHASISWA':^70}")
    print("="*70)
    print("Silahkan pilih menu :")
    i = input("(T)ambah | (U)bah | (H)apus | (C)ari | (L)ihat | (K)eluar : ")

    #Tambah data
    if i.lower() == 't':
        dm.tambah_data()
        dm.is_done()

    #Lihat Data
    elif i.lower() == 'l':
        dm.lihat_data()
        dm.is_done()
       
    #Ubah data
    elif i.lower() == 'u':
        dm.ubah_data()
        dm.is_done()
        # no = 1
        

    #Hapus Data
    elif i.lower() == 'h':
        dm.hapus_data()
        dm.is_done()

    #Cari Data
    elif i.lower() == 'c':
        dm.cari_data()
        dm.is_done()
    
    #Keluar
    elif i.lower() == 'k':
        break

    elif i.lower() == 'dump':
        print(data_mahasiswa)
        dm.is_done()

    else:
        print("Silahkan pilih menu yang tersedia!!!")
        dm.is_done()
