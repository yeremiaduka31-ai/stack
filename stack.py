from collections import deque

stack = deque()

while True:
    print("\n===== PROGRAM STACK =====")
    print("1. Append (tambah kanan)")
    print("2. AppendLeft (tambah kiri)")
    print("3. Pop (hapus kanan)")
    print("4. PopLeft (hapus kiri)")
    print("5. Clear (hapus semua)")
    print("6. Keluar")
    print("=========================")
    print("Isi stack saat ini:", list(stack))

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        data = input("Masukkan data untuk append: ")
        stack.append(data)
        print("Data", data, "ditambahkan ke kanan.")

    elif pilihan == '2':
        data = input("Masukkan data untuk append left: ")
        stack.appendleft(data)
        print("Data", data, "ditambahkan ke kiri.")

    elif pilihan == '3':
        if len(stack) > 0:
            data = stack.pop()
            print("Data", data, "dihapus dari kanan.")
        else:
            print("Stack kosong!")

    elif pilihan == '4':
        if len(stack) > 0:
            data = stack.popleft()
            print("Data", data, "dihapus dari kiri.")
        else:
            print("Stack kosong!")

    elif pilihan == '5':
        stack.clear()
        print("Semua data dalam stack telah dihapus.")

    elif pilihan == '6':
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid! Coba lagi.")
