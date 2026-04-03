# Online Sales Analysis

## Opis Projekta

Online Sales Analysis je Python aplikacija za upravljanje prodajom proizvoda. Omogućava kreiranje kataloga dostupnih proizvoda, upravljanje njihovim količinama i cenama, kao i stvaranje korpe za kupovinu sa kalkulacijom ukupne vrednosti.

---

## Klase

### 1. `Product`
Predstavlja jedan proizvod sa osnovnim podacima i operacijama.

**Atributi:**
- `name` (str) - Naziv proizvoda
- `price` (float) - Cena proizvoda
- `quantity` (int) - Raspoloživa količina

**Metode:**
- `display_info()` - Vraća string sa informacijama o proizvodu (naziv, cena, količina)
- `update_quantity(amount)` - Ažurira količinu proizvoda za dati iznos (može biti pozitivan ili negativan broj)

---

### 2. `ProductManager`
Upravlja kolekcijom dostupnih proizvoda u inventaru.

**Atributi:**
- `products` (list) - Lista svih dostupnih proizvoda

**Metode:**
- `add_product(product)` - Dodaje novi proizvod u inventar
- `display_all_products()` - Vraća formatiran string sa svim dostupnim proizvodima
- `display_total_value()` - Vraća ukupnu vrednost svih proizvoda u inventaru (cena × količina za svaki proizvod)
- `remove_product_by_name(name)` - Uklanja proizvod sa datim nazivom iz inventara (vraća `True` ako je uklonjen, `False` ako nije nađen)

---

### 3. `Cart`
Predstavlja kupčevu korpu za kupovinu.

**Atributi:**
- `cart_items` (list) - Lista proizvoda dodanih u korpu

**Metode:**
- `add_product(product)` - Dodaje proizvod u korpu
- `calculate_total()` - Vraća ukupnu vrednost za naplatu (zbir cena × količina za sve stavke u korpi)
- `display_cart()` - Vraća formatiran string sa svim stavkama u korpi

---

## Glavna Funkcionalnost

Program se izvršava kroz `main.py` fajl koji:

1. **Kreira ProductManager instancu** sa prilagođenim proizvodima (Laptop, Mouse, Keyboard, Monitor, Headphones)
2. **Prikazuje sve dostupne proizvode** i njihove informacije
3. **Izračunava ukupnu vrednost inventara**
4. **Kreira Cart instancu** i nasumično bira 3 proizvoda iz inventara
5. **Prikazuje sadržaj korpe** i **ukupnu vrednost za naplatu**

---

## Kako Pokrenuti

```bash
python main.py
```

---

## Izlaz Programa

Primer očekivanog izlaza:

```
All products:
Product: Laptop1, Price: 1200.0, Quantity: 5
Product: Mouse2, Price: 25.5, Quantity: 20
Product: Keyboard3, Price: 75.0, Quantity: 10
Product: Monitor4, Price: 250.0, Quantity: 7
Product: Headphones5, Price: 45.0, Quantity: 15

Total inventory value: 10457.5

Cart contents:
Product: Mouse2, Price: 25.5, Quantity: 20
Product: Monitor4, Price: 250.0, Quantity: 7
Product: Keyboard3, Price: 75.0, Quantity: 10

Cart total: 2285.0
```

---

## Struktura Projekta

```
online_sales_analysis/
├── product.py              # Klasa Product
├── product_manager.py      # Klasa ProductManager
├── cart.py                 # Klasa Cart
├── main.py                 # Glavna aplikacija
└── README.md               # Ova datoteka
```

---

## Tehnologije

- **Jezik:** Python 3.x
- **Standardi:** Bez eksternih zavisnosti
