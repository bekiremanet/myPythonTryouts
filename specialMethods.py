# www.diveintopython3.net

class books():
    def __init__(self,name,author,page):  # __init__ methodu tekrardan konfigüre edildi.
        self.name = name
        self.author = author
        self.page = page

book_1 = books("name", "author", "page")

print(book_1)  # Print fonksiyonu içerisindeki __str__ methodu düzenlenmedi !!!

class songs():
    def __init__(self,artist, duration, year):
        self.artist = artist
        self.duration = duration
        self.year = year

    def __str__(self):  # Print fonksiyonu içerisindeki __str__ methodu düzenlendi. !!!
        return "Artist: {}\nDuration: {}\nYear: {}".format(self.artist,self.duration,self.year)

    def __len__(self):  # Len fonksiyonu içerisindeki __len__ methodu tekrardan düzenlendi. !!! 
        return self.duration

song_1 = songs("Tarkan", 445, 1996)

print(song_1) 
print(len(song_1)) 




