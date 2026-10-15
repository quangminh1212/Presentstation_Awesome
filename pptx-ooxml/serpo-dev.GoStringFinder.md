

Приложение для поиска строк текста внутри файлов и архивов.  


## 📌 Возможности  
- Рекурсивный обход директорий  
- Поддержка **текстовых и бинарных файлов**  
- Поиск внутри **архивов** различных форматов без их распаковки 
- Сохранение результатов в \`output.txt\`  

## 🔍 Поддерживаемые форматы  

### Архивы  
- .zip, .7z, .rar  

### Документы  
- .rtf, .txt, .html, .htm, .json, .md, .xml, .csv, .log
- .pdf 
- .doc, .xls, .ppt (OLE2-формат MS Office)
- .docx, .xlsx, .pptx (XML/ZIP-формат MS Office)





## ⚙️ Установка и запуск  

```
https://github.com/serpo-dev/GoStringFinder
cd GoStringFinder
go run ./cmd/main.go <путь_к_директории> <строка_поиска>
```

Пример:  

```
go run ./cmd/main.go . Греция
```

После выполнения поиска результаты будут сохранены в файл **output.txt**:  

```
Found results: 36
test/searchers/data/7z/test.7z/zip/doc/test.doc
test/searchers/data/7z/test.7z/zip/docx/test.docx
...
test/searchers/data/doc/test.doc
test/searchers/data/docx/test.docx
...
test/searchers/data/rar/test.rar/zip/doc/test.doc
test/searchers/data/rar/test.rar/zip/docx/test.docx
...
```

## 🗂️ Структура проекта  

```
string-finder/
├── cmd/             # Точка входа
├── internal/
│   ├── core/        # Логика обхода
│   ├── helpers/     # Вспомогательные функции
│   └── searchers/   # Поиск по архивам и файлам
├── test/            # Тесты
└── go.mod
```

## 🎬 Серия роликов на YouTube  

Этот проект был создан мною пошагово в серии из 12 выпусков.  

**👉 [Плейлист на YouTube](https://www.youtube.com/watch?v=wJuBCZr1eDo&list=PL6S9zzqgjYyhS2AVMaxBB8sWvu8rh6rIv)**  

```
Список названий серий:

1. Вступление (#0)
2. Архитектура проекта (#1)
3. Работа с DOCX-файлами (#2)
4. Работа с DOC-файлами (#3)
5. Работа с PPTX-файлами (#4)
6. Работа с PPT-файлами (#5)
7. Работа с XLSX-файлами (#6)
8. Работа с XLS-файлами (#7)
9. Работа с RTF и TXT-файлами (#8)
10. Работа с PDF-файлами (#9)
11. Работа с архивами ZIP, RAR, 7Z (#10)
12. Финальный выпуск (#11) 

```
