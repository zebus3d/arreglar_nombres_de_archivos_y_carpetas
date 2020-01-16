import os
import sys
import re
import unicodedata


if len(sys.argv) == 2:
    rootdir = sys.argv[1]

    if rootdir[-1] != "/":
        rootdir = rootdir + "/"

    regex = '[^A-Za-z0-9._\-\/]'


    def strip_accents(text):
        try:
            text = unicode(text, 'utf-8')
        except NameError: # unicode is a default on python 3 
            pass
        text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
        return str(text)


    # acentos para carpetas:
    print("acentos para archivos")
    i = 1
    for folder, subs, files in os.walk(rootdir):
        new_folder_name = strip_accents(folder)
        # print("sin acento: ", new_folder_name)
        folder_matches = re.findall(regex, folder)
        if folder_matches:
            if folder.upper() != new_folder_name.upper():
                if folder.lower() != new_folder_name.lower():
                    if os.path.isdir(new_folder_name):
                        new_folder_name = new_folder_name + "_" + str(i)
                        os.rename(folder, new_folder_name)
                        i += 1
                    else:
                        # print("no existe el folder se renombra: ", new_folder_name)
                        os.rename(folder, new_folder_name)

    # acentos para archivos:
    print("acentos para archivos")
    for folder, subs, files in os.walk(rootdir):
        j = 1
        for filename in files:
            new_file_name = strip_accents(filename)
            file_matches = re.findall(regex, filename)
            if file_matches:
                fname, fextension = os.path.splitext(folder+filename)
                if filename.upper() != new_file_name.upper():
                    if filename.lower() != new_file_name.lower():
                        if os.path.isfile(folder+"/"+new_file_name):
                            new_file_name = new_file_name.replace( fextension, "_" + str(j) + fextension )
                            os.rename(folder+"/"+filename, folder+"/"+new_file_name)
                            j += 1
                        else:
                            # print("no existe el archivo, se renombra")
                            os.rename(folder+"/"+filename, folder+"/"+new_file_name)

    # caracteres especiales:
    print("Procesando carpetas en: ", rootdir)
    i = 1
    for folder, subs, files in os.walk(rootdir):
        folder_matches = re.findall(regex, folder)
        new_folder_name = re.sub(regex, "_", folder)
        if folder_matches:
            # print("new folder name: ", new_folder_name)
            if os.path.isdir(new_folder_name):
                # print("ya existe el folder se le suma 1:", new_folder_name + "_" + str(i))
                new_folder_name = new_folder_name + "_" + str(i)
                os.rename(folder, new_folder_name)
                i += 1
            else:
                # print("no existe el folder se renombra: ", new_folder_name)
                os.rename(folder, new_folder_name)

    print("Procesando archivos en: ", rootdir)
    for folder, subs, files in os.walk(rootdir):
        j = 1
        for filename in files:
            fname, fextension = os.path.splitext(folder+filename)
            file_matches = re.findall(regex, filename)
            new_file_name = re.sub(regex, "_", filename)
            if file_matches:
                if folder[-1] == "/":
                    folder = folder[:-1]
                # print(folder+"/"+new_file_name)
                # print("folder: ", folder)
                # print("new file name: ", new_file_name)
                if os.path.isfile(folder+"/"+new_file_name):
                    # print("ya existe se le suma 1:", new_file_name.replace( fextension, "_" + str(j) + fextension ) )
                    new_file_name_count = new_file_name.replace( fextension, "_" + str(j) + fextension )
                    os.rename(folder+"/"+filename, folder+"/"+new_file_name_count)
                    j += 1
                else:
                    # print("no existe el archivo, se renombra: ", folder+"/"+filename, folder+"/"+new_file_name)
                    os.rename(folder+"/"+filename, folder+"/"+new_file_name)
else:
    print("Help:\n$: python3 procesar_nombres.py Archivo_comprimido/")
