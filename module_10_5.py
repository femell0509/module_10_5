from time import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        all_data += file.readlines() #запись файла в список построчно

filenames = [f'file {number}.txt' for number in range(1, 5)] # создания списка с названиями файлов
# time_start = time()
# for file in filenames:
#     read_info(file)
# time_finish = time()
# print(time_finish - time_start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool: # запуск 4 параллельных прцессов
        time_start = time()
        result = pool.map(read_info, filenames) # выполнение 4 параллельных процессов с файлами 
        time_finish = time()
        print(time_finish - time_start)
