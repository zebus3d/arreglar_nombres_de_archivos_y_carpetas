import os
import shutil
import subprocess

# El problema era que dentro de los archivos de final cut .fcpbundle hay unos enlaces simbolicos
# que apuntan al mismo directorio en el que estan. Esto el total commander se embucló copiando 
# por culpa de estos enlaces simbolicos. Lo que hago es borrar los .fcpcache que son los directorios recursivos y 
# volver a crear el enlace simbolico. 

# Para obtener los fc_proyects uso find /Volumes/Proyectos/ -iname "*.fcpbundle"
# fc_proyects = ["/Volumes/Proyectos//BKCF/LocucionesCallCenter/CALL CENTER BKT.fcpbundle","/Volumes/Proyectos//BKCF/Vídeo resumen Informe Anual/Material/Audio/Audio.fcpbundle","/Volumes/Proyectos//EDT Eventos/Fiesta Verano/AV/Final_Cut/Fiesta de verano.fcpbundle","/Volumes/Proyectos//EDT Eventos/VideoWall/01_AV/Final_Cut/EDT_Videowall.fcpbundle","/Volumes/Proyectos//Ferrovial/Directivos_Annual_Conference_AGROMAN/01_AV/Final_Cut/Directivos_AGROMAN.fcpbundle","/Volumes/Proyectos//Ferrovial/FerrovialServicios/Infografias/Infografias_Ferrovial_Servicios.fcpbundle","/Volumes/Proyectos//KATAMEDIA/RealMadrid/_Fc/CaseStudies_RM.fcpbundle","/Volumes/Proyectos//KATAMEDIA/RRSS_Katamedia/01_AV/Final_Cut/R.R.S.S..fcpbundle","/Volumes/Proyectos//KOTRA/190925_Kotra_2019_M00073/01_AV/Final_Cut/Kotra_2019.fcpbundle","/Volumes/Proyectos//LOCALE/Video_Corporativo/01_AV/Final_Cut/LOCALE_Video_Corporativo.fcpbundle","/Volumes/Proyectos//Real Madrid/Asamblea_Socios_2019/AV/Final_Cut/RM_Video_Demo_Asamblea_2019.fcpbundle","/Volumes/Proyectos//Real Madrid/Asamblea_Socios_2019_Expo/AV/_Fc/Real Madrid Asamblea.fcpbundle","/Volumes/Proyectos//Real Madrid/Asamblea_Socios_2019_Expo/AV/_Fc/Rm_Expor_Ajuste.fcpbundle","/Volumes/Proyectos//Real Madrid/Asamblea_Socios_2019_Expo/AV/_Fc/RM_zona4.fcpbundle","/Volumes/Proyectos//UST Global/191023_VideoManoFinanciero/01_AV/Final_Cut/Borrar/UST_GLOBAL.fcpbundle","/Volumes/Proyectos//UST Global/191023_VideoManoFinanciero/01_AV/Final_Cut/UST_GLOBAL.fcpbundle","/Volumes/Proyectos//Vídeos partido 24:8/Real Madrid partidos.fcpbundle"]

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
