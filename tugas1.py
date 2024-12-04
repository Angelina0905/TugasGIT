data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        
        }
    },
    'lokasi2': {
        'nama_lokasi':'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panenn': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 850,
            'kedelai': 550
        }
    }, 
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }

    }

}

print([data_panen])

print(data_panen['lokasi2']['hasil_panen']['jagung'])

print(data_panen['lokasi3']['nama_lokasi'])


lokasi1_padi = data_panen['lokasi1']['hasil_panen']['padi']
lokasi1_kedelai = data_panen['lokasi1']['hasil_panen']['kedelai']

lokasi2_padi = data_panen['lokasi2']['hasil_panen']['padi']
lokasi2_kedelai = data_panen['lokasi2']['hasil_panen']['kedelai']

lokasi3_padi = data_panen['lokasi3']['hasil_panen']['padi']
lokasi3_kedelai = data_panen['lokasi3']['hasil_panen']['kedelai']

lokasi4_padi = data_panen['lokasi4']['hasil_panen']['padi']
lokasi4_kedelai = data_panen['lokasi4']['hasil_panen']['kedelai']

lokasi5_padi = data_panen['lokasi5']['hasil_panen']['padi']
lokasi5_kedelai = data_panen['lokasi5']['hasil_panen']['kedelai']

# Mengelola kondisi setiap lokasi berdasarkan hasil panen
for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    
    # Mengatasi typo untuk lokasi3
    hasil_panen = data.get('hasil_panen', data.get('hasil_panenn', {}))
    
    padi = hasil_panen.get('padi', 0)
    jagung = hasil_panen.get('jagung', 0)
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {nama_lokasi} dalam kondisi baik.")

Angelina 
