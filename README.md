# Notes & Quiz Days 17 Purwadhika JCDS Module 2

Pada repo ini, saya akan menjelaskan project saya,

```
Bagaimana cara memanggil API dari web sportsdb.com. Dan secara langsung menyimpan ke dalam format .xlsx, .json dan .csv. 
```
Data yang kita ambil berdasarkan nama tim, dan kita akan mengekstrak nama pemain, posisi, usia dan negara asalnya.

## 1. Let's do the coding
```
import requests
import datetime as dt
import xlsxwriter
import json
import csv
```
kita import dulu library yang dibutuhkan.

```
team = input('Insert team name: ')
url_footbal = f'http://www.thesportsdb.com/api/v1/json/1/searchplayerszzz.php?t={team}'
data = requests.get(url_footbal)
players = data.json()['player']

header = ['player_name', 'position', 'age', 'nationality']
all_players = []
```
- Kita panggil API nya dengan mengosongi nama teamnya. Bisa dilihat di akhir link saya hanya ketik  `{team}` karena 'team' adalah hasil input dari user.

- Simpan data player dari `data.json()` dengan keys ['player']

- Buat dulu headernya, ini akan berfungsi untuk membuat xlsx, json dan csv

- Buat list kosong, untuk menampung data player yang kita butuhkan

```
for player in players:
    player_data = []
    player_data.append(player['strPlayer'])
    player_data.append(player['strPosition'])
    player_data.append(2019 - int(player['dateBorn'][:4]))
    player_data.append(player['strNationality'])
    all_players.append(player_data)
```

- Dari koding ini, kita mulai menata data yang sudah kita dapatkan, dan memasukkannya satu per satu ke dalam `all_players` list. Jangan lupa untuk membuat temporary list (di sini saya gunakan variable `player_data`. Ada di dalam for loops) untuk menyatukan data, sebelum ke list utama (`all_players`)

```
all_player_json = []
for i in range(len(all_players)):
    x = dict(zip(header, all_players[i]))
    all_player_json.append(x)
```
- Koding ini kita akan mulai untuk menyiapkan data untuk ditulis dalam format .json
- Buat list kosong `all_player_json`.
- Buat for loops untuk mengiterasi berdasarkan banyaknya (`len`) dari `all_player` list.
- zip `header` list dengan data `all_player` pada index i, dan ubah menjadi `dictionary`
- lalu tambahkan ke dalam `all_player_json` list

```
with open(f'{team}.json', 'w') as player_data:
    json.dump(all_player_json, player_data)

with open(f'{team}.csv', 'w', newline='') as csv_player:
    column = header
    y = csv.DictWriter(csv_player, fieldnames = column)
    y.writeheader()
    y.writerows(all_player_json[1:])
```
- Pada koding ini, saya akan langsung membuat 2 file langsung yaitu .json dan .csv, karena .csv sudah memiliki method `DictWriter` maka ini akan memudahkan kita mengubah data dari json ke csv.

```
union_data = []
union_data.append(header)
for data in all_players:
    union_data.append(data)
print(union_data)
data_xlsx = xlsxwriter.Workbook(f'{team}.xlsx')
sheet1 = data_xlsx.add_worksheet(f"{team}'s squad")
for i in range(len(union_data)):
    for j in range(len(header)):
        sheet1.write(i,j,union_data[i][j])
```
- Sedangkan pada koding ini saya mengubah data tadi ke dalam format .xlsx

** Kekurangan dari koding ini**
- Koding ini belum terotomatisasi jika ingin mengetahui umur pemain. Karena di sini saya hanya mengurangi tahun ini (2019), dengan tahun kelahiran si pemain.
- Error akan muncul jika tim tidak terdapat dalam API

Akan segera diupdate. Terimakasih.