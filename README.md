# EcoHeat — strona wizytówkowa

Klient: **EcoHeat Agnieszka Belka** (Wrocław / Pichlice), montaż pomp ciepła.
Zastępuje starą stronę na Google Sites (ecoheatab.pl).

**Podgląd na żywo:** https://newhope77.github.io/ecoheat-site/

## Zawartość
- `index.html` — cała strona (one-pager, PL)
- `assets/` — logo (przetworzone na PNG z przezroczystym tłem), favicony, OG image
- `assets/realizacje/` — zdjęcia realizacji pobrane z fanpage'a
- `_CNAME-po-przepieciu-domeny` — **zmienić nazwę na `CNAME`** dopiero po przekierowaniu DNS ecoheatab.pl na GitHub Pages

## Wymagania klienta (z rozmowy)
- profesjonalny wygląd, budujący zaufanie ✔
- 2–3 oferty ✔ (3 pakiety Panasonic Aquarea Gen L: 5 / 7 / 9 kW) — **bez cen** (decyzja z 31.08.2026)
- tylko pompy ciepła Panasonic, BEZ oferty ogrzewania podłogowego ✔
- zdjęcia realizacji ✔ + realizacje jako posty z fanpage'a ✔ (Facebook Page Plugin)
- linki do fanpage'a ✔
- ta sama domena: ecoheatab.pl
- bez hostingu → GitHub Pages

## Baner na stronie głównej
`assets/hero-banner.jpg` (2200×940) i `assets/hero-banner-mobile.jpg` (800×2050) — złożone z dwóch
**oficjalnych materiałów Panasonic** (cdn.aircon.panasonic.eu, kampania Aquarea L):
- **pierwszy plan:** ostry render jednostki zewnętrznej Aquarea Gen L z kanału alfa
  (`01-Aquarea-L-Banner.png`, 1260×1040, PNG z przezroczystością — wycięty sam agregat, bez plakietek nagród),
- **tło:** wizualizacja domu z `05-Aquarea-L.jpg`, rozmyta (efekt głębi ostrości) i przyciemniona pod tekst.

Dzięki temu to, na co patrzy oko (urządzenie), jest w pełnej ostrości, a niska rozdzielczość
źródłowej wizualizacji tła jest niewidoczna. Logo „Panasonic" na obudowie jest w tej skali nieczytelne,
więc pierwszy ekran pozostaje bez nazwy marki.

⚠️ To materiały chronione prawem autorskim Panasonic. Autoryzowani instalatorzy zwykle mogą korzystać
z materiałów marketingowych producenta — **klient powinien to potwierdzić u swojego dystrybutora Panasonic**
(wyższa rozdzielczość jest dostępna po zalogowaniu w Panasonic PRO Club).
Alternatywa: własne zdjęcie realizacji w wysokiej rozdzielczości — wtedy podmieniamy plik.
Na darmowych stockach (Pexels/Unsplash/Pixabay) nie ma zdjęcia pompy ciepła bez logo konkurencji (alpha innotec).

## Do uzupełnienia od klienta
- lepszej jakości zdjęcia realizacji (obecne pobrane z FB, max ~800 px)
- logo w oryginale (wektor / PNG bez tła) — obecne odtworzone z JPG
- dane do domeny (panel rejestratora) do przepięcia DNS
