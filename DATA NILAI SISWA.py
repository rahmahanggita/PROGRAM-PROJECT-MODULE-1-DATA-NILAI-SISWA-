# Inisialisasi data dummy menggunakan list of dictionaries
students_data = [
    {'ID': '001', 'NAMA': 'ADRIAN BUDI', 'KELAS': '7A', 'SEMESTER': '1', 'MATEMATIKA': 85, 'B INGGRIS': 78, 'IPA': 92, 'IPS': 74, 'SENI': 88},
    {'ID': '002', 'NAMA': 'ANANDA KRISTIN', 'KELAS': '7A', 'SEMESTER': '1', 'MATEMATIKA': 90, 'B INGGRIS': 82, 'IPA': 89, 'IPS': 76, 'SENI': 91},
    {'ID': '003', 'NAMA': 'BRIAN NOVANDA', 'KELAS': '7A', 'SEMESTER': '1', 'MATEMATIKA': 80, 'B INGGRIS': 85, 'IPA': 80, 'IPS': 75, 'SENI': 85},
    {'ID': '004', 'NAMA': 'CINDY NAYLA', 'KELAS': '7B', 'SEMESTER': '1', 'MATEMATIKA': 90, 'B INGGRIS': 85, 'IPA': 85, 'IPS': 85, 'SENI': 85},
    {'ID': '005', 'NAMA': 'FATIN ANNISA', 'KELAS': '7B', 'SEMESTER': '1', 'MATEMATIKA': 92, 'B INGGRIS': 87, 'IPA': 80, 'IPS': 80, 'SENI': 80},
    {'ID': '006', 'NAMA': 'KARINA AESPA', 'KELAS': '7B', 'SEMESTER': '1', 'MATEMATIKA': 82, 'B INGGRIS': 85, 'IPA': 89, 'IPS': 90, 'SENI': 70},
    {'ID': '007', 'NAMA': 'REYNALD FIDRIANSYAH', 'KELAS': '8A', 'SEMESTER': '1', 'MATEMATIKA': 85, 'B INGGRIS': 78, 'IPA': 92, 'IPS': 74, 'SENI': 88},
    {'ID': '008', 'NAMA': 'ROY MARTIN', 'KELAS': '8A', 'SEMESTER': '1', 'MATEMATIKA': 80, 'B INGGRIS': 72, 'IPA': 85, 'IPS': 79, 'SENI': 90},
    {'ID': '009', 'NAMA': 'RIRIS HARYANTI', 'KELAS': '8A', 'SEMESTER': '1', 'MATEMATIKA': 86, 'B INGGRIS': 85, 'IPA': 90, 'IPS': 85, 'SENI': 79},
    {'ID': '010', 'NAMA': 'JAENAL', 'KELAS': '8B', 'SEMESTER': '1', 'MATEMATIKA': 80, 'B INGGRIS': 86, 'IPA': 85, 'IPS': 86, 'SENI': 88},
    {'ID': '011', 'NAMA': 'REZA AGALANG', 'KELAS': '8B', 'SEMESTER': '1', 'MATEMATIKA': 90, 'B INGGRIS': 85, 'IPA': 89, 'IPS': 80, 'SENI': 89},
    {'ID': '012', 'NAMA': 'BAGAS MAHARDHIKA', 'KELAS': '8B', 'SEMESTER': '1', 'MATEMATIKA': 82, 'B INGGRIS': 90, 'IPA': 85, 'IPS': 81, 'SENI': 82},
    {'ID': '013', 'NAMA': 'IFAN ARI', 'KELAS': '9A', 'SEMESTER': '1', 'MATEMATIKA': 90, 'B INGGRIS': 80, 'IPA': 92, 'IPS': 80, 'SENI': 88},
    {'ID': '014', 'NAMA': 'FAHRUL ANDRIAN', 'KELAS': '9A', 'SEMESTER': '1', 'MATEMATIKA': 87, 'B INGGRIS': 85, 'IPA': 80, 'IPS': 80, 'SENI': 90},
    {'ID': '015', 'NAMA': 'ANNISA PUTRI', 'KELAS': '9A', 'SEMESTER': '1', 'MATEMATIKA': 88, 'B INGGRIS': 88, 'IPA': 80, 'IPS': 90, 'SENI': 85},
    {'ID': '016', 'NAMA': 'JAMILAH', 'KELAS': '9B', 'SEMESTER': '1', 'MATEMATIKA': 88, 'B INGGRIS': 85, 'IPA': 85, 'IPS': 80, 'SENI': 78},
    {'ID': '017', 'NAMA': 'AYU TING TING', 'KELAS': '9B', 'SEMESTER': '1', 'MATEMATIKA': 90, 'B INGGRIS': 89, 'IPA': 81, 'IPS': 78, 'SENI': 80},
    {'ID': '018', 'NAMA': 'RAFFI AHMAD', 'KELAS': '9B', 'SEMESTER': '1', 'MATEMATIKA': 85, 'B INGGRIS': 85, 'IPA': 89, 'IPS': 80, 'SENI': 79}
]

kelas_options = ['7A', '7B', '8A', '8B', '9A', '9B']
semester_options = ['1', '2']

# menampilkan daftar pilihan menu kepada user
def main_menu(): 
    print("Aplikasi Data Nilai Siswa")
    print("1. Lihat Data Siswa")
    print("2. Tambah Data Siswa")
    print("3. Update Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Hitung Rata-rata Nilai Per Siswa")
    print("6. Peringkat Siswa Berdasarkan Kelas")
    print("7. Pencarian Siswa Berdasarkan Nilai Tertentu")
    print("8. Tampilkan Data Rangkuman")
    print("9. Nilai Mata Pelajaran Terbaik dan Terburuk")
    print("10. Keluar")

# inti dari program yang mengontrol alur eksekusi berdasarkan pilihan user:
def main():
    # Dictionary ini memetakan setiap pilihan menu (dalam bentuk string) ke fungsi yang sesuai
    menu_functions = {
        '1': view_students,
        '2': add_student,
        '3': update_student,
        '4': delete_student,
        '5': calculate_average_score_per_student,
        '6': rank_students_by_class,
        '7': search_students_by_score,
        '8': display_summary_data,
        '9': best_and_worst_scores_by_subject,
        '10': exit
    }
    while True:
        main_menu()
        choice = input("Pilih menu (1-10): ")
        print ("")
        if choice in menu_functions:
            menu_functions[choice]()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print ("")

# mencetak tabel ke layar dengan format yang rapi, menggunakan header dan baris data yang diberikan
def print_table(headers, rows):
    column_widths = [max(len(str(value)) for value in column) for column in zip(*([headers] + rows))]
    separator = '+-' + '-+-'.join('-' * width for width in column_widths) + '-+'
    header_row = '| ' + ' | '.join(f"{header:<{width}}" for header, width in zip(headers, column_widths)) + ' |'
    
    print(separator)
    print(header_row)
    print(separator)
    for row in rows:
        print('| ' + ' | '.join(f"{str(value):<{width}}" for value, width in zip(row, column_widths)) + ' |')
    print(separator)

# Fungsi untuk lihat data siswa
def view_students():
    while True:
        print("Lihat Data Siswa")
        print("1. Lihat Semua Data Siswa")
        print("2. Lihat Data Siswa Berdasarkan ID")
        print("3. Lihat Data Siswa Berdasarkan Nama")
        print("4. Lihat Data Siswa Berdasarkan Kelas")
        print("5. Kembali ke Menu Utama")
        choice = input("Pilih menu (1-5): ")
        print ("")
        if choice == '1':
            headers = list(students_data[0].keys())
            rows = [list(student.values()) for student in students_data]
            print_table(headers, rows)
            print ("")
        elif choice == '2':
            student_id = input("Masukkan ID Siswa: ")
            print ("")
            student_found = False
            for student in students_data:
                if student['ID'] == student_id:
                    headers = list(student.keys())
                    row = list(student.values())
                    print_table(headers, [row])
                    print ("")
                    student_found = True
                    break
            if not student_found:
                print("Data siswa tidak ditemukan.")
                print ("")
        elif choice == '3' :
            name = input("Masukkan nama siswa yang akan dicari: ").upper()
            print ("")
            matched_students = [student for student in students_data if name in student['NAMA'].upper()]
            if matched_students:
                headers = list(matched_students[0].keys())
                rows = [list(student.values()) for student in matched_students]
                print_table(headers, rows)
                print ("")
            else:
                print("Data siswa tidak ditemukan.")
                print ("")
        elif choice == '4':
            class_selected = select_option("Pilih kelas untuk melihat data siswa", kelas_options)
            print ("")
            matched_students = [student for student in students_data if student['KELAS'] == class_selected]
            if matched_students:
                headers = list(matched_students[0].keys())
                rows = [list(student.values()) for student in matched_students]
                print_table(headers, rows)
                print ("")
            else:
                print("Data siswa tidak ditemukan.")
                print ("")
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print ("")

# Fungsi untuk tambah data siswa
def add_student():
    while True:
        print("1. Masukkan Data Siswa")
        print("2. Kembali ke Menu Utama")
        choice = input("Pilih menu (1/2): ")
        print ("")
        if choice == '1':
            while True:
                student_id = input("Masukkan ID Siswa: ")
                if any(student['ID'] == student_id for student in students_data):
                    print("ID Siswa sudah ada. Masukkan ID yang berbeda.")
                    print ("")
                else:
                    break

            student = {
                'ID': student_id,
                'NAMA': input("Masukkan Nama Siswa: "),
                'KELAS': select_option("Pilih Kelas Siswa", kelas_options),
                'SEMESTER': select_option("Pilih Semester", semester_options),
                'MATEMATIKA': int(input("Masukkan Nilai Matematika: ")),
                'B INGGRIS': int(input("Masukkan Nilai Bahasa Inggris: ")),
                'IPA': int(input("Masukkan Nilai IPA: ")),
                'IPS': int(input("Masukkan Nilai IPS: ")),
                'SENI': int(input("Masukkan Nilai Seni: "))
            }
            
            print("\nData siswa yang Anda masukkan:")
            headers = list(student.keys())
            row = list(student.values())
            print_table(headers, [row])
            print ("")
            confirm = input("Apakah Anda ingin menyimpan data ini? (YES/NO): ").upper()
            print ("")
            
            if confirm == 'YES':
                students_data.append(student)
                print("Data siswa berhasil ditambahkan.")
                print ("")
            elif confirm == 'NO':
                print("Data siswa tidak disimpan.")
                print ("")
            else:
                print("PERINTAH YANG DIMASUKAN SALAH, MOHON ULANG KEMBALI")
                print ("")
        elif choice == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print ("")

# menampilkan daftar pilihan kepada user dan mengambil input user untuk memilih salah satu opsi dari daftar tersebut
def select_option(prompt, options):
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        choice = input(f"Pilih opsi (1-{len(options)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk update data siswa
def update_student():
    while True:
        print("1. Update Data Siswa")
        print("2. Kembali ke Menu Utama")
        choice = input("Pilih menu (1/2): ")
        print ("")
        if choice == '1':
            student_id = input("Masukkan ID Siswa yang akan diupdate: ")
            print ("")
            for student in students_data:
                if student['ID'] == student_id:
                    print("\nData siswa yang akan diupdate:")
                    headers = list(student.keys())
                    row = list(student.values())
                    print_table(headers, [row])
                    print ("")
                    print("Pilih data yang ingin diupdate:")
                    print("1. Nama")
                    print("2. Kelas")
                    print("3. Semester")
                    print("4. Nilai Matematika")
                    print("5. Nilai Bahasa Inggris")
                    print("6. Nilai IPA")
                    print("7. Nilai IPS")
                    print("8. Nilai Seni")
                    data_choice = input("Pilih data yang ingin diupdate (1-8): ")

                    if data_choice == '1':
                        student['NAMA'] = input(f"Nama ({student['NAMA']}): ") or student['NAMA']
                    elif data_choice == '2':
                        student['KELAS'] = select_option(f"Pilih Kelas ({student['KELAS']}): ", kelas_options)
                    elif data_choice == '3':
                        student['SEMESTER'] = select_option(f"Pilih Semester ({student['SEMESTER']}): ", semester_options)
                    elif data_choice == '4':
                        student['MATEMATIKA'] = int(input(f"Nilai Matematika ({student['MATEMATIKA']}): ") or student['MATEMATIKA'])
                    elif data_choice == '5':
                        student['B INGGRIS'] = int(input(f"Nilai Bahasa Inggris ({student['B INGGRIS']}): ") or student['B INGGRIS'])
                    elif data_choice == '6':
                        student['IPA'] = int(input(f"Nilai IPA ({student['IPA']}): ") or student['IPA'])
                    elif data_choice == '7':
                        student['IPS'] = int(input(f"Nilai IPS ({student['IPS']}): ") or student['IPS'])
                    elif data_choice == '8':
                        student['SENI'] = int(input(f"Nilai Seni ({student['SENI']}): ") or student['SENI'])
                    else:
                        print("Pilihan tidak valid.")
                        print ("")
                        continue

                    print("\nData siswa yang diupdate:")
                    headers = list(student.keys())
                    row = list(student.values())
                    print_table(headers, [row])

                    confirm = input("Apakah Anda ingin mengupdate data ini? (YES/NO): ").upper()
                    print ("")

                    if confirm == 'YES':
                        print("Data siswa berhasil diupdate.")
                        print ("")
                    elif confirm == 'NO':
                        print("Data siswa tidak diupdate.")
                        print ("")
                    else:
                        print("PERINTAH YANG DIMASUKAN SALAH, MOHON ULANG KEMBALI")
                        print ("")
                    return
            print("Data siswa tidak ditemukan.")
            print ("")
        elif choice == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print ("")

# Fungsi untuk hapus data siswa
def delete_student():
    while True:
        print("1. Hapus Data Siswa")
        print("2. Kembali ke Menu Utama")
        choice = input("Pilih menu (1/2): ")
        print ("")
        if choice == '1':
            student_id = input("Masukkan ID Siswa yang akan dihapus: ")
            print ("")
            for student in students_data:
                if student['ID'] == student_id:
                    print("Data siswa yang akan dihapus:")
                    print ("")
                    headers = list(student.keys())
                    row = list(student.values())
                    print_table(headers, [row])
                    print ("")
                    confirm = input("Apakah Anda yakin ingin menghapus data ini? (YES/NO): ").upper()
                    print ("")
                    if confirm == 'YES':
                        students_data.remove(student)
                        print("Data siswa berhasil dihapus.")
                        print ("")
                    elif confirm == 'NO':
                        print("Data siswa tidak dihapus.")
                        print ("")
                    else:
                        print("Pilihan tidak valid.")
                        print ("")
                    return
            print("Data siswa tidak ditemukan.")
            print ("")
        elif choice == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print ("")

# menghitung rata-rata nilai siswa dalam kelas yang dipilih dan menampilkan hasilnya
def calculate_average_score_per_student():
    class_selected = select_option("Pilih kelas untuk melihat rata-rata nilai siswa", kelas_options)
    print ("")
    for student in students_data:
        if student['KELAS'] == class_selected:
            scores = [value for key, value in student.items() if key in ['MATEMATIKA', 'B INGGRIS', 'IPA', 'IPS', 'SENI']]
            average_score = sum(scores) / len(scores)
            print(f"Rata-rata nilai {student['NAMA']} ({student['ID']}): {average_score:.2f}")
            print ("")

# menampilkan peringkat siswa dalam kelas tertentu berdasarkan rata-rata nilai dari beberapa mata pelajaran
def rank_students_by_class():
    class_selected = select_option("Pilih kelas untuk melihat peringkat siswa", kelas_options)
    class_students = [student for student in students_data if student['KELAS'] == class_selected]

    ranked_students = sorted(class_students, key=lambda x: sum([x[subject] for subject in ['MATEMATIKA', 'B INGGRIS', 'IPA', 'IPS', 'SENI']]) / 5, reverse=True)
    print(f"\nPeringkat Siswa untuk Kelas {class_selected}")
    headers = ['RANK'] + list(ranked_students[0].keys())
    rows = [[rank + 1] + list(student.values()) for rank, student in enumerate(ranked_students)]
    print_table(headers, rows)
    print('-' * 50)
    print("")

# mencari siswa berdasarkan nilai tertentu pada mata pelajaran yang dipilih
def search_students_by_score():
    while True:
        print("1. Cari Siswa dengan Nilai di Atas Angka Tertentu")
        print("2. Cari Siswa dengan Nilai di Bawah Angka Tertentu")
        print("3. Kembali ke Menu Utama")
        choice = input("Pilih menu (1/3): ")
        print("")

        if choice == '1':
            subject = select_option("Pilih mata pelajaran", ['MATEMATIKA', 'B INGGRIS', 'IPA', 'IPS', 'SENI'])
            score = int(input(f"Masukkan nilai minimum untuk {subject}: "))
            matched_students = [student for student in students_data if student[subject] >= score]
            if matched_students:
                headers = list(matched_students[0].keys())
                rows = [list(student.values()) for student in matched_students]
                print_table(headers, rows)
                print("")
            else:
                print(f"Tidak ada siswa dengan nilai {subject} di atas {score}.")
                print("")
        elif choice == '2':
            subject = select_option("Pilih mata pelajaran", ['MATEMATIKA', 'B INGGRIS', 'IPA', 'IPS', 'SENI'])
            score = int(input(f"Masukkan nilai maksimum untuk {subject}: "))
            matched_students = [student for student in students_data if student[subject] <= score]
            if matched_students:
                headers = list(matched_students[0].keys())
                rows = [list(student.values()) for student in matched_students]
                print_table(headers, rows)
                print("")
            else:
                print(f"Tidak ada siswa dengan nilai {subject} di bawah {score}.")
                print("")
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("")

# menampilkan rangkuman data siswa berdasarkan kelas yang dipilih oleh pengguna
def display_summary_data():
    class_selected = select_option("Pilih kelas untuk melihat rangkuman data", kelas_options)
    class_students = [student for student in students_data if student['KELAS'] == class_selected]

    if class_students:
        total_students = len(class_students)
        avg_scores = {subject: sum(student[subject] for student in class_students) / total_students for subject in ['MATEMATIKA', 'B INGGRIS', 'IPA', 'IPS', 'SENI']}
        
        print(f"\nRangkuman Data Kelas {class_selected}:")
        print(f"Jumlah Siswa: {total_students}")
        for subject, avg in avg_scores.items():
            print(f"Rata-rata {subject}: {avg:.2f}")
    else:
        print(f"Tidak ada data siswa untuk kelas {class_selected}.")
        print("")

# menampilkan nilai tertinggi dan terendah dari setiap mata pelajaran untuk siswa dalam kelas tertentu yang dipilih oleh user
def best_and_worst_scores_by_subject():
    class_selected = select_option("Pilih kelas untuk melihat nilai terbaik dan terburuk", kelas_options)
    class_students = [student for student in students_data if student['KELAS'] == class_selected]

    if class_students:
        print(f"\nNilai Terbaik dan Terburuk untuk Kelas {class_selected}")
        print("")
        subjects = ['MATEMATIKA', 'B INGGRIS', 'IPA', 'IPS', 'SENI']
        for subject in subjects:
            highest_student = max(class_students, key=lambda x: x[subject])
            lowest_student = min(class_students, key=lambda x: x[subject])
            print(f"{subject}:")
            print(f"  Nilai Tertinggi: {highest_student['NAMA']} ({highest_student['ID']}) dengan nilai {highest_student[subject]}")
            print(f"  Nilai Terendah: {lowest_student['NAMA']} ({lowest_student['ID']}) dengan nilai {lowest_student[subject]}")
        print('-' * 50)
        print("")
    else:
        print(f"Tidak ada data siswa untuk kelas {class_selected}.")
        print("")


if __name__ == "__main__":
    main()