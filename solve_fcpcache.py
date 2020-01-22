import os
import shutil
import subprocess

# El problema era que dentro de los archivos de final cut .fcpbundle hay unos enlaces simbolicos
# que apuntan al mismo directorio en el que estan. Esto el total commander se embucló copiando 
# por culpa de estos enlaces simbolicos. Lo que hago es borrar los .fcpcache que son los directorios recursivos y 
# volver a crear el enlace simbolico. 

# Para obtener los fc_proyects uso find /Volumes/Proyectos/ -iname "*.fcpbundle"
# fc_proyects = ["/Volumes/Proyectos/LocucionesCallCenter/CALL CENTER.fcpbundle","/Volumes/Proyectos//Vídeo resumen Informe Anual/Material/Audio/Audio.fcpbundle","/Volumes/Proyectos//Fiesta Verano/AV/Final_Cut/Fiesta de verano.fcpbundle","/Volumes/Proyectos//VideoWall/01_AV/Final_Cut/Videowall.fcpbundle","/Volumes/Proyectos//Directivos_Annual_Conference/01_AV/Final_Cut/Directivos.fcpbundle","/Volumes/Proyectos//Infografias/Infografias.fcpbundle","/Volumes/Proyectos//_Fc/CaseStudies.fcpbundle","/Volumes/Proyectos//01_AV/Final_Cut/R.fcpbundle","/Volumes/Proyectos//01_AV/Final_Cut/Kot.fcpbundle","/Volumes/Proyectos//Video_Corporativo/01_AV/Final_Cut/Video_Corporativo.fcpbundle","/Volumes/Proyectos//Asamblea/AV/Final_Cut/Asamblea_2019.fcpbundle","/Volumes/Proyectos//Socios_2019_Expo/AV/_Fc/socios.fcpbundle","/Volumes/Proyectos//Asamblea_Expo/AV/_Fc/Expor_Ajuste.fcpbundle","/Volumes/Proyectos//Socios_2019_Expo/AV/_Fc/zona4.fcpbundle","/Volumes/Proyectos//01_AV/Final_Cut/Borrar/GLOBAL.fcpbundle","/Volumes/Proyectos//191023_VideoFinanciero/01_AV/Final_Cut/GLOBAL2.fcpbundle","/Volumes/Proyectos//Vídeos partido 24:8/partidos.fcpbundle"]

for fcp in fc_proyects:
    # print(fcp)
    # subprocess.run(["ls", "-al", fcp])
    # target_path = "/Users/EDICION5/test_fc/prueba.fcpbundle"
    target_path = fcp
    target_file = target_path+"/.fcpcache"
    exist = os.path.exists(target_file)
    if exist:
        print(target_file, "exist!")
        if os.path.islink(target_file):
            print("is already symlink")
            print(os.listdir(target_file)[0], "->", os.readlink(target_file))
        elif os.path.isdir(target_file):
            print("remove ", target_file, "...")
            shutil.rmtree(target_file)
            print("create symlink...")
            os.chdir(target_path)
            os.symlink(".", ".fcpcache")
        elif os.path.isfile(target_file):  
            print(target_file, "is a file")
    else:
        print(target_file, "Not exist!!!")
