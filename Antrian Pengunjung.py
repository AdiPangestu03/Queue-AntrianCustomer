class Customer:
    def __init__(self, nama):
        self.nama = nama

#Membuat Fungsi yang akan digunakan
class antriCustomer:
    def __init__(self):
        self.antri = []

    #method untuk Menambahkan Antrian
    def add_customer(self, antri):
        self.antri.append(antri)

    #method untuk Menghapus Antrian
    def delete_customer(self, index):
        if 1 <= index <= len(self.antri):
            del self.antri[index-1]
        else:
            print("Nomor antrian tidak ditemukan.")

    # method untuk Menampilkan Antrian
    def display_antrian(self):
        if not self.antri:
            print("Antrian Kosong.")
        else:
            print("Current queue:")
            for i, antri in enumerate(self.antri, start=1):
                print(f"{i}. {antri.nama}")


# Memanggil method di kelas antriCustomer dengan menjadikan variabel "antri" sebagai kapsul 
antri = antriCustomer()

while True:
    # Membuat Opsi pilihan untuk User
    print("\nChoose an option:\n")
    print("1. Tambahkan Antrian")
    print("2. Hapus Antrian")
    print("3. Display Antrian")
    print("4. Quit")
    option = int(input("Enter your choice (1-4): "))

    # Menambahkan Customer
    if option == 1:
        # Memasukkan nama Customer
        nama_customer = []
        while True:
            nama = input("Masukkan nama customer (atau tulis 'done' untuk selesai): ")
            if nama.lower() == "done":
                break
            nama_customer.append(nama)

        # Menambahkan nama tersebut ke Kelas Customer
        for nama in nama_customer:
            antri.add_customer(Customer(nama))

    # Menghapus Customer
    elif option == 2:
        # Menampilkan Antrian saat ini
        antri.display_antrian()

        delete = int(input("Masukkan nomor antrian yang akan dihapus : "))

        # Menghapus Customer sesuai dengan nomor index yang diberikan
        antri.delete_customer(delete) # "delete = no index yang diberikan"

    # Menampilkan antrian
    elif option == 3:
        antri.display_antrian()

    # Quit
    elif option == 4:
        break

    # Invalid option
    else:
        print("Pilihan salah. Mohon ulangi.")