import tabulate
import pyinputplus as pypi

def pilih_os ():
    print (f'''
            =====Pilih Smartphone Berdasarkan OS=====
            1. OS Android
            2. iOS (Apple)
            3. Kembali ke Menu Utama
            ''')

def readMenu (database, title='''**********Menu #1 Tampilkan Data Smartphone**********\n
         1. Tampilkan Semua Daftar Smartphone
         2. Pilih Berdasar OS Smartphone
         3. Kembali Ke Menu Utama
         '''):
    """Fungsi untuk menampilkan database ke prompt
    Args:
        database (dictionary): database yang akan ditampilkan
        title (str, optional): judul tampilan. Defaults "\nDaftar Smartphone yang Tersedia\n".
    """
    # Menampilkan judul
    print(title)
    # Main Program Show dan Print data ke prompt dalam bentuk tabulasi

    data = list(database.values())[1:]
    header = database['column']
    print(tabulate.tabulate(data, header, tablefmt="outline"))
    print("\n")


def addMenu(database):
    """Fungsi untuk menambahkan item ke dalam database

    Args:
        database (dict): database yang akan diolah

    Returns:
        dict: data terbaru
    """
    # Input nama item, validasi dengan regex numerik
    namePhone = pypi.inputStr(
        prompt="Input Brand Smartphone: ",
        applyFunc=lambda x: x.capitalize(),
        blockRegexes=[r"[0-9]"],
    )
    # Input jumlah item, validasi dengan integer number
    OSPhone = pypi.inputStr(
        prompt="Input Tipe Smartphone: ",
    )
    # Input harga item, validasi dengan integer number
    chipsetPhone = pypi.inputStr(
        prompt="Input Chipset Smartphone: ",
    )
    # Input harga item, validasi dengan integer number
    ramPhone = pypi.inputInt(
        prompt="Input RAM Smartphone: ",
    )
    # Input harga item, validasi dengan integer number
    memoryPhone = pypi.inputInt(
        prompt="Input Memori Smartphone: ",
    )
    # Input harga item, validasi dengan integer number
    countPhone = pypi.inputInt(
        prompt="Input Jumlah Smartphone: ",
    )
    # Input harga item, validasi dengan integer number
    pricePhone = pypi.inputInt(
        prompt="Input Harga Smartphone: ",
    )
    # Apabila item tersedia, update stock atau harga item tersebut
    if namePhone in list(database):
        database[namePhone][2] = OSPhone
        database[namePhone][3] = chipsetPhone
        database[namePhone][4] = ramPhone
        database[namePhone][5] = memoryPhone
        database[namePhone][6] += countPhone
        database[namePhone][7] = pricePhone
    # Selain itu, tambahkan sebagai item baru
    else:
        database.update(
            {f"{namePhone}": [len(database) - 1, namePhone, typePhone, chipsetPhone, ramPhone, 
                              memoryPhone, countPhone, pricePhone]}
        )
    # Menampilkan daftar item terbaru
    show(database)
    return database


def updateMenu(database):

def deleteMenu(database):
    """Fungsi untuk menghapus item dari database

    Args:
        database (dict): databases yang akan diolah

    Returns:
        dict: data terbaru
    """
    # Input indeks item yang akan dihapus
    # Validasi dengan indeks item yang tersedia
    id = pypi.inputInt(prompt="Input indeks item: ", lessThan=len(database) - 1)
    # Loop terhadap database
    for key, value in database.copy().items():
        if key == "column":
            continue
        # Jika item tersedia, hapus item berdasarkan indeks
        if id in value:
            del database[key]
        # Selain itu, update indeks item yang tersisa
        elif id < value[0]: 
            database.update({f"{key}": [value[0] - 1, value[1], value[2], value[3]]})
    # Menampilkan daftar item terbaru
    show(database)
    return database


def buyMenu(database):
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
        show(database)
        # Input indeks item yang akan dibeli
        # Validasi dengan indeks item yang tersedia
        id = pypi.inputInt(prompt="Input indeks item: ", lessThan=len(database) - 1)
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
        show(chart, title="\nIsi Keranjang Anda\n")
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
        show(chart, title="\nDaftar Belanjaan Anda\n")
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
    return database

    
