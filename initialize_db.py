import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS products (
    ad_no INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price REAL,
    city TEXT,
    image_url TEXT,
    category TEXT
)
''')

products = [
    ('Laptop', 'Yüksek performanslı oyun laptopu', 30000, 'Ankara', 'https://img-itopya.mncdn.com/cdn/1000/yeni-proje-2-8baaf7.jpg', 'Elektronik'),
    ('Tablet', 'Çocuklar için eğitim tableti', 5000, 'İzmir', 'https://www.jebinde.com/Content/ContentImage/638588970231139152-en-iyi-tablet-onerileri-2024.jpg', 'Elektronik'),
    ('Bebek Arabası', 'Hafif ve katlanabilir bebek arabası', 1500, 'İstanbul', 'https://file.babymall.com.tr/babymall/product/505x505/4b50851c84_maxi-cosi-lara2-super-hafif-katlanabilir-cabin-bebek-arabasi-essential-black.webp', 'Bebek'),
    ('Gitar', 'Elektro gitar, müzik tutkunları için ideal', 4500, 'İstanbul', 'https://img-zuhalmuzik.mncdn.com/mnresize/1000/1000/images/product/1155080144502506_1.jpg', 'Müzik'),
    ('Saat', 'Akıllı saat, sağlık takibi için', 8000, 'Ankara', 'https://www.segment.com.tr/images/productimages/EVER_FIT_W22_01.jpg', 'Aksesuar'),
    ('Drone', 'Havadan çekim için profesyonel drone', 12000, 'Antalya', 'https://www.drone.net.tr/images/thumbnails/1920/1416/detailed/7/Hubsan_E58X-2.png', 'Elektronik'),
    ('Bisiklet', 'Dağ bisikleti, sağlam ve hafif', 7500, 'İzmir', 'https://ideacdn.net/idea/em/27/myassets/products/764/tommybike-copper-aluminyum-kadro-29-jant-disk-fren-21-vites-dag-bisikleti-3959.jpeg?revision=1734335419', 'Spor'),
    ('Kamera', 'HD video çekim için kamera', 7000, 'Ankara', 'https://cdn.akakce.com/z/canon/canon-xa60b-4k-profesyonel.jpg', 'Elektronik'),
    ('Klavye', 'Mekanik oyun klavyesi', 1200, 'İstanbul', 'https://m.media-amazon.com/images/I/61c8DjYXCjL._AC_SL1500_.jpg', 'Elektronik'),
    ('Kedi Maması', 'Premium kedi maması, 5kg', 250, 'İzmir', 'https://m.media-amazon.com/images/I/61wTvEtG74L._AC_SL1218_.jpg', 'Evcil Hayvan'),
]


for product in products:
    conn.execute('INSERT INTO products (title, description, price, city, image_url, category) VALUES (?, ?, ?, ?, ?, ?)', product)

conn.commit()
conn.close()

db_path = conn.database
db_path
