# Prediction demo: text-only vs vision (provenience) model

7 hand-picked tablet(s) (`--tablet_ids`). Both models see the exact same masked positions per example (bold <strong>?</strong> shown at every chosen position, 15% of eligible tokens) -- differences in restoration come only from the two models' separately trained weights, not from the image itself (the image only reaches `provenience_head`, see module docstring). The metadata table's `provenience` row is where the image can actually change an answer.

## Example 1 — `P333901` (has photo: True)

**Original text (transliteration):**
> u₂ - la₂ / i - di₂ - i / i - nu - mi₃ a - di₂ - nu - ki - ni / 5diš ma - na ku₃ - babbar <strong>...</strong> <strong>x</strong> <strong>...</strong> <strong>x</strong> <strong>...</strong> <strong>...</strong> <strong>x</strong> da ša u₃ mu <strong>x</strong> i - li - im - ma eš₁₈ - dar - ba - aš₂ - ti₂

**Cuneiform (Unicode signs, whole document, not position-aligned to the text above):**
> 𒌑 𒊹 𒄿 𒑰 𒄿 𒉡 𒈨 𒀀 𒊹 𒉡 𒆠 𒉌 𒑰 𒐊 𒈠 𒈾 𒆬 𒌓 𒁕 𒊭 𒅇 𒈬 x 𒅎 𒈠 𒀹 𒁯 𒁀

**Masked input (10 positions):**
> u₂ - <strong>?</strong> <strong>?</strong> / <strong>?</strong> - di₂ - i / i - nu - mi₃ <strong>?</strong> - di₂ <strong>?</strong> nu <strong>?</strong> ki - ni / 5diš ma - na <strong>?</strong>₃ - babbar <strong>...</strong> <strong>x</strong> <strong>...</strong> <strong>x</strong> <strong>...</strong> <strong>...</strong> <strong>x</strong> da <strong>?</strong> u₃ mu <strong>x</strong> i - li - im - ma <strong>?</strong>₁₈ - dar - ba - aš₂ - ti <strong>?</strong>

### Restoration (masked-token predictions)

| # | true token | text-only top-1 | text-only top-3 | text-only top-5 | vision top-1 | vision top-3 | vision top-5 | text-only correct | vision correct | text-only top-3 hit | vision top-3 hit | text-only top-5 hit | vision top-5 hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `la` | `ma` | `ma`, `la`, `ṣ` | `ma`, `la`, `ṣ`, `mi`, `ul` | `la` | `la`, `mi`, `ma` | `la`, `mi`, `ma`, `ul`, `di` | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | `##₂` | `##₂` | `##₂`, `##₃`, `##m` | `##₂`, `##₃`, `##m`, `/`, `-` | `##₂` | `##₂`, `##₃`, `/` | `##₂`, `##₃`, `/`, `-`, `##m` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | `i` | `i` | `i`, `a`, `li` | `i`, `a`, `li`, `ni`, `id` | `i` | `i`, `a`, `na` | `i`, `a`, `na`, `ni`, `li` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4 | `a` | `i` | `i`, `a`, `li` | `i`, `a`, `li`, `ni`, `im` | `i` | `i`, `a`, `ni` | `i`, `a`, `ni`, `li`, `na` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 5 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `dumu`, `šu` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `dumu`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `dumu`, `igi` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `dumu`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | `ku` | `ku` | `ku`, `u`, `i` | `ku`, `u`, `i`, `tu`, `ša` | `ku` | `ku`, `u`, `i` | `ku`, `u`, `i`, `tu`, `ka` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 8 | `ša` | `-` | `-`, `/`, `da` | `-`, `/`, `da`, `##₃`, `a` | `-` | `-`, `/`, `##₃` | `-`, `/`, `##₃`, `a`, `ni` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 9 | `eš` | `eš` | `eš`, `aš`, `u` | `eš`, `aš`, `u`, `ša`, `nig` | `eš` | `eš`, `aš`, `u` | `eš`, `aš`, `u`, `du`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 10 | `##₂` | `##₂` | `##₂`, `##₃`, `-` | `##₂`, `##₃`, `-`, `ša`, `##₄` | `##₂` | `##₂`, `/`, `##₃` | `##₂`, `/`, `##₃`, `-`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Top-1 accuracy on this example: text-only 7/10 (70%), vision 8/10 (80%)

Top-3 accuracy on this example: text-only 9/10 (90%), vision 9/10 (90%)

Top-5 accuracy on this example: text-only 9/10 (90%), vision 9/10 (90%)

### Metadata predictions

| head | ground truth | text-only prediction | vision prediction |
|---|---|---|---|
| period | Old Assyrian | Old Assyrian (0.94) | Old Assyrian (0.96) |
| genre | (no label) | Letters (0.70) | Letters (0.73) |
| language | (no label) | Akkadian (0.92) | Akkadian (0.90) |
| provenience | Kanesh | Kanesh (0.95) | Kanesh (0.96) |

---

## Example 2 — `P357584` (has photo: True)

**Original text (transliteration):**
> um - ma puzur₄ - a - šur₃ - ma a - na wa - qa₂ - ar - tim qi₂ - bi - ma 1diš ma - na ku₃ - babbar ni - is - ha - su₂ diri ša - du - a - su₂ ša - bu ku - nu - ki - a a - šur - i - di₂ na - aš₂ - a - ki - im ṣu₂ - ba - tam₂ qa₂ - at - na - am ša tu₃ - še₂ - bi - li - ni ša ki - ma šu - wa - ti₂ ib - ši₂ - ma iš - ti₂ a - šur - i - di₂ še₂ - bi₄ - li - ma 1 / 2diš ma - na ku₃ - babbar lu - še₂ - bi₄ - la₂ - ki - im ša ṣu₂ - ba - tim pa₂ - na - am iš - te₂ - na - ma li - im - šu - ṭu₃ la i - qa₂ - tu - pu - šu šu - tu₃ - šu lu ma - da - at i - ṣe₂ - er pa₂ - ni - im ṣu₂ - ba - tim ša tu₃ - še₂ - bi₄ - li - ni ša - ap₂ - tam₂ 1diš ma - na - ta ra - di₂ - i - ma lu qa₂ - at - nu pa₂ - na - am ša - ni - a - am i - li - la li - im - šu - ṭu₃ šu - ma ša - ar - tam₂ i - ta - aš₂ - u₂ ki - ma ku - ta - nim li - iq - tu - pu - šu a - ba - ar - ni - a - am la ta - tu₃ - ri - ma ša ki - ma a - mi₃ - im la₂ tu₃ - še₂ - bi₄ - li - im šu - ma te₂ - pi₂ - ši₂ ša ki - ma a - ma - kam al - ta - ap₂ - tu₃ ep - ši₂ šu - ma ṣu - ba - ti₂ qa₂ - at - nu - tim la ta - ka₃ - ši₂ - di₂ a - ša - me - ma a - ma - kam a - ši₂ - mi₃ - im ma - du ša - mi₃ - ma še₂ - bi₄ - li - im ga

**Cuneiform (Unicode signs, whole document, not position-aligned to the text above):**
> 𒌝 𒈠 𒅤𒊭 𒀀 𒋓 𒈠 𒀀 𒈾 𒁀 𒂵 𒅈 𒁴 𒆠 𒁉 𒈠 𒁹 𒈠 𒈾 𒆬 𒌓 𒉌 𒄑 𒄩 𒍪 𒋛𒀀 𒊭 𒁺 𒀀 𒍪 𒊭 𒁍 𒆪 𒉡 𒆠 𒀀 𒀀 𒋩 𒄿 𒊹 𒈾 𒀾 𒀀 𒆠 𒅎 𒍪 𒁀 𒁮 𒂵 𒀜 𒈾 𒄠 𒊭 𒁺 𒋛 𒁉 𒇷 𒉌 𒊭 𒆠 𒈠 𒋗 𒁀 𒄭 𒅁 𒋛 𒈠 𒅖 𒄭 𒀀 𒋩 𒄿 𒊹 𒋛 𒁁 𒇷 𒈠 𒈦 𒈠 𒈾 𒆬 𒌓 𒇻 𒋛 𒁁 𒇲 𒆠 𒅎 𒊭 𒍪 𒁀 𒁴 𒁀 𒈾 𒄠 𒅖 𒄭 𒈾 𒈠 𒇷 𒅎 𒋗 𒁺 𒆷 𒄿 𒂵 𒌅 𒁍 𒋗 𒋗 𒁺 𒋗 𒇻 𒈠 𒁕 𒀜 𒄿 𒍣 𒅕 𒁀 𒉌 𒅎 𒍪 𒁀 𒁴 𒊭 𒁺 𒋛 𒁁 𒇷 𒉌 𒊭 𒀖 𒁮 𒁹 𒈠 𒈾 𒋫 𒊏 𒊹 𒄿 𒈠 𒇻 𒂵 𒀜 𒉡 𒁀 𒈾 𒄠 𒊭 𒉌 𒀀 𒄠 𒄿 𒇷 𒆷 𒇷 𒅎 𒋗 𒁺 𒋗 𒈠 𒊭 𒅈 𒁮 𒄿 𒋫 𒀾 𒌑 𒆠 𒈠 𒆪 𒋫 𒉏 𒇷 𒅅 𒌅 𒁍 𒋗 𒀀 𒁀 𒅈 𒉌 𒀀 𒄠 𒆷 𒋫 𒁺 𒊑 𒈠 𒊭 𒆠 𒈠 𒀀 𒈨 𒅎 𒇲 𒁺 𒋛 𒁁 𒇷 𒅎 𒋗 𒈠 𒄭 𒁉 𒋛 𒊭 𒆠 𒈠 𒀀 𒈠 𒄭𒁁 𒀠 𒋫 𒀖 𒁺 𒅁 𒋛 𒋗 𒈠 𒍮 𒁀 𒄭 𒂵 𒀜 𒉡 𒁴 𒆷 𒋫 𒂵 𒋛 𒊹 𒀀 𒊭 𒈨 𒈠 𒀀 𒈠 𒄭𒁁 𒀀 𒋛 𒈨 𒅎 𒈠 𒁺 𒊭 𒈨 𒈠 𒋛 𒁁 𒇷 𒅎 𒂵 𒄠 𒊏 𒄠 𒍪 𒁀 𒋫 𒄠 𒊭 𒄭 𒁉 𒋛 𒄭 𒋛 𒄿 𒈾 𒈨 𒁴 𒇻 𒌑 𒊒 𒊌 𒋗 𒊭 𒈠 𒉌 𒄿 𒈾 𒀀 𒈨 𒁴 𒇻 𒊒 𒁍 𒋗

**Masked input (76 positions):**
> um - ma puzur₄ - a - šur₃ - ma a - na wa - <strong>?</strong>a₂ - <strong>?</strong> - <strong>?</strong> qi₂ <strong>?</strong> <strong>?</strong> <strong>?</strong> <strong>?</strong> 1diš ma <strong>?</strong> na ku₃ - ba <strong>?</strong>r ni <strong>?</strong> is <strong>?</strong> ha - <strong>?</strong>₂ diri <strong>?</strong> - du - a - su₂ <strong>?</strong> - bu <strong>?</strong> - nu - ki <strong>?</strong> a a - šu <strong>?</strong> - i - di₂ na - aš₂ - a - ki - im ṣu₂ <strong>?</strong> ba - tam <strong>?</strong> qa₂ - at - na - <strong>?</strong> ša tu₃ <strong>?</strong> še₂ - <strong>?</strong> <strong>?</strong> li - ni ša ki - ma šu <strong>?</strong> <strong>?</strong> - ti <strong>?</strong> ib - ši₂ - ma iš - ti₂ a - šur - i - di₂ <strong>?</strong>₂ - bi₄ <strong>?</strong> li - ma <strong>?</strong> / 2diš <strong>?</strong> - na ku₃ - babbar lu - še₂ - bi₄ - la₂ - ki - im ša ṣ <strong>?</strong>₂ - ba - <strong>?</strong> pa₂ - na - am iš - te₂ - na <strong>?</strong> ma li - im - šu - ṭu₃ <strong>?</strong> i - <strong>?</strong> <strong>?</strong>₂ - tu <strong>?</strong> pu - šu šu - tu₃ - šu <strong>?</strong> ma - da - at <strong>?</strong> - ṣe₂ - er pa₂ - ni - im ṣu <strong>?</strong> <strong>?</strong> ba - tim ša <strong>?</strong>₃ - še₂ - bi₄ - <strong>?</strong> - ni ša <strong>?</strong> ap₂ - <strong>?</strong>₂ 1diš ma <strong>?</strong> na <strong>?</strong> ta ra <strong>?</strong> <strong>?</strong>₂ <strong>?</strong> <strong>?</strong> - ma <strong>?</strong> q <strong>?</strong> <strong>?</strong> - <strong>?</strong> <strong>?</strong> <strong>?</strong> pa₂ - na - am ša - ni - a - am i - li <strong>?</strong> la li - im <strong>?</strong> <strong>?</strong> - ṭu₃ <strong>?</strong> - ma ša - ar - tam₂ i - ta - aš₂ - u₂ ki - ma <strong>?</strong> <strong>?</strong> ta - nim li - iq <strong>?</strong> tu - pu - šu a <strong>?</strong> ba - ar - ni - a - am la ta - tu₃ - ri - ma ša ki - ma a - mi₃ - im la₂ tu₃ <strong>?</strong> še <strong>?</strong> - bi₄ - li - <strong>?</strong> šu - ma te₂ - pi₂ - ši <strong>?</strong> ša ki - ma a <strong>?</strong> ma - kam al - ta - ap₂ - tu₃ ep - ši <strong>?</strong> šu - ma ṣu - ba - <strong>?</strong>₂ qa₂ - at - nu - tim la ta - ka₃ - <strong>?</strong>₂ - di₂ a - <strong>?</strong> - me - ma a - ma - kam a - ši <strong>?</strong> - mi₃ - im ma - du ša - mi₃ - <strong>?</strong> še₂ - bi₄ - li - im ga

### Restoration (masked-token predictions)

| # | true token | text-only top-1 | text-only top-3 | text-only top-5 | vision top-1 | vision top-3 | vision top-5 | text-only correct | vision correct | text-only top-3 hit | vision top-3 hit | text-only top-5 hit | vision top-5 hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `q` | `q` | `q`, `ṣ`, `ṭ` | `q`, `ṣ`, `ṭ`, `ʾ`, `ḫ` | `q` | `q`, `ṣ`, `ṭ` | `q`, `ṣ`, `ṭ`, `dar`, `ʾ` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | `ar` | `a` | `a`, `ri`, `ra` | `a`, `ri`, `ra`, `ru`, `ar` | `a` | `a`, `ri`, `ar` | `a`, `ri`, `ar`, `bu`, `ru` | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| 3 | `tim` | `ma` | `ma`, `am`, `um` | `ma`, `am`, `um`, `ni`, `a` | `ma` | `ma`, `tim`, `im` | `ma`, `tim`, `im`, `a`, `am` | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| 4 | `-` | `-` | `-`, `.`, `##₂` | `-`, `.`, `##₂`, `/`, `+` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5 | `bi` | `bi` | `bi`, `da`, `a` | `bi`, `da`, `a`, `ba`, `du` | `bi` | `bi`, `da`, `ma` | `bi`, `da`, `ma`, `iš`, `du` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6 | `-` | `-` | `-`, `##₂`, `##₁` | `-`, `##₂`, `##₁`, `##₅`, `u` | `-` | `-`, `##₂`, `##₅` | `-`, `##₂`, `##₅`, `##₁`, `##₄` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | `ma` | `ma` | `ma`, `um`, `##₂` | `ma`, `um`, `##₂`, `am`, `im` | `ma` | `ma`, `um`, `im` | `ma`, `um`, `im`, `##₂`, `ni` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 8 | `-` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `/`, `+` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `/`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 9 | `##bba` | `##bba` | `##bba`, `bu`, `##b` | `##bba`, `bu`, `##b`, `-`, `##₂` | `##bba` | `##bba`, `-`, `##ppi` | `##bba`, `-`, `##ppi`, `bu`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 10 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `##r` | `-` | `-`, `##₂`, `##r` | `-`, `##₂`, `##r`, `##₃`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##₃`, `##i` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##₃`, `##i` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 12 | `su` | `su` | `su`, `ti`, `ab` | `su`, `ti`, `ab`, `tam`, `la` | `su` | `su`, `ti`, `la` | `su`, `ti`, `la`, `di`, `ab` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 13 | `ša` | `i` | `i`, `a`, `ha` | `i`, `a`, `ha`, `šu`, `ša` | `i` | `i`, `a`, `##₂` | `i`, `a`, `##₂`, `##₃`, `ha` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| 14 | `ša` | `a` | `a`, `li`, `ha` | `a`, `li`, `ha`, `hu`, `lu` | `a` | `a`, `li`, `ha` | `a`, `li`, `ha`, `šu`, `lu` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 15 | `ku` | `##₃` | `##₃`, `##r`, `##₂` | `##₃`, `##r`, `##₂`, `šu`, `ku` | `##₃` | `##₃`, `##r`, `##₂` | `##₃`, `##r`, `##₂`, `a`, `ku` | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| 16 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `.`, `:` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##₃`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 17 | `##r` | `##r` | `##r`, `##₂`, `##ar` | `##r`, `##₂`, `##ar`, `##₃`, `##l` | `##r` | `##r`, `##₂`, `##₃` | `##r`, `##₂`, `##₃`, `##ar`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 18 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 19 | `##₂` | `##₂` | `##₂`, `##₃`, `-` | `##₂`, `##₃`, `-`, `##m`, `##a` | `##₂` | `##₂`, `##₃`, `-` | `##₂`, `##₃`, `-`, `ša`, `##a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 20 | `am` | `am` | `am`, `tim`, `ma` | `am`, `tim`, `ma`, `ni`, `nim` | `ni` | `ni`, `ma`, `tim` | `ni`, `ma`, `tim`, `am`, `nim` | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| 21 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 22 | `bi` | `bi` | `bi`, `ba`, `bu` | `bi`, `ba`, `bu`, `be`, `li` | `bi` | `bi`, `ba`, `bu` | `bi`, `ba`, `bu`, `be`, `al` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 23 | `-` | `-` | `-`, `##₄`, `##₂` | `-`, `##₄`, `##₂`, `##₃`, `.` | `-` | `-`, `##₄`, `##₂` | `-`, `##₄`, `##₂`, `##₃`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 24 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `u`, `##l` | `-` | `-`, `/`, `u` | `-`, `/`, `u`, `šu`, `##r` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 25 | `wa` | `a` | `a`, `nu`, `ma` | `a`, `nu`, `ma`, `ut`, `wa` | `a` | `a`, `nu`, `ma` | `a`, `nu`, `ma`, `um`, `ur` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| 26 | `##₂` | `##₂` | `##₂`, `-`, `##₃` | `##₂`, `-`, `##₃`, `##m`, `##₄` | `##₂` | `##₂`, `##₃`, `-` | `##₂`, `##₃`, `-`, `##m`, `##₄` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 27 | `še` | `še` | `še`, `te`, `ši` | `še`, `te`, `ši`, `la`, `u` | `še` | `še`, `te`, `ši` | `še`, `te`, `ši`, `la`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 28 | `-` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `/`, `##₂` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 29 | `1` | `1` | `1`, `2`, `5` | `1`, `2`, `5`, `/`, `4` | `1` | `1`, `2`, `5` | `1`, `2`, `5`, `-`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 30 | `ma` | `ma` | `ma`, `a`, `ba` | `ma`, `a`, `ba`, `na`, `ki` | `ma` | `ma`, `a`, `ta` | `ma`, `a`, `ta`, `na`, `ki` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 31 | `##u` | `##u` | `##u`, `##a`, `##i` | `##u`, `##a`, `##i`, `##e`, `##ur` | `##u` | `##u`, `##i`, `##a` | `##u`, `##i`, `##a`, `##e`, `##ur` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 32 | `tim` | `tim` | `tim`, `am`, `nim` | `tim`, `am`, `nim`, `at`, `tam` | `tim` | `tim`, `am`, `nim` | `tim`, `am`, `nim`, `tam`, `im` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 33 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `a`, `##₃` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `a`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 34 | `la` | `ša` | `ša`, `la`, `lu` | `ša`, `la`, `lu`, `ki`, `-` | `ša` | `ša`, `la`, `lu` | `ša`, `la`, `lu`, `/`, `ki` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 35 | `q` | `q` | `q`, `ṣ`, `na` | `q`, `ṣ`, `na`, `ṭ`, `ša` | `na` | `na`, `q`, `ṣ` | `na`, `q`, `ṣ`, `ša`, `ṭ` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 36 | `##a` | `##i` | `##i`, `##a`, `pa` | `##i`, `##a`, `pa`, `##q`, `aš` | `##i` | `##i`, `##a`, `u` | `##i`, `##a`, `u`, `pa`, `la` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 37 | `-` | `-` | `-`, `##₃`, `##₂` | `-`, `##₃`, `##₂`, `##₄`, `.` | `-` | `-`, `##₃`, `##₂` | `-`, `##₃`, `##₂`, `/`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 38 | `lu` | `ša` | `ša`, `la`, `-` | `ša`, `la`, `-`, `/`, `##₂` | `ša` | `ša`, `la`, `-` | `ša`, `la`, `-`, `/`, `##₂` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 39 | `i` | `i` | `i`, `a`, `li` | `i`, `a`, `li`, `lu`, `e` | `i` | `i`, `a`, `li` | `i`, `a`, `li`, `ta`, `e` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 40 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##₅`, `-` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `-`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 41 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 42 | `tu` | `tu` | `tu`, `u`, `ti` | `tu`, `u`, `ti`, `ta`, `ka` | `tu` | `tu`, `u`, `ka` | `tu`, `u`, `ka`, `ta`, `ti` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 43 | `li` | `li` | `li`, `la`, `lu` | `li`, `la`, `lu`, `a`, `i` | `li` | `li`, `la`, `lu` | `li`, `la`, `lu`, `a`, `i` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 44 | `-` | `-` | `-`, `la`, `ša` | `-`, `la`, `ša`, `##₂`, `##₃` | `-` | `-`, `ša`, `##₂` | `-`, `ša`, `##₂`, `a`, `la` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 45 | `tam` | `la` | `la`, `tam`, `ti` | `la`, `tam`, `ti`, `qe`, `pa` | `ti` | `ti`, `la`, `tam` | `ti`, `la`, `tam`, `pi`, `qe` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 46 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `.`, `+` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `.`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 47 | `-` | `-` | `-`, `ša`, `la` | `-`, `ša`, `la`, `šu`, `a` | `-` | `-`, `ša`, `la` | `-`, `ša`, `la`, `šu`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 48 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `##m`, `##b` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `##m`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 49 | `di` | `bi` | `bi`, `pa`, `pi` | `bi`, `pa`, `pi`, `aš`, `di` | `pa` | `pa`, `di`, `pi` | `pa`, `di`, `pi`, `aš`, `ši` | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| 50 | `-` | `-` | `-`, `u`, `ša` | `-`, `u`, `ša`, `/`, `la` | `-` | `-`, `u`, `ša` | `-`, `u`, `ša`, `šu`, `ši` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 51 | `i` | `am` | `am`, `a`, `šu` | `am`, `a`, `šu`, `bi`, `um` | `a` | `a`, `ni`, `ki` | `a`, `ni`, `ki`, `am`, `šu` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 52 | `lu` | `ša` | `ša`, `la`, `-` | `ša`, `la`, `-`, `/`, `lu` | `ša` | `ša`, `la`, `/` | `ša`, `la`, `/`, `-`, `1diš` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| 53 | `##a` | `##a` | `##a`, `##i`, `##ab` | `##a`, `##i`, `##ab`, `##al`, `##u` | `##a` | `##a`, `##i`, `##ab` | `##a`, `##i`, `##ab`, `##al`, `##u` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 54 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##₅`, `-` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `-`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 55 | `at` | `bi` | `bi`, `a`, `ba` | `bi`, `a`, `ba`, `at`, `ti` | `a` | `a`, `bi`, `ti` | `a`, `bi`, `ti`, `ba`, `at` | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| 56 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `##a`, `##i` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `##a`, `u` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 57 | `nu` | `ma` | `ma`, `am`, `im` | `ma`, `am`, `im`, `um`, `tim` | `ma` | `ma`, `im`, `am` | `ma`, `im`, `am`, `ni`, `-` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 58 | `-` | `-` | `-`, `##₂`, `##m` | `-`, `##₂`, `##m`, `ša`, `##p` | `##₂` | `##₂`, `-`, `##m` | `##₂`, `-`, `##m`, `/`, `ša` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 59 | `-` | `-` | `-`, `.`, `la` | `-`, `.`, `la`, `/`, `:` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `la`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 60 | `šu` | `šu` | `šu`, `ša`, `ši` | `šu`, `ša`, `ši`, `aš`, `ku` | `šu` | `šu`, `pu`, `ša` | `šu`, `pu`, `ša`, `ku`, `ši` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 61 | `šu` | `šu` | `šu`, `ki`, `um` | `šu`, `ki`, `um`, `ša`, `a` | `ki` | `ki`, `šu`, `um` | `ki`, `šu`, `um`, `a`, `i` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 62 | `ku` | `a` | `a`, `at`, `iš` | `a`, `at`, `iš`, `ma`, `i` | `a` | `a`, `at`, `al` | `a`, `at`, `al`, `iš`, `i` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 63 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `ma`, `kam` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `ma`, `kam` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 64 | `-` | `-` | `-`, `.`, `##₂` | `-`, `.`, `##₂`, `:`, `/` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `/`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 65 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##₃`, `.` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##₃`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 66 | `-` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `/`, `##₂` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `##₂`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 67 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##₆`, `-` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##r`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 68 | `im` | `im` | `im`, `ni`, `a` | `im`, `ni`, `a`, `ma`, `šu` | `ni` | `ni`, `im`, `ma` | `ni`, `im`, `ma`, `a`, `nim` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 69 | `##₂` | `##₂` | `##₂`, `-`, `##m` | `##₂`, `-`, `##m`, `##b`, `##r` | `##₂` | `##₂`, `-`, `##m` | `##₂`, `-`, `##m`, `##b`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 70 | `-` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `/`, `:` | `-` | `-`, `.`, `##₂` | `-`, `.`, `##₂`, `/`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 71 | `##₂` | `-` | `-`, `##₂`, `##m` | `-`, `##₂`, `##m`, `##r`, `/` | `##₂` | `##₂`, `-`, `##m` | `##₂`, `-`, `##m`, `/`, `##b` | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 72 | `ti` | `tam` | `tam`, `ti`, `tim` | `tam`, `ti`, `tim`, `la`, `u` | `tam` | `tam`, `ti`, `tu` | `tam`, `ti`, `tu`, `tim`, `u` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 73 | `ši` | `la` | `la`, `aš`, `ab` | `la`, `aš`, `ab`, `pa`, `ši` | `la` | `la`, `aš`, `ap` | `la`, `aš`, `ap`, `pa`, `ab` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| 74 | `ša` | `ha` | `ha`, `na`, `ta` | `ha`, `na`, `ta`, `ša`, `nu` | `li` | `li`, `ta`, `ša` | `li`, `ta`, `ša`, `ha`, `na` | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| 75 | `##₂` | `##₂` | `##₂`, `##m`, `ša` | `##₂`, `##m`, `ša`, `##₄`, `a` | `##₂` | `##₂`, `##m`, `ša` | `##₂`, `##m`, `ša`, `##₄`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 76 | `ma` | `im` | `im`, `ma`, `a` | `im`, `ma`, `a`, `šu`, `am` | `im` | `im`, `ma`, `a` | `im`, `ma`, `a`, `tim`, `šu` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |

Top-1 accuracy on this example: text-only 55/76 (72%), vision 51/76 (67%)

Top-3 accuracy on this example: text-only 61/76 (80%), vision 64/76 (84%)

Top-5 accuracy on this example: text-only 70/76 (92%), vision 67/76 (88%)

### Metadata predictions

| head | ground truth | text-only prediction | vision prediction |
|---|---|---|---|
| period | Old Assyrian | Old Assyrian (0.95) | Old Assyrian (0.94) |
| genre | Letters | Letters (0.90) | Letters (0.87) |
| language | (no label) | Akkadian (0.92) | Akkadian (0.92) |
| provenience | Kanesh | Kanesh (0.94) | Kanesh (0.94) |

---

## Example 3 — `P297482` (has photo: True)

**Original text (transliteration):**
> a - na pu - šu - ke - en₆ qi₂ - bi - ma um - ma la₂ - ma - si₂ - ma 9diš tug₂ hi - a ku - lu - ma - a na - aš₂ - a - ku - um 3diš tug₂ hi - a i - di₂ - su₂ - en₆ na - aš₂ - a - kum e - la₂ tug₂ hi - a la₂ - qa₂ - a - am la₂ i - mu - a i - di₂ - su₂ - en₆ 5diš tug₂ hi - a la₂ - qa₂ - a - am la₂ i - mu - a mi₃ - šu ša ta - aš₂ - ta - na - pa₂ - ra - ni um - ma a - ta - ma tug₂ hi - a ša tu₃ - uš - te₂ - ne₂ - bi - li - ni la₂ dam - qu₂ / ma - nu - um za - ak - ru - um ša i - na e₂ - ka₃ wa - aš₂ - bu - ni - ma i - la₂ - ku - ma ma - ah - ri - šu / tug₂ hi - a u₂ - nu - hu - ni / a - na - ku a - šu - mi₃ i - na ha - ra - an ha - ra - ma ku₃ - babbar 1u gin₂ e₂ - ka₃ li - im - qu₂ - tam₂ tug₂ hi - a uš - te₂ - ka₃ - ap - ma e - pa₂ - aš - ma / u₂ - še₂ - ba - la₂ - kum

**Cuneiform (Unicode signs, whole document, not position-aligned to the text above):**
> 𒀀 𒈾 𒁍 𒋗 𒆠 𒅔 𒆠 𒁉 𒈠 𒌝 𒈠 𒇲 𒈠 𒍣 𒈠 𒐎 𒌆 𒄭 𒀀 𒆪 𒇻 𒈠 𒀀 𒈾 𒀾 𒀀 𒆪 𒌝 𒐈 𒌆 𒄭 𒀀 𒄿 𒊹 𒍪 𒅔 𒈾 𒀾 𒀀 𒄣 𒂊 𒇲 𒌆 𒄭 𒀀 𒇲 𒂵 𒀀 𒄠 𒇲 𒄿 𒈬 𒀀 𒄿 𒊹 𒍪 𒅔 𒐊 𒌆 𒄭 𒀀 𒇲 𒂵 𒀀 𒄠 𒇲 𒄿 𒈬 𒀀 𒈨 𒋗 𒊭 𒋫 𒀾 𒋫 𒈾 𒁀 𒊏 𒉌 𒌝 𒈠 𒀀 𒋫 𒈠 𒌆 𒄭 𒀀 𒊭 𒁺 𒍑 𒄭 𒉌 𒁉 𒇷 𒉌 𒇲 𒁮 𒆪 𒑰 𒈠 𒉡 𒌝 𒍝 𒀝 𒊒 𒌝 𒊭 𒄿 𒈾 𒂍 𒁀 𒀾 𒁍 𒉌 𒈠 𒄿 𒇲 𒆪 𒈠 𒈠 𒄴 𒊑 𒋗 𒑰 𒌆 𒄭 𒀀 𒌑 𒉡 𒄷 𒉌 𒑰 𒀀 𒈾 𒆪 𒀀 𒋗 𒈨 𒄿 𒈾 𒄩 𒊏 𒀭 𒄩 𒊏 𒈠 𒆬 𒌓 𒌋 𒂅 𒂍 𒌆 𒄭 𒀀 𒍑 𒄭 𒂵 𒀊 𒈠 𒂊 𒁀 𒀸 𒈠 𒑰 𒌑 𒋛 𒁀 𒇲 𒄣

**Masked input (52 positions):**
> a - na pu - šu - ke - en₆ <strong>?</strong>i₂ - bi - ma um - <strong>?</strong> la₂ - ma - si₂ - ma <strong>?</strong> <strong>?</strong> tu <strong>?</strong>₂ <strong>?</strong> - <strong>?</strong> ku <strong>?</strong> lu <strong>?</strong> ma - a na - <strong>?</strong>₂ - a - ku - um 3diš tug₂ <strong>?</strong> <strong>?</strong> a i - di₂ <strong>?</strong> su₂ - en₆ na - aš₂ - <strong>?</strong> - kum e - la <strong>?</strong> tu <strong>?</strong>₂ hi - a la₂ - qa₂ - a - am la₂ i - mu - a i - di <strong>?</strong> - su₂ - en₆ 5diš tug₂ hi - a la <strong>?</strong> - qa₂ - a - am la₂ i <strong>?</strong> mu - a mi₃ - <strong>?</strong> ša <strong>?</strong> - aš₂ - ta - na - pa₂ <strong>?</strong> ra <strong>?</strong> ni um - ma a - ta - ma tug₂ hi <strong>?</strong> <strong>?</strong> ša <strong>?</strong>₃ <strong>?</strong> uš <strong>?</strong> te₂ - ne₂ - bi - li - ni la₂ dam - <strong>?</strong>₂ / <strong>?</strong> - nu <strong>?</strong> um za - ak - ru - um ša i <strong>?</strong> <strong>?</strong> e₂ - ka₃ wa - aš₂ - bu - <strong>?</strong> <strong>?</strong> ma i - <strong>?</strong>₂ - <strong>?</strong> - ma ma - ah <strong>?</strong> ri - šu / tug₂ <strong>?</strong> - <strong>?</strong> u <strong>?</strong> - nu - hu - ni / <strong>?</strong> - na - ku a - šu - mi₃ i - na ha - ra - an ha - ra - <strong>?</strong> ku₃ - babbar 1u <strong>?</strong>₂ <strong>?</strong> <strong>?</strong> - ka₃ li - im - <strong>?</strong>₂ - tam₂ tug <strong>?</strong> <strong>?</strong> - a uš - te₂ - ka₃ - ap - ma e - pa₂ - <strong>?</strong> - ma / u₂ - še₂ <strong>?</strong> ba <strong>?</strong> la₂ - kum

### Restoration (masked-token predictions)

| # | true token | text-only top-1 | text-only top-3 | text-only top-5 | vision top-1 | vision top-3 | vision top-5 | text-only correct | vision correct | text-only top-3 hit | vision top-3 hit | text-only top-5 hit | vision top-5 hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `q` | `q` | `q`, `ṣ`, `ṭ` | `q`, `ṣ`, `ṭ`, `-`, `ŋ` | `q` | `q`, `ṣ`, `ṭ` | `q`, `ṣ`, `ṭ`, `K`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | `ma` | `ma` | `ma`, `mi`, `na` | `ma`, `mi`, `na`, `ta`, `bi` | `ma` | `ma`, `mi`, `ni` | `ma`, `mi`, `ni`, `ta`, `na` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | `9` | `/` | `/`, `1u`, `7` | `/`, `1u`, `7`, `-`, `8` | `/` | `/`, `1u`, `7` | `/`, `1u`, `7`, `-`, `5` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 4 | `##diš` | `1diš` | `1diš`, `3diš`, `2diš` | `1diš`, `3diš`, `2diš`, `##diš`, `5diš` | `##diš` | `##diš`, `##₂`, `ma` | `##diš`, `##₂`, `ma`, `2diš`, `5diš` | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| 5 | `##g` | `##g` | `##g`, `##l`, `##m` | `##g`, `##l`, `##m`, `la`, `##t` | `##g` | `##g`, `##m`, `##l` | `##g`, `##m`, `##l`, `##h`, `##d` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6 | `hi` | `hi` | `hi`, `ki`, `ha` | `hi`, `ki`, `ha`, `i`, `a` | `hi` | `hi`, `ki`, `a` | `hi`, `ki`, `a`, `ha`, `i` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | `a` | `a` | `a`, `na`, `i` | `a`, `na`, `i`, `ma`, `ni` | `a` | `a`, `na`, `i` | `a`, `na`, `i`, `ma`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 8 | `-` | `-` | `-`, `##₃`, `##m` | `-`, `##₃`, `##m`, `##₂`, `##₅` | `-` | `-`, `##m`, `##₃` | `-`, `##m`, `##₃`, `##₅`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 9 | `-` | `-` | `-`, `##m`, `/` | `-`, `##m`, `/`, `##₂`, `ša` | `##m` | `##m`, `-`, `/` | `##m`, `-`, `/`, `ša`, `3diš` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 10 | `aš` | `aš` | `aš`, `ap`, `ši` | `aš`, `ap`, `ši`, `di`, `pa` | `aš` | `aš`, `ši`, `ap` | `aš`, `ši`, `ap`, `di`, `pa` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11 | `hi` | `hi` | `hi`, `ki`, `ha` | `hi`, `ki`, `ha`, `i`, `hu` | `hi` | `hi`, `ki`, `ha` | `hi`, `ki`, `ha`, `hu`, `i` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 12 | `-` | `-` | `-`, `.`, `/` | `-`, `.`, `/`, `##₂`, `+` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `a`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 13 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `a` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 14 | `a` | `a` | `a`, `ta`, `ba` | `a`, `ta`, `ba`, `bu`, `ra` | `a` | `a`, `ba`, `bu` | `a`, `ba`, `bu`, `ta`, `ku` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 15 | `##₂` | `##₂` | `##₂`, `##m`, `-` | `##₂`, `##m`, `-`, `##₃`, `/` | `##₂` | `##₂`, `##m`, `##₃` | `##₂`, `##m`, `##₃`, `/`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 16 | `##g` | `##g` | `##g`, `##m`, `##l` | `##g`, `##m`, `##l`, `la`, `##š` | `##g` | `##g`, `##m`, `##l` | `##g`, `##m`, `##l`, `##d`, `##t` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 17 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##m`, `##b` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##m`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 18 | `##₂` | `##₂` | `##₂`, `##₃`, `##m` | `##₂`, `##₃`, `##m`, `-`, `##₄` | `##₂` | `##₂`, `##₃`, `##m` | `##₂`, `##₃`, `##m`, `-`, `##₄` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 19 | `-` | `-` | `-`, `.`, `##₃` | `-`, `.`, `##₃`, `+`, `:` | `-` | `-`, `.`, `##₃` | `-`, `.`, `##₃`, `:`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 20 | `šu` | `ma` | `ma`, `im`, `šu` | `ma`, `im`, `šu`, `ni`, `a` | `im` | `im`, `ma`, `šu` | `im`, `ma`, `šu`, `ni`, `a` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 21 | `ta` | `wa` | `wa`, `na`, `ta` | `wa`, `na`, `ta`, `ša`, `ha` | `wa` | `wa`, `na`, `ta` | `wa`, `na`, `ta`, `ha`, `ba` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 22 | `-` | `-` | `-`, `.`, `/` | `-`, `.`, `/`, `:`, `##₂` | `-` | `-`, `.`, `/` | `-`, `.`, `/`, `:`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 23 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `##₂`, `:` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `.`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 24 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `.`, `a` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `a`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 25 | `a` | `a` | `a`, `i`, `-` | `a`, `i`, `-`, `##a`, `na` | `a` | `a`, `i`, `-` | `a`, `i`, `-`, `##a`, `A` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 26 | `tu` | `tu` | `tu`, `ka`, `u` | `tu`, `ka`, `u`, `mi`, `ku` | `tu` | `tu`, `u`, `ka` | `tu`, `u`, `ka`, `mi`, `ku` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 27 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `lu`, `a` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `lu`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 28 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `ša`, `dumu` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `ša`, `dumu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 29 | `qu` | `qu` | `qu`, `ti`, `su` | `qu`, `ti`, `su`, `ši`, `la` | `qu` | `qu`, `la`, `si` | `qu`, `la`, `si`, `ti`, `ši` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 30 | `ma` | `a` | `a`, `ku`, `ma` | `a`, `ku`, `ma`, `šu`, `e` | `a` | `a`, `ku`, `ma` | `a`, `ku`, `ma`, `šu`, `i` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 31 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `##₂`, `:` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 32 | `-` | `-` | `-`, `##₃`, `##b` | `-`, `##₃`, `##b`, `##₂`, `##₇` | `-` | `-`, `##₃`, `##b` | `-`, `##₃`, `##b`, `##p`, `##₇` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 33 | `na` | `na` | `na`, `-`, `ša` | `na`, `-`, `ša`, `ta`, `ma` | `na` | `na`, `-`, `ša` | `na`, `-`, `ša`, `ta`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 34 | `ni` | `um` | `um`, `ni`, `šu` | `um`, `ni`, `šu`, `ur`, `ul` | `um` | `um`, `ni`, `šu` | `um`, `ni`, `šu`, `ur`, `ul` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 35 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##₃`, `:` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##m`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 36 | `la` | `di` | `di`, `la`, `pa` | `di`, `la`, `pa`, `ti`, `ši` | `di` | `di`, `la`, `pa` | `di`, `la`, `pa`, `ti`, `ši` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 37 | `ku` | `šu` | `šu`, `a`, `ak` | `šu`, `a`, `ak`, `ma`, `ku` | `šu` | `šu`, `a`, `ni` | `šu`, `a`, `ni`, `ah`, `ta` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| 38 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `:`, `##₂` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `:`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 39 | `hi` | `hi` | `hi`, `ha`, `ki` | `hi`, `ha`, `ki`, `i`, `a` | `hi` | `hi`, `ha`, `ki` | `hi`, `ha`, `ki`, `i`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 40 | `a` | `a` | `a`, `na`, `i` | `a`, `na`, `i`, `ma`, `ni` | `a` | `a`, `na`, `i` | `a`, `na`, `i`, `ni`, `ma` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 41 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##b`, `##h` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##b`, `##h` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 42 | `a` | `a` | `a`, `i`, `e` | `a`, `i`, `e`, `an`, `iš` | `a` | `a`, `i`, `an` | `a`, `i`, `an`, `ma`, `e` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 43 | `ma` | `an` | `an`, `am`, `ar` | `an`, `am`, `ar`, `ak`, `at` | `an` | `an`, `am`, `at` | `an`, `am`, `at`, `ar`, `ah` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 44 | `gin` | `gin` | `gin`, `la`, `gu` | `gin`, `la`, `gu`, `e`, `ma` | `gin` | `gin`, `la`, `gu` | `gin`, `la`, `gu`, `e`, `ma` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 45 | `e` | `e` | `e`, `-`, `la` | `e`, `-`, `la`, `i`, `u` | `e` | `e`, `-`, `u` | `e`, `-`, `u`, `i`, `la` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 46 | `##₂` | `##₂` | `##₂`, `ta`, `##₃` | `##₂`, `ta`, `##₃`, `na`, `šu` | `##₂` | `##₂`, `##₃`, `ta` | `##₂`, `##₃`, `ta`, `a`, `na` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 47 | `qu` | `qu` | `qu`, `ti`, `ši` | `qu`, `ti`, `ši`, `di`, `la` | `qu` | `qu`, `ti`, `la` | `qu`, `ti`, `la`, `ši`, `si` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 48 | `##₂` | `##₂` | `##₂`, `-`, `##₃` | `##₂`, `-`, `##₃`, `##₄`, `##₅` | `##₂` | `##₂`, `##₄`, `##₃` | `##₂`, `##₄`, `##₃`, `-`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 49 | `hi` | `hi` | `hi`, `ki`, `ha` | `hi`, `ki`, `ha`, `i`, `hu` | `hi` | `hi`, `ki`, `i` | `hi`, `ki`, `i`, `ha`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 50 | `aš` | `al` | `al`, `am`, `ar` | `al`, `am`, `ar`, `ra`, `a` | `al` | `al`, `ra`, `am` | `al`, `ra`, `am`, `ar`, `ni` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 51 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `.` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##₃`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 52 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##b`, `##₃` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##₃`, `##m` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Top-1 accuracy on this example: text-only 42/52 (81%), vision 42/52 (81%)

Top-3 accuracy on this example: text-only 47/52 (90%), vision 48/52 (92%)

Top-5 accuracy on this example: text-only 49/52 (94%), vision 48/52 (92%)

### Metadata predictions

| head | ground truth | text-only prediction | vision prediction |
|---|---|---|---|
| period | Old Assyrian | Old Assyrian (0.93) | Old Assyrian (0.93) |
| genre | Letters | Letters (0.89) | Letters (0.89) |
| language | Akkadian | Akkadian (0.92) | Akkadian (0.91) |
| provenience | Kanesh | Kanesh (0.92) | Kanesh (0.94) |

---

## Example 4 — `P358584` (has photo: True)

**Original text (transliteration):**
> a - na i - na - a qi₂ - bi - ma um - ma ta - ra - am - ku - bi - ma ta - aš₂ - pu - ra - am um - ma a - ta - ma ša - wi - ru - u₂ / u₃ a - nu - qu₂ - u₂ ša i - ba - ši₂ - u₂ - ni / ša - ṣi₂ - ri a - na a - ka₃ - li - ki / li - ib - ši₂ - u₂ ke - na - tim - ma 1 / 2diš ma - na ku₃ - sig₁₇ dingir - ba - ni / tu₃ - še₂ - bi - lam a - i - u₂ - tim ša - wi - ri ša te₂ - zi - ba - ni i - nu - mi₃ tu₃ - uṣ2 - u₂ ku₃ - babbar 1diš gin₂ u₂ - la₂ te₂ - zi - ba - am / e₂ - tam tu₃ - la₂ - qi₂ - it - ma / tu₃ - še₂ - ṣi₂ iš - tu₃ tu₃ - uṣ2 - u₂ - ni da - nu - tum bu - bu - tum i - na a - lim / u₃ - la₂ še - am 1diš sila₃ / te₂ - zi - ba - am / še - am a - na u₂ - kul₂ - ti₂ - ni / aš₂ - ta - na - am u₃ tap - hi - ra - am ša šu - ri - nam i - na it - <strong>...</strong> a - di₂ - in - ma lu - u₂ qa₂ - ti₂ - / ag - da - ma - ar u₃ a - na e₂ a - lim / a - na še - im <strong>x</strong> aš₂ ša a - da - da i - šu - u₂ - ma aš₂ - ta - qa₂ - al mi₃ - num / ri - ib - šu ša ta - aš₂ - ta - na - pa₂ - ra - ni a - na a - ka₃ - li - ni - i la₂ - šu / ne₂ - nu / ri - ib - ši₂ ne₂ - ta - na - pa₂ - aš₂ ša i - qa₂ - ti₂ - a ib - ši₂ - u₂ / u₂ - la₂ - qi₂ - it - ma uš - te

**Cuneiform (Unicode signs, whole document, not position-aligned to the text above):**
> 𒀀 𒈾 𒄿 𒈾 𒀀 𒆠 𒁉 𒈠 𒌝 𒈠 𒋫 𒊏 𒄠 𒆪 𒁉 𒈠 𒋫 𒀾 𒁍 𒊏 𒄠 𒌝 𒈠 𒀀 𒋫 𒈠 𒊭 𒉿 𒊒 𒌑 𒑰 𒅇 𒀀 𒉡 𒆪 𒌑 𒊭 𒄿 𒁀 𒋛 𒌑 𒉌 𒑰 𒊭 𒍣 𒊑 𒀀 𒈾 𒀀 𒂵 𒇷 𒆠 𒑰 𒇷 𒅁 𒋛 𒌑 𒆠 𒈾 𒁴 𒈠 𒈦 𒈠 𒈾 𒆬 𒄀 𒀭 𒁀 𒉌 𒑰 𒁺 𒋛 𒁉 𒇴 𒀀 𒄿 𒌑 𒁴 𒊭 𒉿 𒊑 𒊭 𒄭 𒍣 𒁀 𒉌 𒄿 𒉡 𒈨 𒁺 𒍑 𒌑 𒆬 𒌓 𒁹 𒂅 𒌑 𒇲 𒄭 𒍣 𒁀 𒄠 𒑰 𒂍 𒌓 𒁺 𒇲 𒆠 𒀉 𒑰 𒁺 𒋛 𒍣 𒅖 𒁺 𒁺 𒍑 𒌑 𒉌 𒁕 𒉡 𒌈 𒌈 𒄿 𒈾 𒀀 𒅆 𒆠 𒑰 𒅇 𒇲 𒊺 𒄠 𒁹 𒋡 𒑰 𒄭 𒍣 𒁀 𒄠 𒑰 𒊺 𒄠 𒀀 𒈾 𒌑 𒄢 𒄭 𒉌 𒑰 𒀾 𒋫 𒈾 𒄠 𒅇 𒋰 𒄭 𒊏 𒄠 𒊭 𒋗 𒊑 𒉆 𒄿 𒈾 𒀉 𒀀 𒊹 𒅔 𒈠 𒌑 𒂵 𒄭 𒑰 𒀝 𒁕 𒈠 𒅈 𒅇 𒀀 𒈾 𒂍 𒀀 𒅆 𒆠 𒑰 𒀀 𒈾 𒀾 𒀀 𒁕 𒁕 𒄿 𒋗 𒌑 𒈠 𒀾 𒋫 𒂵 𒀠 𒈨 𒉏 𒑰 𒊑 𒅁 𒋗 𒊭 𒋫 𒀾 𒋫 𒈾 𒁀 𒊏 𒉌 𒀀 𒈾 𒀀 𒂵 𒇷 𒉌 𒄿 𒇲 𒋗 𒑰 𒉌 𒉡 𒑰 𒊑 𒅁 𒋛 𒉌 𒋫 𒈾 𒁀 𒀾 𒊭 𒄿 𒂵 𒄭 𒀀 𒅁 𒋛 𒌑 𒑰 𒌑 𒇲 𒆠 𒀉 𒈠 𒍑 𒄭 𒁁 𒇲 𒄣 𒑰 𒌓 𒈠 𒄠 𒄿 𒁉 𒁴 𒑰 𒂊 𒊑 𒅎 𒑰 𒁀 𒀾 𒁀 𒆪 𒊭 𒌈 𒑰 𒊭 𒈾 𒀜 𒄿 𒄭 𒀉 𒈠 𒑰 𒈨 𒄴 𒊏 𒀜 𒍪 𒁀 𒄭 𒀀 𒑰 𒆬 𒌓 𒑰 𒄿 𒈾 𒄿 𒂵 𒄭 𒂵 𒈠 𒑰 𒄿 𒁀 𒋛 𒌑 𒋛 𒁁 𒇴 𒈠 𒑰 𒊺 𒄠 𒌋 𒀾 𒇲 𒀾 𒄠 𒑰 𒀀 𒋗 𒈨 𒑰 𒁾 𒁉 𒅎 𒊭 𒀀 𒋓 𒄿 𒈨 𒄭 𒌉 𒆪 𒊏 𒊭 𒋛 𒁁 𒑰 𒊭 𒂖 𒆠 𒌑 𒂍 𒁮 𒑰 𒌑 𒊭 𒄴 𒊹 𒅕 𒈠 𒀀 𒈠 𒁴 𒑰 𒌑 𒂵 𒄭 𒈠 𒊭 𒍪 𒍑 𒋫 𒂵 𒑰 𒀀 𒁀 𒁮 𒅅 𒈬 𒊒 𒈠 𒑛 𒈠 𒈾 𒆬 𒌓 𒀾 𒋫 𒃲 𒀀 𒊹 𒋫 𒇲 𒂵 𒉌 𒇲 𒄿 𒊏 𒂵 𒄠 𒑰 𒄿 𒈾 𒀀 𒇲 𒆠 𒂵 𒋫 𒋫 𒌑 𒁀 𒑰 𒈨 𒋗 𒌝 𒑰 𒋫 𒆠 𒇷 𒋫 𒀾 𒋫 𒈾 𒈨 𒈠 𒄭 𒅎 𒋫 𒁴 𒋫 𒀾

**Masked input (76 positions):**
> a - <strong>?</strong> i - na <strong>?</strong> a qi₂ - bi - ma um - ma ta - ra - am - ku - <strong>?</strong> <strong>?</strong> ma ta - <strong>?</strong>₂ - <strong>?</strong> - ra - am um - ma <strong>?</strong> - ta - ma ša - wi - ru <strong>?</strong> <strong>?</strong>₂ / <strong>?</strong>₃ a - nu - qu₂ <strong>?</strong> u₂ ša i - <strong>?</strong> - ši₂ <strong>?</strong> u₂ <strong>?</strong> ni / ša - ṣ <strong>?</strong>₂ <strong>?</strong> ri a - na <strong>?</strong> - ka <strong>?</strong> - li - <strong>?</strong> / li - ib - ši₂ <strong>?</strong> u₂ ke - na - tim - ma 1 / <strong>?</strong> <strong>?</strong> - na ku₃ - sig₁₇ dingir - ba - ni <strong>?</strong> tu₃ - še₂ - bi <strong>?</strong> la <strong>?</strong> a - i - u₂ - tim ša - wi - ri ša te₂ - zi <strong>?</strong> ba - ni i - nu - mi₃ tu <strong>?</strong> - uṣ2 - u₂ ku <strong>?</strong> - babbar 1diš <strong>?</strong>₂ u₂ - <strong>?</strong>₂ te₂ - zi <strong>?</strong> <strong>?</strong> - <strong>?</strong> <strong>?</strong> <strong>?</strong>₂ - tam tu₃ - <strong>?</strong>₂ <strong>?</strong> qi₂ - it <strong>?</strong> ma / tu₃ <strong>?</strong> še₂ - <strong>?</strong>i₂ iš <strong>?</strong> tu₃ tu₃ - uṣ2 - u₂ - <strong>?</strong> da <strong>?</strong> nu - tum bu - bu - tum i - na a - li <strong>?</strong> / u₃ - la₂ še - am <strong>?</strong> sila₃ / te₂ - zi <strong>?</strong> ba - am / <strong>?</strong> - am <strong>?</strong> - na u₂ - kul₂ - ti₂ <strong>?</strong> ni / aš₂ - <strong>?</strong> - na - am <strong>?</strong>₃ tap - <strong>?</strong> - ra - am ša šu - <strong>?</strong> - nam i - na it - <strong>...</strong> a - di <strong>?</strong> - <strong>?</strong> - ma lu - u₂ qa <strong>?</strong> - <strong>?</strong> <strong>?</strong> - / ag <strong>?</strong> da - ma - ar u₃ <strong>?</strong> - na e₂ a - lim / a - na še - im <strong>x</strong> aš <strong>?</strong> ša a - da - da i - šu - u₂ - ma aš₂ - ta - q <strong>?</strong>₂ - al mi₃ - num / <strong>?</strong> - ib - šu ša ta - aš₂ <strong>?</strong> ta - na - pa <strong>?</strong> - ra - ni a - na a - ka₃ - li <strong>?</strong> ni - <strong>?</strong> la₂ <strong>?</strong> šu <strong>?</strong> ne₂ - nu <strong>?</strong> ri - ib - ši₂ <strong>?</strong>₂ - ta - na - pa₂ - aš₂ ša i - qa₂ - ti₂ - a ib - <strong>?</strong> <strong>?</strong> - u <strong>?</strong> / u₂ - la₂ - qi₂ - it - <strong>?</strong> <strong>?</strong> - te

### Restoration (masked-token predictions)

| # | true token | text-only top-1 | text-only top-3 | text-only top-5 | vision top-1 | vision top-3 | vision top-5 | text-only correct | vision correct | text-only top-3 hit | vision top-3 hit | text-only top-5 hit | vision top-5 hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `na` | `na` | `na`, `ta`, `di` | `na`, `ta`, `di`, `a`, `ma` | `na` | `na`, `ta`, `di` | `na`, `ta`, `di`, `hi`, `ma` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `e`, `a` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `e`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | `bi` | `nu` | `nu`, `ni`, `um` | `nu`, `ni`, `um`, `nim`, `bi` | `nu` | `nu`, `um`, `ni` | `nu`, `um`, `ni`, `nim`, `ma` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| 4 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `+` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##m`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5 | `aš` | `aš` | `aš`, `pa`, `la` | `aš`, `pa`, `la`, `qu`, `ši` | `aš` | `aš`, `la`, `pa` | `aš`, `la`, `pa`, `di`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6 | `pu` | `pu` | `pu`, `ha`, `hu` | `pu`, `ha`, `hu`, `bu`, `šar` | `pu` | `pu`, `ha`, `bu` | `pu`, `ha`, `bu`, `bi`, `hu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | `a` | `a` | `a`, `at`, `ma` | `a`, `at`, `ma`, `aš`, `i` | `a` | `a`, `at`, `šu` | `a`, `at`, `šu`, `uš`, `aš` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 8 | `-` | `-` | `-`, `/`, `1diš` | `-`, `/`, `1diš`, `ša`, `##₂` | `-` | `-`, `1diš`, `/` | `-`, `1diš`, `/`, `ša`, `2diš` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 9 | `u` | `u` | `u`, `ti`, `qu` | `u`, `ti`, `qu`, `tam`, `su` | `u` | `u`, `tam`, `ti` | `u`, `tam`, `ti`, `pi`, `qu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 10 | `u` | `u` | `u`, `giri`, `tu` | `u`, `giri`, `tu`, `mi`, `ša` | `u` | `u`, `tu`, `ša` | `u`, `tu`, `ša`, `sila`, `ku` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11 | `-` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `##₂` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 12 | `ba` | `ba` | `ba`, `na`, `a` | `ba`, `na`, `a`, `ni`, `ša` | `ba` | `ba`, `na`, `nu` | `ba`, `na`, `nu`, `ša`, `i` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 13 | `-` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `+` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 14 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `:`, `+` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `:`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 15 | `##i` | `##u` | `##u`, `##e`, `##i` | `##u`, `##e`, `##i`, `##a`, `##ur` | `##e` | `##e`, `##i`, `##u` | `##e`, `##i`, `##u`, `##a`, `##ur` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 16 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `:`, `##₂` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 17 | `a` | `a` | `a`, `i`, `ta` | `a`, `i`, `ta`, `ša`, `šu` | `a` | `a`, `i`, `ta` | `a`, `i`, `ta`, `ša`, `li` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 18 | `##₃` | `##₃` | `##₃`, `##₂`, `##₄` | `##₃`, `##₂`, `##₄`, `##₅`, `-` | `##₃` | `##₃`, `##₂`, `##₄` | `##₃`, `##₂`, `##₄`, `##₅`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 19 | `ki` | `ni` | `ni`, `im`, `a` | `ni`, `im`, `a`, `e`, `i` | `ni` | `ni`, `nim`, `a` | `ni`, `nim`, `a`, `na`, `li` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 20 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `dumu`, `šu` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 21 | `2diš` | `2diš` | `2diš`, `3diš`, `6diš` | `2diš`, `3diš`, `6diš`, `2`, `1diš` | `2diš` | `2diš`, `3diš`, `6diš` | `2diš`, `3diš`, `6diš`, `1diš`, `2` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 22 | `ma` | `ma` | `ma`, `i`, `a` | `ma`, `i`, `a`, `na`, `ta` | `ma` | `ma`, `a`, `i` | `ma`, `a`, `i`, `na`, `ta` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 23 | `/` | `/` | `/`, `ša`, `-` | `/`, `ša`, `-`, `dumu`, `1diš` | `/` | `/`, `ša`, `-` | `/`, `ša`, `-`, `dumu`, `1diš` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 24 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##₄`, `ša` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##₄`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 25 | `##m` | `##₂` | `##₂`, `##m`, `/` | `##₂`, `##m`, `/`, `-`, `ša` | `##₂` | `##₂`, `##m`, `-` | `##₂`, `##m`, `-`, `/`, `##₃` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 26 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##₃`, `##b` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `##m` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 27 | `##₃` | `##₃` | `##₃`, `##₂`, `##₄` | `##₃`, `##₂`, `##₄`, `##₅`, `-` | `##₃` | `##₃`, `##₂`, `-` | `##₃`, `##₂`, `-`, `##₄`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 28 | `##₃` | `##₃` | `##₃`, `##₂`, `##₅` | `##₃`, `##₂`, `##₅`, `-`, `##m` | `##₃` | `##₃`, `##₂`, `##₅` | `##₃`, `##₂`, `##₅`, `-`, `##₄` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 29 | `gin` | `gin` | `gin`, `maš`, `la` | `gin`, `maš`, `la`, `gu`, `e` | `gin` | `gin`, `la`, `maš` | `gin`, `la`, `maš`, `sila`, `e` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 30 | `la` | `la` | `la`, `še`, `ti` | `la`, `še`, `ti`, `ab`, `su` | `la` | `la`, `še`, `ti` | `la`, `še`, `ti`, `di`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 31 | `-` | `-` | `-`, `##b`, `/` | `-`, `##b`, `/`, `##₃`, `##₂` | `-` | `-`, `##b`, `##₂` | `-`, `##b`, `##₂`, `/`, `##m` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 32 | `ba` | `ba` | `ba`, `bu`, `bi` | `ba`, `bu`, `bi`, `a`, `na` | `ba` | `ba`, `bi`, `bu` | `ba`, `bi`, `bu`, `a`, `i` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 33 | `am` | `ni` | `ni`, `am`, `na` | `ni`, `am`, `na`, `nu`, `a` | `ni` | `ni`, `am`, `a` | `ni`, `am`, `a`, `nu`, `na` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 34 | `/` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `q`, `ṣ` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `1diš`, `2diš` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 35 | `e` | `ši` | `ši`, `u`, `qu` | `ši`, `u`, `qu`, `aš`, `##a` | `u` | `u`, `qu`, `ši` | `u`, `qu`, `ši`, `aš`, `##a` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 36 | `la` | `la` | `la`, `še`, `le` | `la`, `še`, `le`, `li`, `ši` | `la` | `la`, `še`, `ša` | `la`, `še`, `ša`, `aš`, `li` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 37 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `##₂`, `dumu` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 38 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `a` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 39 | `-` | `-` | `-`, `/`, `a` | `-`, `/`, `a`, `:`, `la` | `-` | `-`, `/`, `a` | `-`, `/`, `a`, `:`, `la` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 40 | `ṣ` | `ṣ` | `ṣ`, `ṭ`, `q` | `ṣ`, `ṭ`, `q`, `ʾ`, `ḫ` | `ṣ` | `ṣ`, `q`, `ṭ` | `ṣ`, `q`, `ṭ`, `ʾ`, `ḫ` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 41 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `a`, `##₃` | `-` | `-`, `/`, `##kur` | `-`, `/`, `##kur`, `##₂`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 42 | `ni` | `ni` | `ni`, `tim`, `ma` | `ni`, `tim`, `ma`, `nim`, `a` | `ni` | `ni`, `tim`, `ma` | `ni`, `tim`, `ma`, `nim`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 43 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `/`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 44 | `##m` | `##m` | `##m`, `-`, `##₂` | `##m`, `-`, `##₂`, `/`, `##l` | `##m` | `##m`, `##₂`, `-` | `##m`, `##₂`, `-`, `##l`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 45 | `1diš` | `1diš` | `1diš`, `5diš`, `2diš` | `1diš`, `5diš`, `2diš`, `3diš`, `4diš` | `1diš` | `1diš`, `2diš`, `5diš` | `1diš`, `2diš`, `5diš`, `3diš`, `4diš` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 46 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `##b` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `##b` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 47 | `še` | `še` | `še`, `ša`, `ma` | `še`, `ša`, `ma`, `a`, `2diš` | `ša` | `ša`, `še`, `ma` | `ša`, `še`, `ma`, `a`, `ta` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 48 | `a` | `a` | `a`, `i`, `an` | `a`, `i`, `an`, `ma`, `ta` | `a` | `a`, `i`, `an` | `a`, `i`, `an`, `ma`, `ta` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 49 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `:`, `##₂` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 50 | `ta` | `ta` | `ta`, `ku`, `pu` | `ta`, `ku`, `pu`, `ma`, `šu` | `ta` | `ta`, `ku`, `šu` | `ta`, `ku`, `šu`, `ra`, `ma` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 51 | `u` | `u` | `u`, `ša`, `mi` | `u`, `ša`, `mi`, `tu`, `giri` | `u` | `u`, `tu`, `la` | `u`, `tu`, `la`, `ka`, `mi` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 52 | `hi` | `pu` | `pu`, `pa`, `ta` | `pu`, `pa`, `ta`, `ha`, `ru` | `pu` | `pu`, `pa`, `ta` | `pu`, `pa`, `ta`, `ha`, `tap` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 53 | `ri` | `a` | `a`, `na`, `mi` | `a`, `na`, `mi`, `ma`, `nu` | `na` | `na`, `a`, `i` | `na`, `a`, `i`, `ma`, `mi` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 54 | `##₂` | `##₂` | `##₂`, `a`, `##₃` | `##₂`, `a`, `##₃`, `##₄`, `i` | `##₂` | `##₂`, `a`, `##₃` | `##₂`, `a`, `##₃`, `šu`, `##₄` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 55 | `in` | `in` | `in`, `i`, `a` | `in`, `i`, `a`, `na`, `ni` | `in` | `in`, `im`, `um` | `in`, `im`, `um`, `i`, `ni` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 56 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `-`, `##₅` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `-`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 57 | `ti` | `ti` | `ti`, `bi`, `di` | `ti`, `bi`, `di`, `ab`, `tam` | `ti` | `ti`, `di`, `bi` | `ti`, `di`, `bi`, `tam`, `ab` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 58 | `##₂` | `##₂` | `##₂`, `##₃`, `a` | `##₂`, `##₃`, `a`, `i`, `##₄` | `##₂` | `##₂`, `##₃`, `a` | `##₂`, `##₃`, `a`, `i`, `##₄` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 59 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##rig`, `##₃` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##rig`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 60 | `a` | `a` | `a`, `i`, `an` | `a`, `i`, `an`, `ma`, `e` | `a` | `a`, `i`, `an` | `a`, `i`, `an`, `ma`, `e` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 61 | `##₂` | `##₂` | `##₂`, `-`, `##₃` | `##₂`, `-`, `##₃`, `/`, `##₄` | `##₂` | `##₂`, `-`, `##₃` | `##₂`, `-`, `##₃`, `##₄`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 62 | `##a` | `##a` | `##a`, `##i`, `##e` | `##a`, `##i`, `##e`, `##u`, `ša` | `##a` | `##a`, `##i`, `##u` | `##a`, `##i`, `##u`, `##e`, `##al` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 63 | `ri` | `li` | `li`, `ri`, `ni` | `li`, `ri`, `ni`, `ši`, `hi` | `li` | `li`, `ri`, `ši` | `li`, `ri`, `ši`, `ni`, `hi` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 64 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `+`, `la` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `##₂`, `dumu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 65 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##a`, `##m` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##₅`, `##ṭ` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 66 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##m`, `##₃` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##m`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 67 | `i` | `ma` | `ma`, `ni`, `im` | `ma`, `ni`, `im`, `šu`, `a` | `ma` | `ma`, `šu`, `im` | `ma`, `šu`, `im`, `ni`, `a` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 68 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `1diš`, `šu` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `1diš`, `la` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 69 | `/` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `ša`, `##₃` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `ša`, `##₃` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 70 | `/` | `/` | `/`, `-`, `ša` | `/`, `-`, `ša`, `dumu`, `##₂` | `/` | `/`, `-`, `ša` | `/`, `-`, `ša`, `dumu`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 71 | `ne` | `aš` | `aš`, `u`, `la` | `aš`, `u`, `la`, `ši`, `ap` | `u` | `u`, `aš`, `la` | `u`, `aš`, `la`, `ši`, `te` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 72 | `ši` | `la` | `la`, `ši`, `tu` | `la`, `ši`, `tu`, `bi`, `ṭ` | `ši` | `ši`, `la`, `tu` | `ši`, `la`, `tu`, `li`, `ša` | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 73 | `##₂` | `##₂` | `##₂`, `lu`, `##₃` | `##₂`, `lu`, `##₃`, `##₄`, `##u` | `##₂` | `##₂`, `##₃`, `lu` | `##₂`, `##₃`, `lu`, `##₄`, `##u` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 74 | `##₂` | `##₂` | `##₂`, `##b`, `##₃` | `##₂`, `##b`, `##₃`, `##h`, `-` | `##₂` | `##₂`, `##b`, `##₃` | `##₂`, `##b`, `##₃`, `-`, `##m` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 75 | `ma` | `ma` | `ma`, `ni`, `šu` | `ma`, `ni`, `šu`, `tim`, `a` | `ma` | `ma`, `ni`, `a` | `ma`, `ni`, `a`, `im`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 76 | `uš` | `iš` | `iš`, `i`, `##₂` | `iš`, `i`, `##₂`, `a`, `šu` | `iš` | `iš`, `i`, `##₂` | `iš`, `i`, `##₂`, `a`, `e` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

Top-1 accuracy on this example: text-only 61/76 (80%), vision 61/76 (80%)

Top-3 accuracy on this example: text-only 68/76 (89%), vision 68/76 (89%)

Top-5 accuracy on this example: text-only 69/76 (91%), vision 68/76 (89%)

### Metadata predictions

| head | ground truth | text-only prediction | vision prediction |
|---|---|---|---|
| period | Old Assyrian | Old Assyrian (0.92) | Old Assyrian (0.94) |
| genre | (no label) | Letters (0.93) | Letters (0.91) |
| language | (no label) | Akkadian (0.95) | Akkadian (0.96) |
| provenience | Kanesh | Kanesh (0.91) | Kanesh (0.94) |

---

## Example 5 — `P358585` (has photo: True)

**Original text (transliteration):**
> a - na i - na - a qi₂ - bi - ma um - ma ta - ra - am - ku - bi - ma a - wa - tam₂ / ša e₂ ku - ra ša tu₃ - wa - du - u₂ ta - bu - a - at / ku₃ - babbar iš - ti₂ pa₂ - nim - ma še₂ - bi - la₂ - ma / ṭup - pu - šu a - na e₂ - ti₂ - ka₃ li - ip - hu - ru lu - u₂ / ṭup - pu - um ša e₂ en - na - su₂ - en₆ / e₂ šu - be - lim pa₂ - qi₂ - id u₃ ṭup - pu - um ša e₂ ku - ra / puzur₂ - a - šur₃ u₃ - ka₃ - al / ku₃ - babbar i - na pa₂ - ni - ka₃ še₂ - bi - la₂ - ma / i - na e₂ ku - nu - ki - ka₃ li - ni - di₂ ku₃ - babbar a - na še₂ - bu - li - im mi₃ - ma / la₂ ta - pa₂ - la₂ - ah / ku₃ - babbar / a - na ša - na - at ku₃ - babbar še₂ - bi - la₂ - ma u₂ - ṭa₂ - tam₂ a - pa₂ - ni - ka₃ li - iš - pu - ku - ni - kum ba - pi₂ - ra - am ša e - pu - ša - ku - ni il₅ - te₂ - be - er / a - šu - mi₃ ša e₂ ku - ra puzur₂ - a - šur₃ a - šu - mi₃ - ka₃ / ip - la₂ - ah - ma um - ma ne₂ - nu - ma mi₃ - ma la₂ ta - pa₂ - la₂ - ah a - wa - tam₂ / ku - bu - us₂ - ma u₂ a - wi - lum₂ še₂ - ep - šu / a - na a - lim ki li - iq - ru - ba - am u₂ - sa₂ - li - šu - ma / a - wa - tam₂ ig - mu - ur a - pu - tum ki - ma ṭup - pa₂ - am ta - aš₂ - me - u₂

**Cuneiform (Unicode signs, whole document, not position-aligned to the text above):**
> 𒀀 𒈾 𒄿 𒈾 𒀀 𒆠 𒁉 𒈠 𒌝 𒈠 𒋫 𒊏 𒆪 𒈠 𒀀 𒉿 𒁮 𒑰 𒊭 𒂍 𒆪 𒊏 𒊭 𒁺 𒉿 𒁺 𒌑 𒋫 𒁍 𒀀 𒀜 𒑰 𒆬 𒌓 𒅖 𒄭 𒁀 𒉏 𒈠 𒋛 𒁉 𒇲 𒈠 𒑰 𒁾 𒁍 𒋗 𒀀 𒈾 𒂍 𒄭 𒂵 𒇷 𒅁 𒄷 𒊒 𒇻 𒌑 𒑰 𒁾 𒁍 𒌝 𒊭 𒂍 𒂗 𒈾 𒍪 𒅔 𒑰 𒂍 𒋗 𒁁 𒅆 𒁀 𒆠 𒀉 𒅇 𒁾 𒁍 𒌝 𒊭 𒂍 𒆪 𒊏 𒑰 𒀀 𒋓 𒅇 𒂵 𒀠 𒑰 𒆬 𒌓 𒄿 𒈾 𒁀 𒉌 𒂵 𒋛 𒁉 𒇲 𒈠 𒑰 𒄿 𒈾 𒂍 𒆪 𒉡 𒆠 𒂵 𒇷 𒉌 𒄭 𒆬 𒌓 𒀀 𒈾 𒋛 𒁍 𒇷 𒅎 𒈨 𒈠 𒑰 𒇲 𒋫 𒁀 𒇲 𒄴 𒑰 𒆬 𒌓 𒑰 𒀀 𒈾 𒊭 𒈾 𒀜 𒆬 𒌓 𒋛 𒁉 𒇲 𒈠 𒌑 𒁮 𒀀 𒁀 𒉌 𒂵 𒇷 𒅖 𒁍 𒆪 𒉌 𒄣 𒁀 𒁉 𒊏 𒄠 𒊭 𒂊 𒁍 𒊭 𒆪 𒉌 𒂖 𒄭 𒁁 𒅕 𒑰 𒀀 𒋗 𒈨 𒊭 𒂍 𒆪 𒊏 𒀀 𒋓 𒀀 𒋗 𒈨 𒂵 𒑰 𒅁 𒇲 𒄴 𒈠 𒌝 𒈠 𒉌 𒉡 𒈠 𒈨 𒈠 𒇲 𒋫 𒁀 𒇲 𒄴 𒀀 𒉿 𒁮 𒑰 𒆪 𒁍 𒍑 𒈠 𒌑 𒀀 𒉿 𒅆 𒋛 𒅁 𒋗 𒑰 𒀀 𒈾 𒀀 𒅆 𒆠 𒇷 𒅅 𒊒 𒁀 𒄠 𒌑 𒁲 𒇷 𒋗 𒈠 𒑰 𒀀 𒉿 𒁮 𒅅 𒈬 𒌨 𒀀 𒁍 𒌈 𒆠 𒈠 𒁾 𒁀 𒄠 𒋫 𒀾 𒈨 𒌑 𒑰 𒀠 𒄰 𒈠 𒂊 𒅔 𒑰 𒀀 𒋓 𒑰 𒀭 𒂵 𒅇 𒄿 𒇷 𒁁 𒄭 𒅗 𒀀 𒈬 𒌨 𒑰 𒌑 𒀀 𒄭 𒑰 𒁀 𒀠 𒆪 𒉌 𒂊 𒉌 𒂵 𒇲 𒈬 𒌨 𒑰 𒁺 𒇻 𒌝 𒀀 𒈾 𒇷 𒁁 𒉌 𒂊 𒋫 𒊏 𒀊 𒑰 𒆠 𒋫 𒄠 𒑰 𒌑 𒅖 𒊏 𒄠 𒀀 𒈾 <D> 𒈥 𒌅 𒅎 𒊭 𒌉 𒋗 𒆪 𒁉 𒅎 𒌒 𒇲 𒉌 𒑰 𒄿 𒈾 𒂍 𒁾 𒁀 𒄠 𒑰 𒋛 𒁉 𒇲 𒋗 𒈠 𒑰 𒆠 𒋫 𒀀 𒄠 𒅇 𒅖 𒊏 𒄠 𒑰 𒇷 𒄭 𒅔 𒈠 𒑰 𒄿 𒈾 𒁉 𒄭 𒂵 𒑰 𒇷 𒁉 𒋛 𒑰 𒀀 𒋗 𒈨 𒑰 𒄠 𒁴 𒀀 𒋓 𒁖 𒇲 𒆪 𒅖 𒁍 𒊏 𒈠 𒄿 𒈾 𒁾 𒁁 𒋗 𒑚 𒈠 𒈾 𒆬 𒌓 𒀀 𒈾 𒂊 𒇲 𒉌 𒌉 𒋗 𒆪 𒁁 𒅎 𒀀 𒄭 𒅔 𒑰 𒄠 𒁮 𒑰 𒋗 𒌒 𒊑 𒁮 𒇷 𒅖 𒀀 𒈠 𒆠 𒅎 𒌉 𒋗 𒆪 𒁁 𒅎 𒑰 𒀾 𒀠 𒈠 𒌝 𒈠 𒋗 𒌓 𒈠 𒆬 𒌓 𒀀 𒋓 𒁖 𒇲 𒆪 𒇲 𒄿 𒄭 𒉆 𒁾 𒁀 𒄠 𒋛 𒁁 𒇲 𒋗 𒈠 𒑰 𒄠 𒁮 𒇷 𒅖 𒀀 𒄠 𒉌 𒀀 𒄭 𒁉 𒁮 𒊭 𒄭 𒄭 𒂍 𒄭 𒉌 𒑰 𒂵 𒊏 𒁁 𒂊 𒀀 𒋓 𒅖 𒀀 𒈠 𒄣 𒊭 𒂍 𒈾 𒂵 𒊑 𒅎 𒂵 𒇲 𒋗 𒄿 𒇲 𒆠 𒈠 𒑰 𒅖 𒄭 𒁀 𒉏 𒈠 𒑰 𒌑 𒋛 𒁀 𒇲 𒄣

**Masked input (76 positions):**
> <strong>?</strong> - na i - na - a qi₂ <strong>?</strong> bi <strong>?</strong> ma um - ma ta - ra - am - ku - bi - ma a - wa - tam₂ / <strong>?</strong> e₂ ku - ra ša <strong>?</strong>₃ - <strong>?</strong> - du - u <strong>?</strong> <strong>?</strong> - bu - a - at <strong>?</strong> ku₃ <strong>?</strong> babbar iš - ti₂ pa₂ - <strong>?</strong> - <strong>?</strong> <strong>?</strong> <strong>?</strong> - bi - la <strong>?</strong> - ma <strong>?</strong> ṭup - pu - šu a - na e₂ - ti₂ - ka₃ li - <strong>?</strong> <strong>?</strong> - hu - ru lu - u <strong>?</strong> / ṭup - pu - um ša e₂ en - na - <strong>?</strong>₂ - en <strong>?</strong> / <strong>?</strong>₂ šu - be - lim pa₂ - qi₂ - id u <strong>?</strong> ṭup - pu - um <strong>?</strong> e₂ ku - ra / puzur <strong>?</strong> - a - šur₃ <strong>?</strong>₃ <strong>?</strong> ka₃ - al <strong>?</strong> ku₃ <strong>?</strong> <strong>?</strong> <strong>?</strong>r i - na <strong>?</strong>₂ - ni - ka₃ še₂ - bi - la₂ - ma / i - na e₂ ku - nu - ki - ka₃ li - ni - di₂ ku₃ - babbar a - na še <strong>?</strong> - bu - <strong>?</strong> - im <strong>?</strong>₃ <strong>?</strong> ma <strong>?</strong> la₂ ta - pa₂ - <strong>?</strong>₂ - ah / ku₃ <strong>?</strong> <strong>?</strong>bbar / a <strong>?</strong> na <strong>?</strong> - <strong>?</strong> - at <strong>?</strong> <strong>?</strong> - babbar še₂ - bi - la₂ <strong>?</strong> ma u₂ - ṭa₂ - tam₂ a - pa₂ - ni - <strong>?</strong>₃ li - iš <strong>?</strong> <strong>?</strong> - ku - ni - kum ba - <strong>?</strong> <strong>?</strong> - ra - <strong>?</strong> ša e - pu - ša - ku - ni il₅ - te₂ - be - er / a - šu <strong>?</strong> <strong>?</strong>₃ <strong>?</strong> e₂ ku - ra puzur₂ - a - šur₃ a - šu - mi₃ - ka <strong>?</strong> / ip <strong>?</strong> la₂ - ah <strong>?</strong> ma um - ma ne₂ <strong>?</strong> nu - <strong>?</strong> mi₃ - ma <strong>?</strong>₂ ta - pa₂ - la₂ - ah a <strong>?</strong> wa - tam₂ / ku - bu <strong>?</strong> us₂ - ma u₂ a <strong>?</strong> wi <strong>?</strong> lum₂ še₂ - ep <strong>?</strong> šu / a - <strong>?</strong> a - lim ki li - iq - ru - ba - am u₂ <strong>?</strong> sa₂ <strong>?</strong> li - šu - ma / a - wa - tam₂ ig - mu - <strong>?</strong> <strong>?</strong> <strong>?</strong> pu <strong>?</strong> tum ki - ma ṭup - pa₂ - <strong>?</strong> ta - aš <strong>?</strong> - me - <strong>?</strong>₂

### Restoration (masked-token predictions)

| # | true token | text-only top-1 | text-only top-3 | text-only top-5 | vision top-1 | vision top-3 | vision top-5 | text-only correct | vision correct | text-only top-3 hit | vision top-3 hit | text-only top-5 hit | vision top-5 hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `a` | `a` | `a`, `i`, `an` | `a`, `i`, `an`, `um`, `ma` | `a` | `a`, `i`, `an` | `a`, `i`, `an`, `ma`, `um` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `+` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | `-` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `/`, `:` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `.`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4 | `ša` | `ša` | `ša`, `/`, `dumu` | `ša`, `/`, `dumu`, `1diš`, `2diš` | `ša` | `ša`, `/`, `dumu` | `ša`, `/`, `dumu`, `ma`, `3diš` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5 | `tu` | `ka` | `ka`, `tu`, `sa` | `ka`, `tu`, `sa`, `pi`, `mi` | `ka` | `ka`, `tu`, `sa` | `ka`, `tu`, `sa`, `pi`, `mi` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 6 | `wa` | `ba` | `ba`, `šu`, `na` | `ba`, `šu`, `na`, `ri`, `ra` | `ba` | `ba`, `ra`, `bu` | `ba`, `ra`, `bu`, `šu`, `ab` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 7 | `##₂` | `##₂` | `##₂`, `##₃`, `##b` | `##₂`, `##₃`, `##b`, `##h`, `##q` | `##₂` | `##₂`, `##₃`, `##b` | `##₂`, `##₃`, `##b`, `/`, `##h` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 8 | `ta` | `a` | `a`, `ku`, `ha` | `a`, `ku`, `ha`, `i`, `li` | `a` | `a`, `ha`, `ku` | `a`, `ha`, `ku`, `li`, `šu` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 9 | `/` | `/` | `/`, `ša`, `-` | `/`, `ša`, `-`, `dumu`, `##₂` | `/` | `/`, `ša`, `dumu` | `/`, `ša`, `dumu`, `##₂`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 10 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `+` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11 | `nim` | `ni` | `ni`, `li`, `ri` | `ni`, `li`, `ri`, `ra`, `a` | `ni` | `ni`, `ri`, `li` | `ni`, `ri`, `li`, `ra`, `na` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 12 | `ma` | `am` | `am`, `im`, `tim` | `am`, `im`, `tim`, `ma`, `šu` | `am` | `am`, `im`, `tim` | `am`, `im`, `tim`, `šu`, `ma` | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| 13 | `še` | `še` | `še`, `-`, `##₂` | `še`, `-`, `##₂`, `ša`, `te` | `še` | `še`, `##₂`, `-` | `še`, `##₂`, `-`, `te`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 14 | `##₂` | `##₂` | `##₂`, `##₃`, `a` | `##₂`, `##₃`, `a`, `še`, `##₄` | `##₂` | `##₂`, `##₃`, `a` | `##₂`, `##₃`, `a`, `še`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 15 | `##₂` | `##₂` | `##₂`, `##m`, `##₃` | `##₂`, `##m`, `##₃`, `-`, `##₄` | `##₂` | `##₂`, `##m`, `##₃` | `##₂`, `##m`, `##₃`, `-`, `##₄` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 16 | `/` | `/` | `/`, `ša`, `lu` | `/`, `ša`, `lu`, `dumu`, `la` | `/` | `/`, `ša`, `lu` | `/`, `ša`, `lu`, `dumu`, `la` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 17 | `i` | `i` | `i`, `iš`, `ša` | `i`, `iš`, `ša`, `a`, `im` | `i` | `i`, `iš`, `ṭ` | `i`, `iš`, `ṭ`, `a`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 18 | `##p` | `##₂` | `##₂`, `##h`, `##p` | `##₂`, `##h`, `##p`, `##a`, `##b` | `##₂` | `##₂`, `##₃`, `##a` | `##₂`, `##₃`, `##a`, `##h`, `##p` | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| 19 | `##₂` | `##₂` | `##₂`, `##b`, `##₃` | `##₂`, `##b`, `##₃`, `##h`, `##q` | `##₂` | `##₂`, `##b`, `##₃` | `##₂`, `##b`, `##₃`, `##h`, `##q` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 20 | `su` | `su` | `su`, `še`, `be` | `su`, `še`, `be`, `ne`, `he` | `su` | `su`, `be`, `ne` | `su`, `be`, `ne`, `še`, `he` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 21 | `##₆` | `##₆` | `##₆`, `##₈`, `##₃` | `##₆`, `##₈`, `##₃`, `##₇`, `##₅` | `##₆` | `##₆`, `##₈`, `##₃` | `##₆`, `##₈`, `##₃`, `##₅`, `##₇` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 22 | `e` | `e` | `e`, `la`, `u` | `e`, `la`, `u`, `ti`, `di` | `la` | `la`, `e`, `u` | `la`, `e`, `u`, `lu`, `ša` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 23 | `##₃` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##b`, `-` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `-`, `##b` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 24 | `ša` | `ša` | `ša`, `/`, `-` | `ša`, `/`, `-`, `dumu`, `1diš` | `ša` | `ša`, `/`, `-` | `ša`, `/`, `-`, `dumu`, `ki` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 25 | `##₂` | `##₂` | `##₂`, `##₄`, `##₃` | `##₂`, `##₄`, `##₃`, `##2`, `##₅` | `##₂` | `##₂`, `##₄`, `##₃` | `##₂`, `##₄`, `##₃`, `##₅`, `##2` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 26 | `u` | `ka` | `ka`, `mi`, `tu` | `ka`, `mi`, `tu`, `u`, `sa` | `ka` | `ka`, `mi`, `tu` | `ka`, `mi`, `tu`, `u`, `i` | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| 27 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `la`, `na` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `la`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 28 | `/` | `/` | `/`, `ša`, `##₂` | `/`, `ša`, `##₂`, `-`, `##₃` | `/` | `/`, `ša`, `##₂` | `/`, `ša`, `##₂`, `-`, `ki` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 29 | `-` | `-` | `-`, `.`, `/` | `-`, `.`, `/`, `:`, `a` | `-` | `-`, `.`, `/` | `-`, `.`, `/`, `:`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 30 | `ba` | `ba` | `ba`, `bi`, `-` | `ba`, `bi`, `-`, `BA`, `ku` | `ba` | `ba`, `bi`, `na` | `ba`, `bi`, `na`, `bu`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 31 | `##bba` | `##bba` | `##bba`, `bu`, `##₂` | `##bba`, `bu`, `##₂`, `##b`, `##B` | `##bba` | `##bba`, `bu`, `##ppa` | `##bba`, `bu`, `##ppa`, `##B`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 32 | `pa` | `pa` | `pa`, `la`, `pi` | `pa`, `la`, `pi`, `di`, `e` | `pa` | `pa`, `pi`, `la` | `pa`, `pi`, `la`, `e`, `di` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 33 | `##₂` | `##₂` | `##₂`, `##₃`, `##r` | `##₂`, `##₃`, `##r`, `##š`, `##₆` | `##₂` | `##₂`, `##₃`, `##r` | `##₂`, `##₃`, `##r`, `##₄`, `##š` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 34 | `li` | `ni` | `ni`, `ri`, `a` | `ni`, `ri`, `a`, `li`, `ši` | `ni` | `ni`, `li`, `ši` | `ni`, `li`, `ši`, `a`, `ri` | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| 35 | `mi` | `mi` | `mi`, `u`, `ka` | `mi`, `u`, `ka`, `tu`, `i` | `mi` | `mi`, `ka`, `u` | `mi`, `ka`, `u`, `tu`, `sa` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 36 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `šu`, `ma` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `1diš`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 37 | `/` | `/` | `/`, `-`, `ša` | `/`, `-`, `ša`, `1u`, `2u` | `/` | `/`, `-`, `ša` | `/`, `-`, `ša`, `##₂`, `1u` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 38 | `la` | `la` | `la`, `li`, `aš` | `la`, `li`, `aš`, `ra`, `na` | `la` | `la`, `li`, `ša` | `la`, `li`, `ša`, `a`, `ra` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 39 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `+` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 40 | `ba` | `ba` | `ba`, `bi`, `bu` | `ba`, `bi`, `bu`, `BA`, `ga` | `ba` | `ba`, `bu`, `bi` | `ba`, `bu`, `bi`, `ga`, `na` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 41 | `-` | `-` | `-`, `##₂`, `+` | `-`, `##₂`, `+`, `/`, `.` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `/`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 42 | `ša` | `a` | `a`, `ša`, `ha` | `a`, `ša`, `ha`, `ta`, `wa` | `a` | `a`, `ša`, `ni` | `a`, `ša`, `ni`, `ku`, `pu` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 43 | `na` | `wa` | `wa`, `ba`, `ma` | `wa`, `ba`, `ma`, `ra`, `na` | `wa` | `wa`, `ra`, `ba` | `wa`, `ra`, `ba`, `ma`, `na` | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| 44 | `ku` | `ku` | `ku`, `-`, `i` | `ku`, `-`, `i`, `ka`, `u` | `ku` | `ku`, `u`, `-` | `ku`, `u`, `-`, `ka`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 45 | `##₃` | `##₃` | `##₃`, `##₂`, `a` | `##₃`, `##₂`, `a`, `##₄`, `ku` | `##₃` | `##₃`, `##₂`, `a` | `##₃`, `##₂`, `a`, `i`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 46 | `-` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `a` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 47 | `ka` | `ka` | `ka`, `tu`, `mi` | `ka`, `tu`, `mi`, `še`, `u` | `ka` | `ka`, `tu`, `mi` | `ka`, `tu`, `mi`, `u`, `sa` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 48 | `-` | `-` | `-`, `##₃`, `/` | `-`, `##₃`, `/`, `u`, `##₂` | `-` | `-`, `/`, `##₃` | `-`, `/`, `##₃`, `##kur`, `ti` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 49 | `pu` | `tu` | `tu`, `pu`, `me` | `tu`, `pu`, `me`, `ku`, `šu` | `pu` | `pu`, `ku`, `ta` | `pu`, `ku`, `ta`, `tu`, `bu` | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 50 | `pi` | `aš` | `aš`, `la`, `ta` | `aš`, `la`, `ta`, `u`, `šu` | `aš` | `aš`, `la`, `u` | `aš`, `la`, `u`, `ṣ`, `ši` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 51 | `##₂` | `##₂` | `##₂`, `##₃`, `##r` | `##₂`, `##₃`, `##r`, `##₄`, `##ṭ` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##r`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 52 | `am` | `am` | `am`, `tim`, `at` | `am`, `tim`, `at`, `nim`, `ma` | `am` | `am`, `at`, `tim` | `am`, `at`, `tim`, `im`, `nim` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 53 | `-` | `-` | `-`, `##r`, `##₂` | `-`, `##r`, `##₂`, `/`, `##₃` | `-` | `-`, `##r`, `##₂` | `-`, `##r`, `##₂`, `/`, `##m` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 54 | `mi` | `mi` | `mi`, `ka`, `u` | `mi`, `ka`, `u`, `tu`, `pi` | `mi` | `mi`, `ka`, `pi` | `mi`, `ka`, `pi`, `tu`, `am` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 55 | `ša` | `/` | `/`, `ša`, `-` | `/`, `ša`, `-`, `dumu`, `1diš` | `/` | `/`, `ša`, `-` | `/`, `ša`, `-`, `dumu`, `na` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 56 | `##₃` | `##₃` | `##₃`, `##₂`, `-` | `##₃`, `##₂`, `-`, `##₅`, `##₄` | `##₃` | `##₃`, `##₂`, `##₅` | `##₃`, `##₂`, `##₅`, `##₄`, `-` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 57 | `-` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `/`, `##₃` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `.`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 58 | `-` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `##₂` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 59 | `-` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `.`, `a` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `##₂`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 60 | `ma` | `ma` | `ma`, `um`, `šu` | `ma`, `um`, `šu`, `a`, `nim` | `ma` | `ma`, `um`, `šu` | `ma`, `um`, `šu`, `tim`, `nim` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 61 | `la` | `la` | `la`, `u`, `e` | `la`, `u`, `e`, `a`, `lu` | `la` | `la`, `u`, `e` | `la`, `u`, `e`, `a`, `li` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 62 | `-` | `-` | `-`, `.`, `##₂` | `-`, `.`, `##₂`, `/`, `:` | `-` | `-`, `.`, `##₂` | `-`, `.`, `##₂`, `:`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 63 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `##₃` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `+` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 64 | `-` | `-` | `-`, `##₂`, `.` | `-`, `##₂`, `.`, `:`, `/` | `-` | `-`, `.`, `##₂` | `-`, `.`, `##₂`, `/`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 65 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `##₂`, `:` | `-` | `-`, `##₂`, `:` | `-`, `##₂`, `:`, `.`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 66 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `##₂`, `:` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 67 | `na` | `na` | `na`, `ta`, `ma` | `na`, `ta`, `ma`, `di`, `nim` | `na` | `na`, `ta`, `ma` | `na`, `ta`, `ma`, `di`, `hi` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 68 | `-` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `dumu`, `1diš` | `-` | `-`, `/`, `ša` | `-`, `/`, `ša`, `la`, `dumu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 69 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `##₃` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 70 | `ur` | `um` | `um`, `u`, `šu` | `um`, `u`, `šu`, `ur`, `uš` | `um` | `um`, `ur`, `u` | `um`, `ur`, `u`, `ul`, `šu` | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| 71 | `a` | `e` | `e`, `##₃`, `##₂` | `e`, `##₃`, `##₂`, `i`, `a` | `a` | `a`, `e`, `i` | `a`, `e`, `i`, `iš`, `ap` | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| 72 | `-` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `a`, `##₃` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `##₃`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 73 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `.`, `:` | `-` | `-`, `/`, `##₂` | `-`, `/`, `##₂`, `:`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 74 | `am` | `am` | `am`, `nim`, `šu` | `am`, `nim`, `šu`, `tum`, `ar` | `am` | `am`, `nim`, `ni` | `am`, `nim`, `ni`, `ar`, `tim` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 75 | `##₂` | `##₂` | `##₂`, `##₃`, `##₈` | `##₂`, `##₃`, `##₈`, `##₄`, `##₅` | `##₂` | `##₂`, `##₃`, `##₈` | `##₂`, `##₃`, `##₈`, `##₄`, `##₆` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 76 | `u` | `u` | `u`, `ti`, `la` | `u`, `ti`, `la`, `tam`, `e` | `u` | `u`, `la`, `ti` | `u`, `la`, `ti`, `te`, `pa` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Top-1 accuracy on this example: text-only 60/76 (79%), vision 61/76 (80%)

Top-3 accuracy on this example: text-only 66/76 (87%), vision 68/76 (89%)

Top-5 accuracy on this example: text-only 72/76 (95%), vision 72/76 (95%)

### Metadata predictions

| head | ground truth | text-only prediction | vision prediction |
|---|---|---|---|
| period | Old Assyrian | Old Assyrian (0.94) | Old Assyrian (0.95) |
| genre | (no label) | Letters (0.92) | Letters (0.86) |
| language | (no label) | Akkadian (0.94) | Akkadian (0.91) |
| provenience | Kanesh | Kanesh (0.92) | Kanesh (0.95) |

---

## Example 6 — `P358248` (has photo: True)

**Original text (transliteration):**
> 3u ma - na ku₃ - babbar ni - is - ha - su₂ diri ša - du - a - su₂ ša - bu ša da - da - a a - na ku - ku - la₂ - nim dumu ku - ta - a ip - qi₂ - du - ma a - na a - lim ki a - na ši₂ - a - ma - tim ub - lu ku₃ - babbar ša D en - lil₂ - ba - ni a - na - nu - um a - šu - mi₃ D en - lil₂ - ba - ni eq - lam e - ti₂ - iq lu - qu₂ - tum iš - tu₃ a - lim ki e - li - a - ma a - šu - mi₃ D en - lil₂ - ba - ni - ma eq - lam a - na ka₃ - ni - iš₃ e - ra - ba - ma D en - lil₂ - ba - ni i - la₂ - qe₂ - ši₂ igi ba - zi - a dumu dingir - ku - ru - ub igi a - zu - ta - a dumu e - me - me igi a - šur - i - di₂ dumu kur - ub - eš₁₈ - dar

**Cuneiform (Unicode signs, whole document, not position-aligned to the text above):**
> 𒌍 𒈠 𒈾 𒆬 𒌓 𒉌 𒄑 𒄩 𒍪 𒋛𒀀 𒊭 𒁺 𒀀 𒍪 𒊭 𒁍 𒊭 𒁕 𒁕 𒀀 𒀀 𒈾 𒆪 𒆪 𒇲 𒉏 𒌉 𒆪 𒋫 𒀀 𒅁 𒆠 𒁺 𒈠 𒀀 𒈾 𒀀 𒅆 𒆠 𒀀 𒈾 𒋛 𒀀 𒈠 𒁴 𒌒 𒇻 𒆬 𒌓 𒊭 <D> 𒂗 𒆤 𒁀 𒉌 𒀀 𒈾 𒉡 𒌝 𒀀 𒋗 𒈨 <D> 𒂗 𒆤 𒁀 𒉌 𒅅 𒇴 𒂊 𒄭 𒅅 𒇻 𒆪 𒌈 𒅖 𒁺 𒀀 𒅆 𒆠 𒂊 𒇷 𒀀 𒈠 𒀀 𒋗 𒈨 <D> 𒂗 𒆤 𒁀 𒉌 𒈠 𒅅 𒇴 𒀀 𒈾 𒂵 𒉌 𒌍 𒂊 𒊏 𒁀 𒈠 <D> 𒂗 𒆤 𒁀 𒉌 𒄿 𒇲 𒆠 𒋛 𒅆 𒁀 𒍣 𒀀 𒌉 𒀭 𒆪 𒊒 𒌒 𒅆 𒀀 𒍪 𒋫 𒀀 𒌉 𒂊 𒈨 𒈨 𒅆 𒀀 𒋩 𒄿 𒄭 𒌉 𒆳 𒌒 𒁯

**Masked input (41 positions):**
> <strong>?</strong> ma - na ku₃ - babbar ni - is - <strong>?</strong> - su₂ diri ša <strong>?</strong> du - a - su <strong>?</strong> ša - bu ša da - da - a a - na ku - ku - la₂ - nim dumu ku - <strong>?</strong> - <strong>?</strong> ip - <strong>?</strong>i <strong>?</strong> - du - ma a - na a - lim ki a - na ši₂ - a - ma - tim ub - lu <strong>?</strong>₃ <strong>?</strong> <strong>?</strong>bbar ša <strong>?</strong> en - lil₂ <strong>?</strong> ba - <strong>?</strong> a - na - nu - um a - šu - mi₃ <strong>?</strong> en - li <strong>?</strong>₂ <strong>?</strong> <strong>?</strong> - ni eq - lam e <strong>?</strong> ti₂ - iq lu - qu₂ - <strong>?</strong> iš - tu₃ a - lim ki e - li <strong>?</strong> a - <strong>?</strong> a - šu - mi₃ D <strong>?</strong> - lil₂ - ba - ni <strong>?</strong> ma eq - la <strong>?</strong> a - <strong>?</strong> ka₃ - ni - iš₃ e - ra - ba - ma D en - lil <strong>?</strong> <strong>?</strong> ba - ni i - la₂ - <strong>?</strong>₂ - ši₂ igi ba - zi - a dumu din <strong>?</strong> - <strong>?</strong> - <strong>?</strong> - ub igi a - <strong>?</strong> - <strong>?</strong> - a <strong>?</strong> e - me - <strong>?</strong> igi a <strong>?</strong> šur - i - di₂ dumu kur <strong>?</strong> ub <strong>?</strong> eš₁₈ <strong>?</strong> <strong>?</strong>

### Restoration (masked-token predictions)

| # | true token | text-only top-1 | text-only top-3 | text-only top-5 | vision top-1 | vision top-3 | vision top-5 | text-only correct | vision correct | text-only top-3 hit | vision top-3 hit | text-only top-5 hit | vision top-5 hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `3u` | `1diš` | `1diš`, `1u`, `n` | `1diš`, `1u`, `n`, `2diš`, `3diš` | `1diš` | `1diš`, `n`, `1u` | `1diš`, `n`, `1u`, `2diš`, `3diš` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 2 | `ha` | `ha` | `ha`, `ki`, `hu` | `ha`, `ki`, `hu`, `ku`, `su` | `ha` | `ha`, `a`, `ma` | `ha`, `a`, `ma`, `su`, `ki` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | `-` | `-` | `-`, `##₃`, `D` | `-`, `##₃`, `D`, `ki`, `dumu` | `-` | `-`, `##₃`, `ša` | `-`, `##₃`, `ša`, `ki`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4 | `##₂` | `##₂` | `##₂`, `-`, `##m` | `##₂`, `-`, `##m`, `ša`, `##₃` | `##₂` | `##₂`, `-`, `ša` | `##₂`, `-`, `ša`, `##m`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5 | `ta` | `ku` | `ku`, `bu`, `li` | `ku`, `bu`, `li`, `nu`, `la` | `ku` | `ku`, `nu`, `bu` | `ku`, `nu`, `bu`, `ba`, `li` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 6 | `a` | `a` | `a`, `um`, `nim` | `a`, `um`, `nim`, `ni`, `ma` | `a` | `a`, `nim`, `um` | `a`, `nim`, `um`, `ni`, `ma` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | `q` | `q` | `q`, `ṣ`, `ṭ` | `q`, `ṣ`, `ṭ`, `ḫ`, `pal` | `q` | `q`, `ṭ`, `ṣ` | `q`, `ṭ`, `ṣ`, `ʾ`, `pal` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 8 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##₅`, `šu` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `šu`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 9 | `ku` | `ku` | `ku`, `i`, `u` | `ku`, `i`, `u`, `ša`, `tu` | `ku` | `ku`, `u`, `ša` | `ku`, `u`, `ša`, `i`, `tu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 10 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `##₂`, `/` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11 | `ba` | `ba` | `ba`, `ku`, `im` | `ba`, `ku`, `im`, `mu`, `ga` | `ba` | `ba`, `ga`, `bi` | `ba`, `ga`, `bi`, `bu`, `na` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 12 | `D` | `D` | `D`, `d`, `-` | `D`, `d`, `-`, `S`, `ki` | `D` | `D`, `d`, `-` | `D`, `d`, `-`, `S`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 13 | `-` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `dumu`, `ki` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `D`, `dumu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 14 | `ni` | `ni` | `ni`, `nu`, `na` | `ni`, `nu`, `na`, `a`, `nim` | `ni` | `ni`, `na`, `nu` | `ni`, `na`, `nu`, `a`, `še` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 15 | `D` | `D` | `D`, `d`, `-` | `D`, `d`, `-`, `S`, `dumu` | `D` | `D`, `d`, `-` | `D`, `d`, `-`, `S`, `iti` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 16 | `##l` | `##l` | `##l`, `##m`, `##la` | `##l`, `##m`, `##la`, `##r`, `##₂` | `##l` | `##l`, `##m`, `##₂` | `##l`, `##m`, `##₂`, `##la`, `##r` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 17 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `dumu`, `D` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `D`, `dumu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 18 | `ba` | `ba` | `ba`, `a`, `bu` | `ba`, `a`, `bu`, `ga`, `bi` | `ba` | `ba`, `a`, `ra` | `ba`, `a`, `ra`, `ma`, `ga` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 19 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `:` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 20 | `tum` | `ul` | `ul`, `ša`, `nim` | `ul`, `ša`, `nim`, `lu`, `tim` | `ul` | `ul`, `ša`, `nim` | `ul`, `ša`, `nim`, `um`, `lu` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 21 | `-` | `-` | `-`, `##m`, `##₂` | `-`, `##m`, `##₂`, `ša`, `ki` | `##m` | `##m`, `-`, `##₂` | `##m`, `-`, `##₂`, `ša`, `##š` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 22 | `ma` | `na` | `na`, `nim`, `ma` | `na`, `nim`, `ma`, `ta`, `am` | `na` | `na`, `nim`, `ta` | `na`, `nim`, `ta`, `ma`, `di` | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| 23 | `en` | `en` | `en`, `nin`, `ni` | `en`, `nin`, `ni`, `be`, `En` | `en` | `en`, `nin`, `an` | `en`, `nin`, `an`, `de`, `ni` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 24 | `-` | `-` | `-`, `/`, `:` | `-`, `/`, `:`, `a`, `ki` | `-` | `-`, `a`, `/` | `-`, `a`, `/`, `ki`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 25 | `##m` | `##m` | `##m`, `##₂`, `-` | `##m`, `##₂`, `-`, `##em`, `##l` | `##m` | `##m`, `##₂`, `-` | `##m`, `##₂`, `-`, `##em`, `##l` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 26 | `na` | `na` | `na`, `nim`, `ta` | `na`, `nim`, `ta`, `ma`, `šu` | `na` | `na`, `di`, `nim` | `na`, `di`, `nim`, `ta`, `ma` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 27 | `##₂` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `##₁`, `##2` | `##₂` | `##₂`, `##₃`, `##₄` | `##₂`, `##₃`, `##₄`, `-`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 28 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `a` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `/`, `a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 29 | `qe` | `ši` | `ši`, `aš`, `ap` | `ši`, `aš`, `ap`, `qe`, `pa` | `qe` | `qe`, `aš`, `ši` | `qe`, `aš`, `ši`, `ap`, `u` | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| 30 | `##gir` | `##gir` | `##gir`, `##₂`, `##₃` | `##gir`, `##₂`, `##₃`, `##₄`, `##kur` | `##gir` | `##gir`, `##₂`, `##₃` | `##gir`, `##₂`, `##₃`, `##₄`, `##₅` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 31 | `ku` | `šu` | `šu`, `mu`, `ta` | `šu`, `mu`, `ta`, `e`, `ku` | `šu` | `šu`, `mu`, `a` | `šu`, `mu`, `a`, `ku`, `e` | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| 32 | `ru` | `ru` | `ru`, `ku`, `bu` | `ru`, `ku`, `bu`, `šu`, `lu` | `ru` | `ru`, `lu`, `bu` | `ru`, `lu`, `bu`, `ku`, `mu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 33 | `zu` | `hu` | `hu`, `na`, `bu` | `hu`, `na`, `bu`, `hi`, `bi` | `hu` | `hu`, `bu`, `ha` | `hu`, `bu`, `ha`, `bi`, `ba` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 34 | `ta` | `a` | `a`, `la`, `ni` | `a`, `la`, `ni`, `ba`, `ma` | `a` | `a`, `la`, `ba` | `a`, `la`, `ba`, `ni`, `na` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 35 | `dumu` | `dumu` | `dumu`, `igi`, `-` | `dumu`, `igi`, `-`, `ša`, `dam` | `dumu` | `dumu`, `igi`, `-` | `dumu`, `igi`, `-`, `ša`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 36 | `me` | `ni` | `ni`, `er`, `a` | `ni`, `er`, `a`, `e`, `en` | `a` | `a`, `er`, `šu` | `a`, `er`, `šu`, `ni`, `en` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 37 | `-` | `-` | `-`, `+`, `.` | `-`, `+`, `.`, `/`, `##₂` | `-` | `-`, `+`, `##₂` | `-`, `+`, `##₂`, `.`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 38 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `/`, `##₄` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `##₄`, `:` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 39 | `-` | `-` | `-`, `dumu`, `igi` | `-`, `dumu`, `igi`, `##₂`, `iti` | `-` | `-`, `dumu`, `igi` | `-`, `dumu`, `igi`, `##₂`, `##₃` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 40 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `dumu`, `ki` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 41 | `dar` | `dar` | `dar`, `tar`, `um` | `dar`, `tar`, `um`, `zal`, `ša` | `dar` | `dar`, `tar`, `ša` | `dar`, `tar`, `ša`, `šu`, `um` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Top-1 accuracy on this example: text-only 32/41 (78%), vision 32/41 (78%)

Top-3 accuracy on this example: text-only 33/41 (80%), vision 33/41 (80%)

Top-5 accuracy on this example: text-only 35/41 (85%), vision 35/41 (85%)

### Metadata predictions

| head | ground truth | text-only prediction | vision prediction |
|---|---|---|---|
| period | Old Assyrian | Old Assyrian (0.93) | Old Assyrian (0.93) |
| genre | (no label) | Legal (0.61) | Legal (0.64) |
| language | (no label) | Akkadian (0.93) | Akkadian (0.94) |
| provenience | Kanesh | Kanesh (0.92) | Kanesh (0.92) |

---

## Example 7 — `P359100` (has photo: True)

**Original text (transliteration):**
> eš₁₈ - dar - la₂ - ma - si₂ dumu - munus a - šur₃ - na - da puzur₄ - eš₁₈ - dar i - ra - de₈ - ši₂ u₃ qa₂ - di₂ - šu - ma eš₁₈ - dar - la₂ - ma - si₂ a - di₂ 3diš ša - na - at e - ha - az a - šur - ne₂ - me - di₂ i - di₂ - nu - ši₂

**Cuneiform (Unicode signs, whole document, not position-aligned to the text above):**
> 𒀹 𒁯 𒇲 𒈠 𒍣 𒌉 𒊩 𒀀 𒋓 𒈾 𒁕 𒅤𒊭 𒀹 𒁯 𒄿 𒊏 𒄭 𒋛 𒅇 𒂵 𒊹 𒋗 𒈠 𒀹 𒁯 𒇲 𒈠 𒍣 𒀀 𒊹 𒐈 𒊭 𒈾 𒀜 𒂊 𒄩 𒊍 𒀀 𒋩 𒉌 𒈨 𒊹 𒊹 𒉡 𒋛

**Masked input (16 positions):**
> eš₁₈ - dar - la₂ - ma <strong>?</strong> si₂ dumu - <strong>?</strong>us a - šur₃ <strong>?</strong> na - <strong>?</strong> puzur₄ - eš₁₈ - dar i - ra - de₈ - <strong>?</strong>₂ u₃ qa₂ <strong>?</strong> di₂ - šu - <strong>?</strong> eš₁₈ - dar <strong>?</strong> la₂ - ma - si₂ a - di₂ 3diš ša - na - at e - <strong>?</strong> <strong>?</strong> az <strong>?</strong> - šur - ne₂ <strong>?</strong> me - di₂ <strong>?</strong> - di₂ <strong>?</strong> <strong>?</strong> <strong>?</strong> ši₂

### Restoration (masked-token predictions)

| # | true token | text-only top-1 | text-only top-3 | text-only top-5 | vision top-1 | vision top-3 | vision top-5 | text-only correct | vision correct | text-only top-3 hit | vision top-3 hit | text-only top-5 hit | vision top-5 hit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `-` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | `-` | `-`, `.`, `:` | `-`, `.`, `:`, `/`, `##₂` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | `mun` | `mun` | `mun`, `nun`, `ut` | `mun`, `nun`, `ut`, `mur`, `w` | `mun` | `mun`, `nun`, `w` | `mun`, `nun`, `w`, `ut`, `ur` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | `-` | `-` | `-`, `dumu`, `/` | `-`, `dumu`, `/`, `ša`, `šu` | `-` | `-`, `dumu`, `ša` | `-`, `dumu`, `ša`, `šu`, `u` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4 | `da` | `da` | `da`, `ni`, `na` | `da`, `ni`, `na`, `a`, `bi` | `na` | `na`, `da`, `din` | `na`, `da`, `din`, `bi`, `ni` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 5 | `ši` | `u` | `u`, `ši`, `eš` | `u`, `ši`, `eš`, `de`, `li` | `u` | `u`, `qe`, `ši` | `u`, `qe`, `ši`, `li`, `be` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 6 | `-` | `-` | `-`, `/`, `.` | `-`, `/`, `.`, `:`, `##₂` | `-` | `-`, `:`, `/` | `-`, `:`, `/`, `##₂`, `.` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | `ma` | `ma` | `ma`, `nu`, `ni` | `ma`, `nu`, `ni`, `um`, `na` | `nu` | `nu`, `ma`, `um` | `nu`, `ma`, `um`, `ni`, `tim` | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 8 | `-` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `dumu`, `/` | `-` | `-`, `:`, `.` | `-`, `:`, `.`, `a`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 9 | `ha` | `ra` | `ra`, `zi`, `ba` | `ra`, `zi`, `ba`, `za`, `me` | `ra` | `ra`, `ba`, `na` | `ra`, `ba`, `na`, `ta`, `zi` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 10 | `-` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `1diš`, `ša` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `ša`, `##a` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11 | `a` | `a` | `a`, `i`, `aš` | `a`, `i`, `aš`, `šu`, `e` | `a` | `a`, `i`, `aš` | `a`, `i`, `aš`, `e`, `šu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 12 | `-` | `-` | `-`, `/`, `dumu` | `-`, `/`, `dumu`, `##₂`, `ša` | `-` | `-`, `##₂`, `dumu` | `-`, `##₂`, `dumu`, `/`, `ša` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 13 | `i` | `a` | `a`, `i`, `li` | `a`, `i`, `li`, `e`, `ni` | `a` | `a`, `i`, `na` | `a`, `i`, `na`, `ni`, `li` | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 14 | `-` | `-` | `-`, `u`, `ša` | `-`, `u`, `ša`, `/`, `la` | `-` | `-`, `ša`, `u` | `-`, `ša`, `u`, `1diš`, `dumu` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 15 | `nu` | `a` | `a`, `##₂`, `šu` | `a`, `##₂`, `šu`, `na`, `ba` | `na` | `na`, `nu`, `##₂` | `na`, `nu`, `##₂`, `a`, `šu` | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| 16 | `-` | `-` | `-`, `##₂`, `/` | `-`, `##₂`, `/`, `##₃`, `a` | `-` | `-`, `##₂`, `##₃` | `-`, `##₂`, `##₃`, `a`, `/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Top-1 accuracy on this example: text-only 12/16 (75%), vision 10/16 (62%)

Top-3 accuracy on this example: text-only 14/16 (88%), vision 15/16 (94%)

Top-5 accuracy on this example: text-only 14/16 (88%), vision 15/16 (94%)

### Metadata predictions

| head | ground truth | text-only prediction | vision prediction |
|---|---|---|---|
| period | Old Assyrian | Old Assyrian (0.94) | Old Assyrian (0.96) |
| genre | Legal | Letters (0.47) | Letters (0.45) |
| language | Akkadian | Akkadian (0.93) | Akkadian (0.92) |
| provenience | Kanesh | Kanesh (0.94) | Kanesh (0.95) |

---
