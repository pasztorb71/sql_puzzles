DB_SOURCE_DATA = 'db_source_data/html_source.txt'
# forrás https://www.1st-art-gallery.com/most-popular-paintings.html?srsltid=AfmBOopPS1XNFA_Qvrd4HrikL0e6A--y6qcha5uEp3gc5WX_2VnutD9V

if __name__ == '__main__':
    with open(DB_SOURCE_DATA, 'r') as f:
        for line in f:
            if '<img class="hover:shadow-sm object-cover !w-full !h-full hidden md:block" loading="lazy" alt="' in line:
                print(line, end='')
                a = line.split('alt="Reproduction Oil Painting - ')[1].split(' - ')
                print(f'festo:{a[0]}')
                print(f'festmény:{a[1]}')
                if 'Gustav Klimt' in line:
                    break
