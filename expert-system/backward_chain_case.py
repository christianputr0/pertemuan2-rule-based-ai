def bool_converter(option):
    if option.lower() == "Ya":
        return True
    elif option.lower() == "Tidak":
        return False
    else:
        raise Exception("Error.. Tolong pilih ya atau tidak!") 
    
#   input
hewan = ['singa jantan', 'macan tutul', 'orangutan', 'jerapah', 'panda', 'beruang']

nama = str(input("Pilih hewan berikut: ['singa jantan', 'macan tutul', 'orangutan', 'jerapah', 'panda', 'beruang']"))

if nama in hewan:
    bertaring = bool_converter(input("Apakah hewan tersebut bertaring? [YA / TIDAK]"))
    warna_bulu_berpola = bool_converter(input("Apakah hewan tersebut bulunya berpola? [YA / TIDAK]"))
    kepala_berbulu_lebat = bool_converter(input("Apakah hewan tersebut kepalanya berbulu lebat? [YA / TIDAK]"))
    berbulu_lebat = bool_converter(input("Apakah hewan tersebut berbulu lebat? [YA / TIDAK]"))
    berbulu_tipis = bool_converter(input("Apakah hewan tersebut berbulut tipis? [YA / TIDAK]"))
    makan_daging = bool_converter(input("Apakah hewan tersebut makan daging? [YA / TIDAK]"))
    makan_buah = bool_converter(input("Apakah hewan tersebut makan buah? [YA / TIDAK]"))
    berleher_panjang = bool_converter(input("Apakah hewan tersebut berleher panjang? [YA / TIDAK]"))
else:
    raise Exception("Error.. Tolong pilih ya atau tidak!")

if bertaring and kepala_berbulu_lebat and makan_daging:
    print("\nItu SINGA JANTAN")
elif bertaring and makan_daging and warna_bulu_berpola:
    print("\nItu MACAN TUTUL")
elif makan_buah and berbulu_lebat:
    print("\nItu ORANGUTAN")
elif makan_buah and berbulu_tipis and berleher_panjang and warna_bulu_berpola:
    print("\nItu JERAPAH")
elif berbulu_lebat and bertaring and warna_bulu_berpola and makan_buah:
    print("\nItu PANDA")
elif berbulu_lebat and bertaring and warna_bulu_berpola and makan_daging:
    print("\nItu BERUANG")

else:
    print("Tidak ditemukan!")
