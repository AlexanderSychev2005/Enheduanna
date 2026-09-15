# Статистика корпуса (2026-09-15)

Посчитано напрямую из финального датасета (`data/processed/hf_dataset_documents_with_cdli_bulk`,
все три сплита train+validation+test вместе) и `data/processed/hf_dataset_vision`.
Не копировать вручную в другие файлы — при следующем изменении корпуса пересчитать заново
(см. скрипты в конце файла).

## Категории по головам: документы и фото

### Period (9 классов, 128 502 документа с меткой / 12 626 фото, из них 12 620 с меткой period)

| Категория | Документов | Фото |
|---|---|---|
| Ur III | 79 928 | 4 282 |
| Old Babylonian | 13 238 | 2 443 |
| Neo-Assyrian | 12 620 | 1 320 |
| Third Millennium | 12 315 | 2 063 |
| Old Assyrian | 2 614 | 947 |
| Middle Assyrian | 2 619 | 801 |
| Middle Babylonian | 2 123 | 346 |
| Neo-Babylonian | 1 389 | 69 |
| Late Antiquity | 1 656 | 196 |

Пропущено (нет метки): 22 306 документов (14.8%).

### Genre (6 классов, 121 424 документа с меткой)

| Категория | Документов | Фото |
|---|---|---|
| Administrative | 94 836 | 7 076 |
| Legal | 6 577 | 1 054 |
| Royal Inscriptions | 6 399 | 486 |
| Literary & Scholarly | 5 488 | 1 102 |
| Lexical | 4 523 | 280 |
| Letters | 3 601 | 1 030 |

Пропущено: 29 384 документа (19.5%).

### Language (4 класса, 117 009 документов с меткой)

| Категория | Документов | Фото |
|---|---|---|
| Sumerian | 95 000 | 5 847 |
| Akkadian | 19 986 | 2 894 |
| Peripheral/Other | 1 354 | 282 |
| Bilingual | 669 | 30 |

Пропущено: 33 799 документов (22.4%).

### Provenience (36 классов, 117 829 документов с меткой)

| Категория | Документов | Фото |
|---|---|---|
| Umma | 31 074 | 936 |
| Girsu | 22 172 | 923 |
| Puzriš-Dagan | 16 012 | 936 |
| Nineveh | 8 219 | 928 |
| Nippur | 7 492 | 934 |
| Ur | 5 666 | 797 |
| Assur | 3 471 | 937 |
| Kanesh | 2 469 | 941 |
| Irisagrig | 2 971 | 61 |
| Adab | 2 546 | 762 |
| Uruk | 2 017 | 253 |
| Sippar | 1 934 | 409 |
| Garšana | 1 792 | 510 |
| Nimrud | 1 500 | 312 |
| Ugarit | 1 196 | 1 |
| Isin | 1 011 | 153 |
| Babylon | 1 044 | 71 |
| Larsa | 696 | 230 |
| Ebla | 451 | 242 |
| Kisurra | 416 | 0 |
| Zabalam | 373 | 54 |
| Tuttul | 351 | 350 |
| Šuruppak | 304 | 305 |
| Kish | 305 | 198 |
| Ešnunna | 410 | 151 |
| Nuzi | 247 | 186 |
| Susa | 266 | 9 |
| Amarna | 196 | 197 |
| Nerebtum | 216 | 206 |
| Emar | 204 | 0 |
| Mari | 164 | 0 |
| Šaduppum | 182 | 4 |
| Huzirina | 127 | 0 |
| Persepolis | 113 | 34 |
| Pī-Kasî | 112 | 57 |
| Hattusa | 110 | 6 |

Пропущено: 32 979 документов (21.9%).

Примечание: Ugarit, Mari, Emar, Kisurra, Huzirina — 0 или почти 0 фото несмотря на добор в
одной из прошлых сессий (`backfill_class_balance_images.py`) — у CDLI просто нет больше фото
для этих классов сверх уже собранного (не баг, физический потолок доступности).

## Как выбирали 36 классов provenience (и 9 классов period)

Условие отбора — **не каталожный размер класса, а сколько документов реально осталось после
восстановления текста** (`map_provenience()`/`map_period()` в `prepare_hf_dataset.py`): кандидат
попадает в финальный список только если после нормализации и попытки достать транслитерацию из
всех источников (ORACC+CuneiML+CDLI-bulk+eBL) у него набралось **не менее 50 документов**. Это
отсекло кандидатов, у которых каталожная запись показывала тысячи табличек, а реальный текст
почти ни у одной не нашёлся:

- **Provenience:** несколько крупных по каталогу площадок (Ašnakkum, Lagash, Qattara и другие)
  упали до единиц или нуля документов после фильтра и были исключены.
- **Period:** Middle Hittite (в каталоге ~14.7k строк) дал всего 3 реальных документа; Proto-/
  Neo-/Middle Elamite дали 2/0/0 — все четыре исключены как period-кандидаты.

Итоговые 36 provenience и 9 period — это то, что осталось после этого фильтра, не произвольный
округлённый порог.

## Объём текста в корпусе

Полный нетронутый текст (без обрезки по `context_char_max`), все три сплита вместе.

| Единица | Значение |
|---|---|
| Документов | 150 808 |
| Символов | 53 026 927 (~53.0M) |
| Слов (по пробелам) | 8 085 959 (~8.1M) |
| Документов со знаками (`signs`) | 149 795 (99.3%) |
| Клинописных знаков | 14 657 585 (~14.7M) |
| WordPiece-токенов (mBERT, `bert-base-multilingual-cased`) | 27 332 669 (~27.3M) |

**Для сравнения:**
- Lazar et al. (2021): ~10 000 табличек, 1M слов, 2.3M знаков (ORACC).
- Aeneas / LED (Assael et al. 2025): 176 861 надписей, 16M символов.

Наш корпус теперь примерно в 15 раз больше Lazar et al. по числу документов, ~6.5x по объёму
слов и ~6.4x по числу знаков. Aeneas всё ещё больше по числу отдельных надписей (176.8k против
наших 150.8k), но по объёму текста мы его обходим почти в 3.3 раза (53.0M символов против 16M).

## Как пересчитать

```bash
# категории по головам (docs + photos)
uv run python -c "
import json
from collections import Counter
from datasets import load_from_disk

docs = load_from_disk('data/processed/hf_dataset_documents_with_cdli_bulk')
vis = load_from_disk('data/processed/hf_dataset_vision')
lc = json.load(open('data/processed/label_configs.json', encoding='utf-8'))

for head in ['period', 'genre', 'language', 'provenience']:
    labels = lc[head]['labels']
    doc_counts = Counter()
    for split in docs:
        for idx in docs[split][f'{head}_labels']:
            if idx != -100:
                doc_counts[labels[idx]] += 1
    img_counts = Counter()
    for split in vis:
        for val in vis[split][head]:
            if val in labels:
                img_counts[val] += 1
    print(f'=== {head} ===')
    for cls in labels:
        print(f'  {cls}: docs={doc_counts.get(cls, 0)} photos={img_counts.get(cls, 0)}')
"

# объём текста
uv run python -c "
from datasets import load_from_disk
from transformers import AutoTokenizer

ds = load_from_disk('data/processed/hf_dataset_documents_with_cdli_bulk')
tok = AutoTokenizer.from_pretrained(r'checkpoints_final_text/final_model', use_fast=True)

total_docs = total_chars = total_words = total_signs_docs = total_signs = 0
for split in ds:
    for row in ds[split]:
        text = row['text'] or ''
        total_docs += 1
        total_chars += len(text)
        total_words += len(text.split())
        if row['signs']:
            total_signs_docs += 1
            total_signs += len(row['signs'])
print(f'documents={total_docs} chars={total_chars} words={total_words} signs_docs={total_signs_docs} signs={total_signs}')

wp_total = 0
for split in ds:
    texts = ds[split]['text']
    for i in range(0, len(texts), 2000):
        batch = [t or '' for t in texts[i:i+2000]]
        enc = tok(batch, add_special_tokens=False)
        wp_total += sum(len(ids) for ids in enc['input_ids'])
print(f'wordpiece_tokens={wp_total}')
"
```
