class Flat:
    def __init__(self, ploshadi, price):
        self.ploshadi = ploshadi
        self.price = price

    def __eq__(self, other):
        return self.ploshadi == other.ploshadi

    def __ne__(self, other):
        return self.ploshadi != other.ploshadi

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def __str__(self):
        return f"Flat: ploshad={self.ploshadi}, Price={self.price}"

if __name__ == "__main__":
    kvartira1 = Flat(100, 200000)
    kvartira2 = Flat(120, 250000)

    print(kvartira1 == kvartira2)  
    print(kvartira1 != kvartira2)  
    print(kvartira1 < kvartira2)   
    print(kvartira1 > kvartira2)  
    print(kvartira1 <= kvartira2)  
    print(kvartira1 >= kvartira2)  
