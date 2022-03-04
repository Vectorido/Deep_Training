with open('C:/Users/Hurricane/Downloads/dataset_24465_4.txt', 'r', encoding='UTF-8') as f:
    s = f.read().split()[::-1]
    print(s)

with open('C:/Users/Hurricane/Downloads/new_dataset.txt', 'w', encoding='UTF-8') as of:
    for i in s:
        print(i, file=of, end='\n')

