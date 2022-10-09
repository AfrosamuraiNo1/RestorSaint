import numpy as np
import multiprocessing as multi

def chunks(n, page_list):
    #"Разбивает список на n частей"""
    return np.array_split(page_list,n)
 
cpus = multi.cpu_count()
workers = []
page_list = ['www.website.com/page1.html', 'www.website.com/page2.html'
             'www.website.com/page3.html', 'www.website.com/page4.html']

page_bins = chunks(cpus, page_list)

print(page_bins)

# for cpu in range(cpus):
#     sys.stdout.write("CPU " + str(cpu) + "\n")
#     #Процесс, который будет отправлять соответствующий список страниц
#     # к функции execute_extraction
#     worker = multi.Process(name=str(cpu), 
#                            target=perform_extraction, 
#                            args=(page_bins[cpu],))
#     worker.start()
#     workers.append(worker)

 for worker in workers:
     worker.join()
    
# def perform_extraction(page_ranges):  #"""Извлекает данные, выполняет предварительную обработку, записывает данные"""
#     # делать запросы и BeautifulSoup
#     # предварительно обработать данные
#     file_name = multi.current_process().name+'.txt'
#     # write into current process file