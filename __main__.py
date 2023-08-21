import csv
import sys
import os
import tabulate
import pyinputplus as pypi

def clearScreen():
    """
    Function for cleaning the user's screen
    """
    # Untuk Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Untuk macOS and Linux
    else:
        _ = os.system('clear')

def show_data (database):
    # Fungsi Untuk Show Database
    data = list(database.values())[1:]
    header = database['column']
    print(tabulate.tabulate(data, header, tablefmt="outline"))
    print("\n")

def readMenu (database):
    # Main Program Show dan Print data ke prompt dalam bentuk tabulasi
    data = list(database.values())[1:]
    while True:
        print("""
----------Menu Read Star Phone Store----------
    
    1. Tampilkan Semua Daftar Smartphone
    2. Pilih Berdasar OS Smartphone
    3. Kembali ke Menu Utama
    """)
        choices = ["Tampilkan Semua Daftar Smartphone", "Pilih Berdasar OS Smartphone", "Kembali ke Menu Utama"]
        userInput = pypi.inputInt(prompt='\nMasukkan Index pada Read Menu :\n', max=len(choices))
        if userInput == 1:
            show_data(db)
        elif userInput == 2:
            pilih_os (db)
        elif userInput == 3:
            response = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu utama? (yes/no)')
            if response == 'yes':
                main ()
            elif response == 'no':
                readMenu (db)

def addMenu (database):
    # Main Program add/create data ke prompt dalam bentuk tabulasi
    data = list(database.values())[1:]
    while True:
        print("""
----------Menu Tambah Data Star Phone Store----------
    
    1. Tambahkan Data Smartphone
    2. Lihat Data Smartphone Update
    3. Kembali ke Menu Utama
    """)
        choices = ["Tambahkan Data Smartphone", "Lihat Data Smartphone Update", "Kembali ke Menu Utama"]
        userInput = pypi.inputInt(prompt='\nMasukkan Index pada Read Menu :\n', max=len(choices))
        if userInput == 1:
            addFunction(db)
        elif userInput == 2:
            show_data (db)
        elif userInput == 3:
            response = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu utama? (yes/no)')
            if response == 'yes':
                main ()
            elif response == 'no':
                addMenu (db)

def updateMenu (database):
    # Main Program update data ke prompt dalam bentuk tabulasi
    data = list(database.values())[1:]
    while True:
        print("""
----------Menu Update Data Star Phone Store----------
    
    1. Update Data Smartphone
    2. Lihat Data Smartphone Update
    3. Kembali ke Menu Utama
    """)
        choices = ["Update Data Smartphone", "Lihat Data Smartphone Update", "Kembali ke Menu Utama"]
        userInput = pypi.inputInt(prompt='\nMasukkan Index pada Read Menu :\n', max=len(choices))
        if userInput == 1:
            updateFunction(db)
        elif userInput == 2:
            show_data (db)
        elif userInput == 3:
            response = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu utama? (yes/no)')
            if response == 'yes':
                main ()
            elif response == 'no':
                addMenu (db)
                
def deleteMenu (database):
    # Main Program delete data ke prompt dalam bentuk tabulasi
    data = list(database.values())[1:]
    while True:
        print("""
----------Menu Update Data Star Phone Store----------
    
    1. Delete Data Smartphone
    2. Lihat Data Smartphone Update
    3. Kembali ke Menu Utama
    """)
        choices = ["Delete Data Smartphone", "Lihat Data Smartphone Update", "Kembali ke Menu Utama"]
        userInput = pypi.inputInt(prompt='\nMasukkan Index pada Read Menu :\n', max=len(choices))
        if userInput == 1:
            deleteFunction(db)
        elif userInput == 2:
            show_data (db)
        elif userInput == 3:
            response = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu utama? (yes/no)')
            if response == 'yes':
                main ()
            elif response == 'no':
                addMenu (db)

def buyMenu (database):
    # Main Program pembelian barang ke prompt dalam bentuk tabulasi
    data = list(database.values())[1:]
    while True:
        print("""
----------Menu Update Data Star Phone Store----------
    
    1. Beli Smartphone
    2. Lihat Data Smartphone Update
    3. Kembali ke Menu Utama
    """)
        choices = ["Beli Smartphone", "Lihat Data Smartphone Update", "Kembali ke Menu Utama"]
        userInput = pypi.inputInt(prompt='\nMasukkan Index pada Read Menu :\n', max=len(choices))
        if userInput == 1:
            buyFunction(db)
        elif userInput == 2:
            show_data (db)
        elif userInput == 3:
            response = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu utama? (yes/no)')
            if response == 'yes':
                main ()
            elif response == 'no':
                addMenu (db)

def filter_android():
    '''Fungsi untuk memfilter OS Android pada database
    '''
    # input the key (ANDROID) that used to filter
    key = 'ANDROID'

    # Create dataset from the selected value
    filterDataset = {}
    for val in db.values():
        if key in val:
            filterDataset.update({
                val[0]:val
            })  
    print(tabulate.tabulate(filterDataset.values(),headers=headings,tablefmt="outline"))

def filter_ios():
    '''Fungsi untuk memfilter OS IOS pada database
    '''
    # input the key (IOS) that used to filter
    key = 'IOS'

    # Create dataset from the selected value
    filterDataset = {}
    for val in db.values():
        \
        
        if key in val:
            filterDataset.update({
                val[0]:val
            })  
    print(tabulate.tabulate(filterDataset.values(),headers=headings,tablefmt="outline"))
    
def pilih_os (database):
    # Main Function Pemilihan Smartphone berdasarkan OS, menampilkan dalam bentuk tabulasi 
    data = list(database.values())[1:]
    while True:

        print("""
----------Menu Read Star Phone Store----------
    
    1. Tampilkan Smartphone OS Android
    2. Tampilkan Smartphone OS iOS
    3. Kembali ke Menu Sebelumnya
    """)
        choice = ['Pilih OS Android', 'Pilih OS iOS', 'Kembali ke Menu Sebelumnya']
        userInp = pypi.inputMenu(prompt='Pilih Smartphone berdasarkan OS:\n', choices=choice, numbered = True)
        if userInp == 'Pilih OS Android':
            filter_android ()
        elif userInp == 'Pilih OS iOS':
            filter_ios ()
        elif userInp == 'Kembali ke Menu Sebelumnya':
            response = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu sebelumnya? (yes/no)')
            if response == 'yes':
                readMenu (db)
            if response == 'no':
                pilih_os (db)

def addFunction (database):
    """Fungsi untuk menambahkan item ke dalam database

    Args:
        database (dict): database yang akan diolah

    Returns:
        dict: data terbaru
    """
    # Input nama item Smartphone
    namePhone = pypi.inputStr(
        prompt="Input Nama Smartphone: ",
        applyFunc=lambda x: x.title()
    ).title()

    # Cek nama item, apakah sudah exist?
    if namePhone in list(database):
        print ('\nData sudah terdapat di Database!, \nSilahkan Kembali pilih Update Menu!\n')
        addMenu (db)

    else:
        # Input jenis OS Android/ iOS, validasi dengan string
        OSPhone = pypi.inputStr(
            prompt="Input OS Smartphone: ",
        ).upper()
        # Input Jenis Chipset, validasi dengan string
        chipsetPhone = pypi.inputStr(
            prompt="Input Chipset Smartphone: ",
        ).title()
        # Input jenis RAM, validasi dengan integer number
        ramPhone = pypi.inputInt(
            prompt="Input RAM Smartphone: ",blockRegexes='-'
        )
        # Input besar memory, validasi dengan integer number
        memoryPhone = pypi.inputInt(
            prompt="Input Memori Smartphone: ",blockRegexes='-'
        )
        # Input jumlah item yang diinput, validasi dengan integer number
        countPhone = pypi.inputInt(
            prompt="Input Jumlah Smartphone: ",blockRegexes='-'
        )
        # Input harga item, validasi dengan integer number
        pricePhone = pypi.inputInt(
            prompt="Input Harga Smartphone: ",blockRegexes='-'
        )
    
    #Konfirmasi Ulang Untuk Input Data Smartphone
    tabularAddedData = [namePhone, OSPhone, chipsetPhone, ramPhone, memoryPhone, countPhone, pricePhone]
    print(tabulate.tabulate(list([tabularAddedData]), headers=headings, tablefmt="github"))
    response = pypi.inputYesNo(prompt='Apakah Anda Ingin Menambah Data? (yes/no)')
    if response == 'no':
        addMenu(db)
    else:
        database.update(
            {f"{namePhone}": [len(database) - 1, namePhone, OSPhone, chipsetPhone, ramPhone, 
                              memoryPhone, countPhone, pricePhone]}
        )
    # Menampilkan daftar item terbaru
    show_data (database)
    return database

def updateFunction (database):
    """Fungsi untuk menambahkan item ke dalam database

    Args:
        database (dict): database yang akan diolah

    Returns:
        dict: data terbaru
    """
    # Input nama item Smartphone
    namePhone = pypi.inputStr(
        prompt="Input Nama Smartphone: ",
        applyFunc=lambda x: x.title()
    ).title()

     # Cek nama item, apakah sudah exist?
    if namePhone not in list(database):
        print ('\nData tidak terdapat di Database!, \nSilahkan Kembali pilih Create/ Add Menu!\n')
        updateMenu (db)

    # Input jenis OS Android/ iOS, validasi dengan string
    OSPhone = pypi.inputStr(
        prompt="Input OS Smartphone: ",
    ).upper()
    # Input Jenis Chipset, validasi dengan string
    chipsetPhone = pypi.inputStr(
        prompt="Input Chipset Smartphone: ",
    ).title()
    # Input jenis RAM, validasi dengan integer number
    ramPhone = pypi.inputInt(
        prompt="Input RAM Smartphone: ",blockRegexes='-'
    )
    # Input besar memory, validasi dengan integer number
    memoryPhone = pypi.inputInt(
        prompt="Input Memori Smartphone: ",blockRegexes='-'
    )
    # Input jumlah item yang diinput, validasi dengan integer number
    countPhone = pypi.inputInt(
        prompt="Input Jumlah Smartphone: ",blockRegexes='-'
    )
    # Input harga item, validasi dengan integer number
    pricePhone = pypi.inputInt(
        prompt="Input Harga Smartphone: ",blockRegexes='-'
    )

    tabularAddedData = [namePhone, OSPhone, chipsetPhone, ramPhone, memoryPhone, countPhone, pricePhone]
    print(tabulate.tabulate(list([tabularAddedData]), headers=headings, tablefmt="github"))
    # Apabila item tersedia, update stock atau harga item tersebut
    response = pypi.inputYesNo(prompt='Apakah Anda Ingin Update Data? (yes/no)')
    if response == 'no':
        updateMenu(db)
    else :
        database[namePhone][1] = namePhone
        database[namePhone][2] = OSPhone
        database[namePhone][3] = chipsetPhone
        database[namePhone][4] = ramPhone
        database[namePhone][5] = memoryPhone
        database[namePhone][6] += countPhone
        database[namePhone][7] = pricePhone
   
    # Menampilkan daftar item terbaru
    show_data(database)
    return database

def deleteFunction (database):
    """Fungsi untuk menghapus item dari database

    Args:
        database (dict): databases yang akan diolah

    Returns:
        dict: data terbaru
    """
    # Input indeks item yang akan dihapus
    # Validasi dengan indeks item yang tersedia
    id = pypi.inputInt(prompt="Input indeks item: ", lessThan=len(database) - 1,blockRegexes='-')

    response = pypi.inputYesNo(prompt='\nApakah Anda Ingin Menghapus Data? (yes/no)\n')
    if response == 'no':
        deleteMenu(db)
    else :
    # Loop terhadap database
        for key, value in database.copy().items():
            if key == "column":
                continue
        # Jika item tersedia, hapus item berdasarkan indeks
        if id in value:
            del database[key]
        # Selain itu, update indeks item yang tersisa
        elif id < value[0]: 
            database.update({f"{key}": [value[0] - 1, value[1], value[2], value[3],value[4],value[5],value[6],value[7]]})
    # Menampilkan daftar item terbaru
    show_data(database)
    return deleteMenu

def buyFunction (database):
    """Fitur untuk membeli item dari databases

    Args:
        database (dict): databases yang akan diolah

    Returns:
        dict: data terbaru
    """
    # Deklarasi variabel 'chart'
    chart = {
        "column": ["nama",  "qty", "harga"],
    }
    while True:
        # Menampilkan data Smartphone terbaru
        show_data(database)
        # Input indeks item yang akan dibeli
        # Validasi dengan indeks item yang tersedia
        id = pypi.inputInt(prompt="Input indeks item: ", lessThan=len(database) - 1,blockRegexes='-')
        # Breakdown item Smartphone menjadi nama, stock, dan harga
        for value in database.values():
            if id in value:
                name, stock, price = value[1], value [-2], value [-1]      
                break
        # Input jumlah item, validasi dengan stock yang tersedia
        countPhone = pypi.inputInt(
            prompt="Input jumlah item: ",
            max=stock,
        )
        # Jika jumlah pesanan terpenuhi, update listChart
        chart.update({f"{name}": [name, countPhone, price]})
        # Kurangi persedian stock di database
        # print (f'ERORRR= {database[name][2]} - {countPhone}')
        database[name][-2] -= countPhone
        # Tampilkan isi keranjang belanjaan
        print ('\nIsi Keranjang Anda :\n')
        show_data (chart)
        # Konfirmasi status re-order
        reorder = pypi.inputYesNo(prompt="Beli item lain?(yes/no): ")
        if reorder.lower() == "no":
            break

    # Proses kalkulasi total harga
    for key, value in chart.items():
        if key == "column":
            # Tambah kolom 'total harga'
            value.append("total harga")
            chart[key] = value
        else:
            # Kalkulasi Qty x Harga
            value.append(value[1] * value[2])
            chart[key] = value

    # Proses pembayaran
    while True:
        # Menampilkan daftar belanja
        print ("\nDaftar Belanjaan Anda\n")
        show_data(chart)
        # Hitung total harga yang harus dibayar
        price = 0
        for value in list(chart.values())[1:]:
            price += value[-1]
        print(f"\nTotal yang harus dibayar: {price}")
        # Input jumlah uang pembayaran
        pay = pypi.inputInt(
            prompt="Input jumlah uang: ",
            min=price,
        )
        # Jika uang terpenuhi, tampilkan kembalian dan terima kasih
        print(f"Uang kembalian anda {pay - price}, terima kasih.")
        break
    # Kosongkan keranjang belanja
    del chart
    return buyMenu

def main():
    """
    Program Utama Untuk Menjalankan Proses Keseluruhan
    """
    global db
    while True:
    
        # Menampilkan Program Utama
        prompt = f"Selamat Datang di Alfian Phone Store! \n\nPilihan Menu:\n"
        print (prompt)
        # Memilih Menu yang Akan di Eksekusi
        choice = ["Menampilkan Stock Smartphone", 
                  "Menambah Stock Smartphone",
                  "Update Stock Smartphone", 
                  "Menghapus Stock Smartphone", 
                  "Melakukan Pembelian Smartphone", 
                  "Exit Program"]
        for index,values in enumerate(choice):
            print(f'{index+1}. {values}')
        # user Input
        userInput = pypi.inputInt(prompt='\nMasukan Angka Pilihan Menu :\n', max=len(choice))

# Menjalankan Menu yang Dipilih
        if userInput == 1:
            readMenu(db)
        elif userInput == 2:
            addMenu(db)
        elif userInput == 3:
            updateMenu(db)
        elif userInput == 4:
            deleteMenu(db)
        elif userInput == 5:
            buyMenu(db)
            #db = deleteMenu(db) 
        elif userInput == 6:
            break
            #print('Have a great one!')
            
    # Import database file
    file = open(path, "w")
    # Menjaga Database Up to Date
    writer = csv.writer(file, lineterminator='\n', delimiter=';')
    columns = list(db.values())[0] # termasuk kolom dan data
    data = list(db.values())[1:]
    writer.writerow(columns) #db.values()
    data = list(db.values())[1:]
    for i in data:
         writer.writerow(i)

if __name__ == "__main__":
    # Cleaning Screen User
    clearScreen()
    # Setting Path Database CSV
    path = r'C:\10. Project Capstone - Edit Edit\phonemarketcapstone\data.csv'
    # Cek database contents, jika kosong, munculkan pesan berikut.
    if os.path.getsize(path) == 0:
        print('Database Kosong, Mohon Masukan Data Terlebih Dahulu!')
    else:
        # Import database file
        file = open(path)
        # Membaca Data dari Database
        reader = csv.reader(file, delimiter=";")
        # Create dictionary dari database
        headings = next(reader)
        if len(headings) == 0:
            headings =  ['Index','nameBrand','OS','chipset','RAM (*GB)','memory (*GB)','stock','harga']
        else:
            db = {"column": headings}
        for row in reader:
            db.update(
                {
                    str(row[1]): [
                        int(row[0]), 
                        str(row[1]), 
                        str(row[2]), 
                        str(row[3]),
                        int(row[4]),
                        int(row[5]),
                        int(row[6]),
                        int(row[7]),
                    ]
                }
            )
        # Close database file
        file.close()
        # Menjalankan program utama
        main()
    # Close program
    sys.exit()