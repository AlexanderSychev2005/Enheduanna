# NLP Classification of Cuneiform Archives as a Tool for the Quantitative History of Entrepreneurship: The Case of the Old Assyrian Trade Colony of Kanesh

*Working title — English version. Structure follows the advisor's required
outline; Section 3 is adapted to describe our own contribution without
foregrounding architecture/metrics. See `article_outline.md` for the thesis
list this draft is built from and `showcase_tablets.md` for full source
documentation of every quoted tablet.*

> *"Who is this man who lives in your house and who is criticizing the
> textiles when they get to him?"*
> — Lamassī to Pūšu-kēn (BIN 6, 11)

---

## 1. Introduction

Kanesh – a merchant colony in ancient central Anatolia (Kültepe, near
Kayseri, Turkey) that was an Old Assyrian trade outpost (*kārum*) and the
first attested commercial system in world history. The city was a part of
the well-organized Old Assyrian long-distance trade of around 2000–1750 BC
in which donkey caravans carried tin (essential for the Anatolian
production of bronze) and fine textiles from Assur to Anatolia to be
exchanged there for silver and gold shipped back to Assur (1,2).

Kanesh was an administrative centre of around 30 commercial settlements in
ancient Anatolia. Considering other settlements mentioned in ancient texts,
only two have been identified besides Kanesh, those at Boğazköy (Hattusa)
and Alisar (most probably Amkuwa), but compared with Kanesh, there are a
few fragmented dozen tablets left, and these date from a slightly later
period (2,3).

Kanesh investigations started in the 19th century. The city was first
excavated by illegal diggers and scholars looking for written sources.
Regular excavations by Turkish archaeologists started in 1948 after world
wars under the direction of Tahsin Özgüç, and since 2006, Kültepe
excavations have been directed by Fikri Kulakoğlu, who invite many
colleagues from different fields to unveil new layers about the daily life
at Kanesh. Now, approximately 23,500 cuneiform tablets are found, the
excavations since 1948 have added 17,000 tablets. Over 23,350 are from
Kanesh and about 150 tablets are from sites from the surrounding area in
Anatolia (4,5). Regarding the genre, thanks to the work of Thomas Hertel
and the OATP, we know that letters are the largest category (one third,
about 2,000) of documents (4).

*Fig. 1.1. Map of Old Assyrian trade network in Anatolia. Cartography by
Ivan d'Hostingue and Gojko Barjamovic 2010*

Historically, family plays a vital role when it comes to long-distance
commerce. For example, the Assur-idi family is a perfect example of family
firm, a father in Assur was running a fairly tightly organised business
where he was a boss and three sons who functioned as his agents in
Anatolia where correspondence was the only way to contact to each other
being 1,000 kilometres away (1).

The naruqqum was a long-term joint-stock company or partnership that was
used to concentrate large amounts of capital in the hands of competent
merchants in the overland commerce. The term literally means "a sack",
referring to original practice where investors would throw their
contributions into a bag. The contracts ran for 10-12 years and premature
withdrawal of the investment meant that the investor would not share in
the profit (1).

The management of credit sales and debt collection across the trade
network mostly relied on trust and correspondence. Because credit agents
were moving around all the time, some local representatives had to bring
them before witnesses and make them declare their intentions without the
original debt notes, making legal processes difficult. However, the
documentation tells that the traders made up with different commercial and
judicial practices including contractual and legal rules for coping with
insolvent, absent or unwilling debtors, and issuing bearer bonds, which, as
Assyriologists point out, was millennia ahead of European medieval
commercial innovations (1,2).

Women in Assur were housewives and businesswomen at the same time. They
managed the household and the maintenance of the building housing the
family, manufactured the textiles that were the main export good. Also,
they could be owners, buyers, and heirs of houses (5–7).

All of that historical heritage is still unread. First, most tablets are
known because of illicit diggings, so they lack needed archaeological
context to reconstruct the original archives of those merchants, so there
will inevitably be tablets whether broken by time or lacking enough data
to determine the context. Second, the corpus is full of homonyms, and
papponymy makes it worse, as there was a practice when sons were usually
named after their fathers and grandfathers. As a result, a single name may
refer to different people in the corpus and the long-term effect of
papponymy is accumulative name redundancy over multiple generations (4).

Working with an overwhelming amount of highly interrelated "big data"
makes the manual reconstruction impossible. As historians note, the lack
of provenance requires using computational models and network analysis to
work with all possible archives (4,8).

*Editorial note: the numbers above are live Zotero (NLM/Vancouver,
citation-sequence) citations, matching the Word draft `article.docx`. The
bracketed `[N]` citations in §2–4 below are a provisional numbering from
before the switch to Zotero and do not yet refer to the same list — they
will be reconciled once those sections get their own Zotero pass.*

**References (Introduction, Zotero/Vancouver numbering):**

1. Larsen MT. *Ancient Kanesh: A Merchant Colony in Bronze Age Anatolia*.
   Cambridge: Cambridge University Press; 2015.
2. Veenhof KR. 'Modern' Features in Old Assyrian Trade. *J Econ Soc Hist
   Orient*. 1997;40(4):336–66.
3. Veenhof KR. *Aspects of Old Assyrian Trade and Its Terminology*. Leiden:
   E. J. Brill; 1972. (Studia et Documenta ad Iura Orientis Antiqui
   Pertinentia; X).
4. Anderson AG. *The Old Assyrian Social Network: An Analysis of the Texts
   from Kültepe-Kanesh (1950–1750 B.C.E.)* [PhD Thesis]. [Cambridge, MA]:
   Harvard University, Department of Near Eastern Languages and
   Civilizations; 2018.
5. Michel C. *Women of Assur and Kanesh: Texts from the Archives of
   Assyrian Merchants*. Atlanta: SBL Press; 2020. (Writings from the
   Ancient World; no. 42).
6. Michel C. Femmes et production textile à Aššur au début du IIe
   millénaire av. J.-C. *Tech Cult*. 2006;46:285–301.
7. Michel C. Women and Real Estate in the Old Assyrian Texts. *Orient*.
   2016;51:83–94.
8. Anderson AG. Disambiguating the Old Assyrian Social Networks Using NLP
   and Network Theory [Internet]. 2019. Available from:
   https://www.researchgate.net/publication/336460070_Disambiguating_the_Old_Assyrian_Social_Networks_Using_NLP_and_Network_Theory

## 2. Literature Review

### 2.1. The Old Assyrian economic system and the tablets as archive

The tablets found in kārum Kanesh uncovered the knowledge about the first
attested commercial system in the world. Foundational works by Veenhof
(1972, 1997) and Larsen (2015) demonstrate that Kanesh was not just a
local trade post, but the hub of a long-distance caravan trade system.
Business deals relied mostly on correspondence and trust while making
contracts, including long-term joint-stock partnerships (naruqqum),
credit management, and conflict resolution at a distance of 1,000
kilometres away.

The archive is not limited to economy but includes the culture, language,
religion, and private lives of individuals — for example, the emotional
correspondence between the men who were merchants in Kanesh and their
wives in Assur, who were entrepreneurs and produced textiles in their
homes. This genre diversity creates a real classification problem for
natural language processing (NLP) models.

### 2.2. Quantitative and network approaches for the Kanesh corpus

Considering the number of tablets found — around 23,500 — computational
and quantitative methods can challenge traditional manual epigraphy.
Barjamovic et al. (2019) used a structural gravity model to analyse a
large dataset of commercial records produced by Assyrian merchants in the
19th century BCE, in order to locate lost ancient cities without knowing
their geographical coordinates.

Quantitative research so far has mostly focused on the biographical
structure of the trade network and cannot cope with a high density of
homonyms — specifically papponymy — which makes identity resolution a
difficult task. To address this, Bamman et al. (2013) proposed a
probabilistic latent-variable model for inferring unique individuals and
their social rank. Later, Anderson (2018, 2019) applied natural language
processing (NLP) and social network analysis (SNA) for homonym
disambiguation and for determining the demographic characteristics of age
cohorts. This body of work does not solve the document classification
problem: reconstructing fragmentary cuneiform tablets remains extremely
difficult without knowing their provenance, and without attributing them
directly to specific private archives or business entities based on
textual and visual features.

### 2.3. Deep learning for ancient languages

Automated processing of ancient texts has developed from rule-based
syntactic analysers to deep learning architectures. Regarding cuneiform,
Lazar et al. (2021) demonstrated the potential of fine-tuning
multilingual BERT (mBERT) on a transliterated Akkadian corpus of roughly
10,000 tablets from the Open Richly Annotated Cuneiform Corpus (ORACC),
showing that masked language modelling (MLM) directly corresponds to
philological lacuna reconstruction based on context.

A parallel line of work on deep-learning text restoration developed
independently in Greek epigraphy. Pythia, the first such system, already
outperformed expert epigraphists on damaged Greek inscriptions, reaching a
character error rate of 30.1% against 57.3% for human epigraphists working
under the same conditions. Its successor, Ithaca, restructured the task
around a single shared transformer torso feeding three separate task
heads — restoration, geographic attribution, and chronological
attribution — trained jointly on 178,551 ancient Greek inscriptions, a
direct precedent for a model that predicts several tablet attributes
jointly rather than restoration alone. Ithaca's own successor, Aeneas,
further extended this architecture with a vision branch, conditioning
geographic attribution on a photograph of the inscription and handling
gaps of unknown length — the direct architectural precedent for combining
textual and visual input within a single classification model.

## 3. Methodology: Selected Examples

Our model performs two tasks jointly from a tablet's transliteration and
photograph together: it restores damaged or illegible spans of text, and
it attributes the tablet to a period, genre, provenience, and language. It
is trained on a large corpus that includes tablets from Kanesh among its
sources; on the held-out test portion of that corpus it reaches 96.2%
accuracy on period, 96.2% on genre, 98.6% on language, and 87.0% on
provenience across 38 possible places of origin — including 100% recall on
Kanesh itself. This section does not describe the model's architecture
further; instead, it presents the kind of material the model is trained
and evaluated on, through a small number of real tablets, each
independently verified against Michel's published translations [10].
Every prediction shown below is the actual output of the trained
checkpoint on these seven tablets, all of which sit in the held-out test
split the model was never trained on. Across the 347 masked tokens in
these seven tablets combined, the model recovers 76.4% on its first guess
and 87.9% within its top three guesses.

**Puzur-Aššur to Waqqurtum (AO 9256), on weaving.** A husband in Kanesh
gives his wife in Assur precise technical instructions for the textiles she
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
famine in Assur:

> *"When you left, you did not leave me silver, not even a single shekel!
> You emptied the house and took (everything) out! After you had gone,
> there was a severe famine in the city (of Aššur) while you had not left
> me barley, not even a single liter!"*
> *([10] Michel 2020, document #128, pp. 215–216)*

Two further tablets from the same archives are cited without a full
quotation. A damaged letter from Imdī-ilum and Ištar-baštī to their
daughter Zizizi (VS 26, 33) reproaches her, after the death of her first
husband, for having remarried an Anatolian and drifted from her family in
Assur *([10] Michel 2020, document #50 "The Cost of a Remarriage," pp.
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
| `qe` (in "i-la₂-qe₂-ši₂," "he will receive it") | `qe` | ✅ |
| `tum` | `ul` | ❌ |
| `zu` (in the witness name "Azutaya") | `hu` | ❌ |

Overall, the model recovered 32 of the 41 masked signs correctly on its
first guess (78%), close to the 76.4% aggregate across all seven tablets
reported above.

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
practice for merchants who spent long periods away from Assur — the
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

## References (§2–4, provisional — pending Zotero pass)

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
