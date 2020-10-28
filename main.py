import imdb

inpt = 'y'
while inpt == 'y' or inpt == 'Y':
    title = input('Enter name of movie or tv show: ')
    print(imdb.content_advisory(title))
    print('*' * 200)
    inpt = input('Do you wish to continue(y/n)? ')
