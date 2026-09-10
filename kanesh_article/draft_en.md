# NLP Classification of Cuneiform Archives as a Tool for the Quantitative History of Entrepreneurship: The Case of the Old Assyrian Trade Colony of Kanesh

*Working title — English version. Structure follows the advisor's required
outline; Section 3 is adapted to describe our own contribution without
foregrounding architecture/metrics. See `article_outline.md` for the thesis
list this draft is built from and `showcase_tablets.md` for full source
documentation of every quoted tablet.*

**Epigraph — not yet chosen, two candidates (see `article_outline.md`):**

> *"Urgent! When you hear this letter, come, look to Aššur, your god, and
> your home hearth, and let me see you in person while I am still alive!
> Misery has entered our minds."*
> — Tarām-Kūbī to Innaya (CCT 3, 25) [10]

*or*

> *"Who is this man who lives in your house and who is criticizing the
> textiles when they get to him?"*
> — Lamassī to Pūšu-kēn (BIN 6, 11) [10]

---

## 1. Introduction

Kanesh — a merchant colony in central Anatolia, at what is now Kültepe,
Turkey — was the administrative hub of a network of roughly thirty Old
Assyrian trading settlements (*kārū* and *wabartātum*) scattered across the
Anatolian plateau, of which only two others have ever been identified:
Boğazköy (ancient Ḫattuš) and Alişar (probably ancient Amkuwa), both
yielding only a few dozen fragmentary tablets by comparison *([3] Veenhof
1972, pp. xxi–xxii; [4] Veenhof 1997, p. 338; [10] Michel 2020, p. 6)*.
Merchants from the city of Aššur ran this colony as a private, long-distance
trade (ca. 1950–1750 BCE): donkey caravans carried tin and fine woollen
textiles into Anatolia, to be exchanged there for the silver and gold
shipped back to Aššur *([1] Larsen 2015, ch. 14 "The Caravan Trade," pp.
171–188; [4] Veenhof 1997, p. 338)*. Larsen calls Kanesh "the earliest
attested commercial society in world history" *([1] Larsen 2015, back-cover
/ inside-jacket blurb — unpaginated jacket copy, not a numbered page)*.

The scale of the resulting archive is itself worth stating plainly, since it
is the reason this paper exists. Tablets from Kanesh have been looted since
the late nineteenth century; systematic, controlled excavation resumed only
in 1948 under Tahsin Özgüç, who directed the site for fifty-seven years, and
has continued since 2006 under Fikri Kulakoğlu *([2] Anderson 2018, pp.
29–30, incl. footnote 52; [1] Larsen 2015, ch. 2 "The Discovery," p. 17;
[10] Michel 2020, pp. 6–8)*. Roughly 23,500 tablets are known in total
(23,350 from Kültepe itself, plus some 150 from the handful of neighboring
Anatolian sites above); the excavations after 1948 alone added over 17,000
tablets to the ca. 6,500 already known before *([2] Anderson 2018, pp.
29–30, footnote 52)*. By genre, according to the Old Assyrian Text Project
database, the largest single category is letters (2,113 of roughly 6,300
tagged texts — about a third), followed by debt notes (553) and depositions
(260) *([2] Anderson 2018, p. 33, footnote 56)*.

These merchants operated as family trading houses: a father based in Aššur,
a son or agent stationed in Kanesh, and correspondence as the operational
instrument that held a business together across roughly 1,000 km
*([1] Larsen 2015, ch. 16 "Families and Money," pp. 202–217)*. To finance
individual caravan expeditions, merchants used the *naruqqum* ("money bag")
— a joint fund pooled from 10 to 15 investors for a single venture lasting
some 10 to 12 years, with profits distributed by share, a structure with an
obvious resemblance to venture or joint-stock financing *([1] Larsen 2015,
ch. 17 "Where Did the Money Come from?," pp. 217–227)*. Credit was extended
at roughly 30% annual interest, agency relationships were formalized by
contract, and reputation substituted for the courts that essentially did
not exist for the enforcement of these obligations across distance —
enforcement instead ran through correspondence *([1] Larsen 2015, ch. 14,
pp. 182–184, and ch. 16–17, pp. 205, 217)*. Assyriologists themselves
describe these features as unusually advanced for their time: the abstract
of Veenhof's 1997 paper states directly that Old Assyrian trade shows
"features not attested in earlier commercial records from ancient
Mesopotamia or elsewhere and/or usually considered innovations of classical
or early medieval times" *([4] Veenhof 1997, p. 336, Abstract)*.

Women in Aššur were independent economic agents in this system, not merely
custodians of the household while their husbands traveled. They produced the
textiles that were the trade's principal export good, from raw wool through
to a finished, sellable product *([5] Michel 2006, p. 285, Résumé)*, and
they are independently documented as buyers, heirs, and holders of capital
and real estate in their own right *([6] Michel 2016, p. 83, Abstract, for
the claim itself; pp. 84–85, § III "How Did Women Become Owners of a
House?" for the purchase/inheritance detail)*.

This entire institutional inheritance — family firms, venture-style
financing, credit and reputation mechanisms, women as independent economic
actors — is recorded on the roughly 23,500 cuneiform tablets described
above, the large majority of which have never been translated or
systematically processed *([2] Anderson 2018, pp. 29–30)*. Two further
obstacles compound that imbalance. First, most tablets reached museum and
private collections through undocumented, illicit digging rather than
controlled excavation, so scholars usually cannot rely on archaeological
provenance to reconstruct which texts belonged to the same original archive
*([2] Anderson 2018, pp. 34–35)*. Second, the corpus is dense with
homonymy, sharpened by *papponymy* — the practice of naming a son after his
own father or grandfather — so that a single personal name can correspond
to several different individuals across the archive, sometimes with dozens
of attested patronymics for the same name *([2] Anderson 2018, pp. 36–38;
[8] Bamman, Anderson & Smith 2013, p. 1)*. Larsen himself, after
reconstructing one of the best-documented family archives at Kanesh,
concluded that a full reconstruction of the original archives "on the basis
of an internal analysis of texts without any archaeological context" is
simply not achievable *([2] Anderson 2018, pp. 39–40, quoting Larsen 2002,
pp. xiv–xv)*. That imbalance between the size and tangledness of the archive
and the pace at which it can be read and disambiguated by hand is the
starting point for this paper: can automatic processing make this archive
tractable at scale?

## 2. Literature Review

The historical and institutional backdrop above draws on two standard
references: Larsen's monograph on the organization of the Kanesh *kārum*,
its family houses, credit, and caravan trade *([1] Larsen 2015; ch. 1
"Introduction," p. 1, is the fastest entry point)*, and Veenhof's
foundational philological and economic study of Old Assyrian trade
terminology and institutions, still the field's reference work half a
century after publication *([3] Veenhof 1972; Preface, p. xiii)*. Veenhof's
later paper on the "modern" features of Old Assyrian trade law — including
the *naruqqum* and long-term partnership structures — argues directly that
these mechanisms anticipate what are usually considered much later legal
inventions, a claim made by a specialist Assyriologist from inside the
field rather than by an outside popularizer *([4] Veenhof 1997, p. 336,
Abstract)*. On the social side, Michel's work documents women in Aššur as
textile producers responsible for the trade's principal export good
*([5] Michel 2006, p. 285, Résumé)*, and, separately, as independently
attested buyers, heirs, and holders of capital and real estate *([6] Michel
2016, p. 83, Abstract)*.

A separate strand of literature establishes that quantitative and
computational methods have already produced genuinely new historical
knowledge from this specific corpus, which is the direct precedent this
paper builds on. Barjamovic, Chaney, Coşar, and Hortaçsu built a structural
gravity model of Bronze Age trade from roughly 12,000 digitized Old Assyrian
tablets and used it to statistically locate lost ancient cities, resolving
long-standing disputes among historians — published, notably, in a leading
economics journal rather than an Assyriological one *([7] Barjamovic et al.
2019/2017 NBER working-paper PDF, pp. 1–2, Abstract)*. Bamman, Anderson,
and Smith applied computational social network analysis directly to the
Kanesh corpus to infer the relative social rank of individual merchants from
correspondence patterns, with a co-author (Noah A. Smith) who is a
recognized NLP researcher — an explicit bridge between Assyriology and
computer science on this exact material *([8] Bamman, Anderson & Smith
2013, p. 1, § 1 "Introduction")*. Anderson's dissertation performs a
quantitative, network-based reconstruction of Old Assyrian society from
roughly 6,000 of the archive's ~23,000 tablets, including hierarchical
social status and family genealogies *([2] Anderson 2018, p. iii, Abstract,
for the overall claim; pp. 29–30 for the tablet-count figure)*. Most
directly relevant to the present paper, Anderson separately describes an
NLP and network-theory pipeline built specifically to disambiguate
homonymous individuals in the Old Assyrian corpus — the closest existing
precedent, by its own title, to "NLP classification of cuneiform archives"
*([9] Anderson 2019, Abstract — the ResearchGate page is not paginated)*.

## 3. Methodology: Selected Examples

Our model performs two tasks jointly from a tablet's transliteration and
photograph together: it restores damaged or illegible spans of text, and
it attributes the tablet to a period, genre, provenience, and language. It
is trained on a large corpus that includes tablets from Kanesh among its
sources; on the held-out test portion of that corpus it reaches 96.2%
accuracy on period, 96.2% on genre, 98.6% on language, and 87.0% on
provenience across 38 possible places of origin — including 100% recall on
Kanesh itself. This section does not describe the model's architecture or
report comparative metrics further; instead, it presents the kind of
material the model is trained and evaluated on, through a small number of
real tablets, each independently verified against Michel's published
translations [10]. Every prediction shown below is the actual output of
the trained checkpoint on these seven tablets, all of which sit in the
held-out test split the model was never trained on.

**Puzur-Aššur to Waqqurtum (AO 9256), on weaving.** A husband in Kanesh
gives his wife in Aššur precise technical instructions for the textiles she
is producing for him to sell:

> *"The thin textile you sent me, make (more) like it and send (them) to me
> with Aššur-idī, and I will send you ½ mina of silver (apiece). They should
> strike one side of the textile, and not pluck it. Its warp should be
> close. Process per piece 1 mina more wool than you used for the previous
> textile you sent me, but they must remain thin! [...] A finished textile
> that you make must be 9 cubits long and 8 cubits wide."*
> *([10] Michel 2020, document #162 "Technical Advice for Weaving and
> Finishing a Textile," pp. 264–265)*

This is not a stray detail: it is a specification, with tolerances, for a
traded good, exchanged as ordinary business correspondence between spouses
thousands of kilometers apart.

**Lamassī to Pūšu-kēn (BIN 6, 11), on quality control and suspicion.**
Lamassī answers her husband's repeated complaints about the textiles she
sends him:

> *"Why do you write to me every time as follows: 'The textiles that you
> keep sending me are not good?' Who is this man who lives in your house
> and who is criticizing the textiles when they get to him? As for me, in
> order that from each caravan trip at least 10 shekels of silver accrue to
> your house, I try my best to make and send textiles to you!"*
> *([10] Michel 2020, document #165 "Criticism of the Quality of Textiles
> Sent," p. 268)*

In four sentences the letter carries an economic claim (her labor generates
at least 10 shekels of silver per caravan trip) and a pointed domestic one
(who, exactly, is criticizing her work in her husband's house).

**Tarām-Kūbī to Innaya (CCT 3, 24), on being left destitute.** Writing after
her husband's departure, Tarām-Kūbī describes what happened at home during a
famine in Aššur:

> *"When you left, you did not leave me silver, not even a single shekel!
> You emptied the house and took (everything) out! After you had gone,
> there was a severe famine in the city (of Aššur) while you had not left
> me barley, not even a single liter!"*
> *([10] Michel 2020, document #128, pp. 215–216)*

Two further tablets from the same archives are cited without a full
quotation. A damaged letter from Imdī-ilum and Ištar-baštī to their
daughter Zizizi (VS 26, 33) reproaches her, after the death of her first
husband, for having remarried an Anatolian and drifted from her family in
Aššur *([10] Michel 2020, document #50 "The Cost of a Remarriage," pp.
106–107)*. A second letter from Tarām-Kūbī to Innaya (CCT 3, 25) — already
present in our corpus with its photograph — mixes routine household
business (silver, barley, unpaid debts) with a single urgent line asking
her husband to come home while she is still alive *([10] Michel 2020,
document #129, pp. 216–217)*; whichever epigraph is ultimately chosen for
this paper is drawn from that same letter.

**A demonstration on an "uninteresting" text (VS 26, 102).** Roughly 90% of
the archive consists of exactly this kind of short, dry, legally structured
record, not letters with personal drama. This deposition — first published
by Larsen, who identifies it as the opening document of a three-part
"Standard Text" dossier (declaration of a silver claim → notification
letter → caravan account) [11] — reads:

> *"The 30 minas of silver — its import tax added, its transport fee paid —
> which Dadaya entrusted to Kukkulanum, son of Kutaya, and which he carried
> to the City for purchases — that silver belongs to Enlil-bāni. [...]
> Before Baziya, son of Ili-kurub; before Azutaya, son of Ememe; before
> Aššur-idī, son of Kurub-Ištar."*
> *([10,11] Larsen 1967, pp. 7–9, the "Type 1: the Transport-Contract"
> edition; also in our own corpus as VS 26,102 / P358248)*

This is the kind of input the model has to handle correctly for a
processing pipeline over the archive to be useful at all: a formulaic legal
text naming a sum, two parties, a purpose, and witnesses, with none of the
narrative color of the letters above. To make the restoration task concrete,
we masked 41 of this tablet's signs (15% of the text) and asked the model to
recover them one at a time, from context alone:

| masked sign (true value) | model's top prediction | correct? |
|---|---|---|
| `ha` | `ha` | ✅ |
| divine determinative `D` (before "Enlil-bāni") | `D` | ✅ |
| `qe` (in "i-la₂-qe₂-ši₂," "he will receive it") | `qe` | ✅ (text-only alone predicted `ši` — wrong) |
| `tum` | `ul` | ❌ |
| `zu` (in the witness name "Azutaya") | `hu` | ❌ |

Overall, the model recovered 32 of the 41 masked signs correctly on its
first guess (78%) — in line with the aggregate figures above — and the one
case flagged in the table is a small, concrete illustration of what the
photograph adds: the text-only model guesses wrong where the vision model,
seeing the same masked text plus the tablet's photograph, gets it right.

**A marriage contract (Prague I 490).** The archive's legal genre extends
beyond debt and transport to family law. This contract, arranged after the
death of the merchant Aššur-nādā by his son and his Anatolian wife
Šišaḫšušar for their daughter, includes a clause governing a possible second
marriage and a clause on childlessness:

> *"Puzur-Ištar married as an amtum-wife Ištar-lamassī, daughter of
> Aššur-nādā [...]. Also he shall not marry another (wife) apart from his
> aššutum-wife in the city of Aššur. If, within 3 years, Ištar-lamassī does
> not see a baby, he may buy a female slave and take her (for
> procreation)."*
> *([10] Michel 2020, document #23 "Clause Concerning Infertility, Mention
> of Another Wife in Aššur," pp. 78–79)*

Michel's broader study situates this clause as a normal, legally regulated
practice for merchants who spent long periods away from Aššur — the
"amtum"/"aššutum" wife pairing, not a secret second household — which
Michel describes as unique in the ancient Near East precisely because of
the demands of this merchant lifestyle *([10] Michel 2020, §
"Monogamy and Bigamy," pp. 68–71)*. This document sits in the same family
archive as Aššur-nādā's own correspondence quoted above: the marriage it
records took place after his death.

**All seven tablets together.** Period (Old Assyrian) and language (Akkadian,
where labeled) were predicted correctly for every one of the seven tablets
above, so they are left out of the table below; provenience (Kanesh) was
also predicted correctly for all seven, with 0.92–0.96 confidence — the
table instead shows genre, the head with the most room to disagree:

| Tablet | Genre (ground truth) | Model's genre prediction |
|---|---|---|
| Zizizi (VS 26, 33) | *(unlabeled)* | Letters (0.73) |
| Puzur-Aššur → Waqqurtum (AO 9256) | Letters | Letters (0.87) |
| Lamassī → Pūšu-kēn (BIN 6, 11) | Letters | Letters (0.89) |
| Tarām-Kūbī, doc. #128 (CCT 3, 24) | *(unlabeled)* | Letters (0.91) |
| Tarām-Kūbī, doc. #129 (CCT 3, 25) | *(unlabeled)* | Letters (0.86) |
| Kukkulanum (VS 26, 102) | *(unlabeled)* | Legal (0.64) |
| Marriage contract (Prague I 490) | Legal | **Letters (0.45)** |

Six of seven are exactly what a reader would expect. The seventh is a real
miss worth stating plainly rather than hiding: the marriage contract is
mislabeled as a letter — and at 0.45 confidence, the model itself is
visibly unsure, rather than confidently wrong. A one-line, second-person
legal formula ("Puzur-Ištar married... he shall pay...") is close enough in
surface form to an opening letter formula that the two genres apparently
blur together at the model's current scale; a larger or better-balanced
training set for the Legal class is one direction to explore before this
model gets used for anything beyond illustration.

## 4. Conclusion

Automated processing of an archive of this size opens the same kind of
research to historians and economists that Barjamovic et al. performed by
hand on a subset of digitized tablets — geographic reconstruction of lost
cities and trade routes — but at the scale of the full archive rather than
a curated sample *([7] Barjamovic et al. 2019/2017, pp. 1–2, Abstract)*.
More directly, it extends into the history of entrepreneurship: the
*naruqqum* as a precursor to venture financing, and reputation mechanisms
as a precursor to credit history, become material for scalable, corpus-wide
research rather than a handful of individually selected illustrative
tablets — our own argument, building on [1] and [4] above. For the author's
own diploma project, this paper is intended to substitute for what had been
a purely technical description of model architecture: a "Motivation" and
"Related Work" grounded in the actual economic and historical stakes of the
material the model is trained on.

---

## References

1. Larsen, Mogens Trolle. 2015. *Ancient Kanesh: A Merchant Colony in
   Bronze Age Anatolia*. Cambridge: Cambridge University Press.
2. Anderson, Adam Grant. 2018. *The Old Assyrian Social Network: An
   Analysis of the Texts from Kültepe-Kanesh (1950–1750 B.C.E.)*. PhD
   dissertation, Harvard University, Department of Near Eastern Languages
   and Civilizations.
3. Veenhof, Klaas R. 1972. *Aspects of Old Assyrian Trade and Its
   Terminology*. Studia et Documenta ad Iura Orientis Antiqui Pertinentia,
   Volumen X. Leiden: E. J. Brill.
4. Veenhof, Klaas R. 1997. "'Modern' Features in Old Assyrian Trade."
   *Journal of the Economic and Social History of the Orient* 40 (4):
   336–366.
5. Michel, Cécile. 2006. "Femmes et production textile à Aššur au début du
   IIe millénaire av. J.-C." *Techniques & Culture* 46: 285–301.
6. Michel, Cécile. 2016. "Women and Real Estate in the Old Assyrian Texts."
   *Orient* 51: 83–94.
7. Barjamovic, Gojko, Thomas Chaney, Kerem A. Coşar, and Ali Hortaçsu.
   2019. "Trade, Merchants, and the Lost Cities of the Bronze Age."
   *Quarterly Journal of Economics* 134 (3): 1455–1503.
8. Bamman, David, Adam Anderson, and Noah A. Smith. 2013. "Inferring
   Social Rank in an Old Assyrian Trade Network." Paper presented at
   *Digital Humanities 2013*, Lincoln, NE. arXiv:1303.2873.
9. Anderson, Adam G. 2019. "Disambiguating the Old Assyrian Social
   Networks Using NLP and Network Theory." Self-archived research note,
   ResearchGate, October 2019. https://www.researchgate.net/publication/336460070
10. Michel, Cécile. 2020. *Women of Assur and Kanesh: Texts from the
    Archives of Assyrian Merchants*. Writings from the Ancient World 42.
    Atlanta: SBL Press.
11. Larsen, Mogens Trolle. 1967. *Old Assyrian Caravan Procedures*.
    Publications de l'Institut Historique et Archéologique Néerlandais de
    Stamboul (PIHANS) XXII. Leiden: Nederlands Instituut voor het Nabije
    Oosten.
