import glob
import os

working_dir = os.getcwd()
archives = glob.glob('*zip')


dirs = []

for n, manga in enumerate(archives):
    print(f"[{str(n).rjust(4,'0')}/{str(len(archives)).rjust(4,'0')}]")
    dir = manga.replace('.zip','').replace(' ','_')
    dirs.append(dir)
#   распаковываем архив и переходим в папку
    os.system(f"unzip \'{manga}\' -d \'{dir}\' > /dev/null")
    os.chdir(dir)
#   получаем содержимое папки в нормальном виде, в человекочиприятном порядке
    files = os.popen('ls | sort -V').read().split()
#   переименовываем все файлы чтобы они были в последовательном порядке
    for id, img in enumerate(files):
        res = img.split('.')[1]
        os.rename(img, f"{str(id).rjust(4,'0')}.{res}")
#   формируем пдф и удаляем временную папку
    os.chdir(working_dir)
    os.system(f"convert '{dir}/*' -quality 100 -monitor {dir}.pdf")
    
    os.rmdir(dir)
