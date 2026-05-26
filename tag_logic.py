import mysql.connector
db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "remindme"
)
def generate_auto_tags(text):

    keywords = {
        "#coding": ["python", "script", "code", "logic", "mysql"],
        "#materi": ["kuliah", "modul", "bab", "belajar", "dosen", "materi"],
        "#task" : ["tugas", "proyek", "deadline", "due", "kerjakan", "latihan", "kumpul"],
        "#reminder" :["jangan lupa", "ingat", "besok", "jadwal", "kuis"],
        "#notes" : ["catatan", "ide", "tanya"]
    }

    found_tags = []
    #chexk tags in text
    text = text.lower()
    for tag, words in keywords.items():
        for word in words:
            if word in text:
                found_tags.append(tag)
                break

    return found_tags

cursor=db.cursor()

input_user = input("what ur list?: ")
hasil_tags=generate_auto_tags(input_user)
print(input_user)
print(hasil_tags)

tags_string=".".join(hasil_tags)

sql = "INSERT INTO metadata_assets(title, tags) VALUE (%s, %s)"
tagdb = (input_user, tags_string)


try:
    
    cursor.execute(sql, tagdb)
    db.commit()
    print("Data sucessfully add")
except Exception as e:
    db.rollback()
    print(f"Failed to added data {e}")

cursor.close()
cursor =db.cursor()

print("DAFTAR SAYA")
sql_view = "SELECT id, title, tags from metadata_assets"

try :
    cursor.execute(sql_view)
    result = cursor.fetchall()

    if not result:
        print("Data is Empty")
    else:
        for row in result:
            print(f"ID: {row[0]} | judul: {row[1]} | Tags: {row[2]}")
            print("-"*30)
except Exception as b:
    print("failed to appear data :{b}")



#what if input not exuxt in tag
##buat perulangan, ini kau bikin aja yaaaaaa dari yang kalku itu.

id_hapus = input("\nMasukkan ID yang ingin dihapus : ")
sql_delete = "DELETE FROM metadata_assets WHERE id=%s"

try:
    cursor.execute(sql_delete, (id_hapus,))

    db.commit()
    print("Berhasil dihapus")

except Exception as e:
    db.rollback()
    print(f"gagal menghapus{e}")

cursor.close()