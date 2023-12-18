import time
import os
def banner():
    print("\n \n")

    print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
    print('@  @  @ @ @     @    @ @   @ @     @')
    print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
    print('@  @  @ @ @     @    @ @   @ @     @')
    print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')


    print("\n \n")

def clear():
    os.system('cls' if os.name == "nt" else "clear")

dataMahasiswa = []

def inputData():
    banner()
    print("[1]. Input Data (Nama dan Nilai Mahasiswa) >> ")
    print("(ketik exit untuk keluar dari menu ini.)")
    nama = input("Masukkan Nama: ")
    userDitemukan = False
    if nama.lower() == "exit":
        return clear(), main()
    else:
        for user in dataMahasiswa:
            if user['nama'].lower() == nama.lower().strip():
                userDitemukan = True
                print("Nama sudah terdaftar!, silahkan cari nama lain")
                return time.sleep(1), clear(), inputData()
        if not userDitemukan:
            if nama.isalpha() and not nama.isdigit():
                prak1 = input("Masukan Nilai Praktikum ke-1 : ")
                prak2 = input("Masukan Nilai Praktikum ke-2 : ")
                prak3 = input("Masukan Nilai Praktikum ke-3 : ")
                if (prak1 == "exit") or (prak2 == "exit") or (prak3 == "exit") or ((prak1 and prak2 and prak3) == "exit"):
                    return clear(), main()
                elif (prak1 and prak2 and prak3).isdigit():
                    data = {"nama": nama, "prak1": int(prak1), "prak2": int(prak2), "prak3": int(prak3)}
                    dataMahasiswa.append(data)
                    print("Berhasil menginput data!")
                    return time.sleep(1), clear(),main()
                else:
                    print("Nilai Praktikum harus angka!")
                    return time.sleep(1), clear(), inputData()
            else:
                print("Masukan nama yang benar!")
                return time.sleep(1), clear(), inputData()

def rataRata():
    banner()
    print("[2]. Rata Rata Nilai Praktikum Mahasiswa")
    print("------------------------------------------------")
    print("| Mahasiswa | Rata-Rata |       Praktikum      |")
    print("------------------------------------------------")
    for user in dataMahasiswa:
        rata_rata = ((user['prak1'] + user['prak2'] + user['prak3']) / 3)
        print("| {} | {} | {}  {}  {} |".format(user['nama'].ljust(9),str(round(rata_rata, 2)).ljust(9),str(user['prak1']).ljust(7),str(user['prak2']),str(user['prak3']).rjust(7)))
    totalPrak1 = sum(user['prak1'] for user in dataMahasiswa)
    totalPrak2 = sum(user['prak2'] for user in dataMahasiswa)
    totalPrak3 = sum(user['prak3'] for user in dataMahasiswa)
    jumlahData = len(dataMahasiswa)
    rataPrak1 = totalPrak1 / jumlahData
    rataPrak2 = totalPrak2 / jumlahData
    rataPrak3 = totalPrak3 / jumlahData
    print("------------------------------------------------")
    print("| Rata Rata Praktikum   | {}  {}  {} |".format(str(int(rataPrak1)).ljust(7), str(int(rataPrak2)), str(int(rataPrak3)).rjust(7)))
    opsi = input("| Keluar? (y/n) : ")
    if opsi in ("y", "yes"):
        return clear(), main()
    elif opsi in ("no", "n"):
        return rataRata()
    else:
        print("Opsi Tidak Valid!")
        return rataRata()

def main():
    banner()
    print("======<MENU>======")
    print("1. Input Data")
    print("2. Menghitung Rata - Rata")
    print("0. Keluar Dari program")
    opsi = input("pilih opsi : ")

    if opsi == "1":
        clear()
        inputData()
        
    elif opsi == "2":
        clear()
        rataRata()
        
    elif opsi == "0":
        print("Terima kasih telah menggunakan layanan dari program ini.")
        time.sleep(3)
        clear()
        return exit(time.sleep(2))
    
if __name__ == "__main__":
    clear()
    main()