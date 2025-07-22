from transformers import T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("cahya/t5-base-indonesian-summarization-cased")

text = "MODEL COCOMO Constructive Cost Model = Model Biaya Konstruktif) Tahap Perencanaan ( Estimasi) Model COCOMO Merupakan algoritma estimasi biaya perangkat lunak model yang dikembangkan oleh Barry Boehm. Model ini menggunakan rumus regresi dasar, dengan parameter yang berasal dari data historis dan karakteristik proyek saat ini. Person-month (PM) dianggap sebagai unit yang tepat untuk mengukur upaya, karena developer biasanya ditugaskan ke sebuah proyek selama beberapa bulan tertentu. Perlu dicatat bahwa perkiraan upaya 100 PM tidak berarti bahwa 100 orang harus bekerja selama 1 bulan. Asumsikan bahwa gaji rata-rata seorang developer perangkat lunak adalah Rp. 15.000.000 per bulan. Tentukan upaya yang diperlukan untuk mengembangkan produk perangkat lunak, waktu pengembangan nominal, dan biaya untuk mengembangkan produk. Kelemahan utama dari model COCOMO dasar dan menengah adalah bahwa mereka menganggap produk perangkat lunak sebagai satu kesatuan yang homogen. Namun, sebagian besar sistem besar terdiri dari beberapa sub-sistem yang lebih kecil. Sub-sistem ini seringkali memiliki karakteristik yang sangat berbeda."

tokens = tokenizer.tokenize(text)
id = tokenizer.convert_tokens_to_ids(tokens)

print("Kata:", tokens)
print("Angka:", id)
print("Jumlah token: ", len(id))