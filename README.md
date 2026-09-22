## Kvalitetssäkring & CI/CD Pipeline

Systemet är byggt med ett strikt fokus på mjukvarukvalitet, automatiserad testning och kontinuerlig integration.

* **Enhetstester:** Byggda med Pythons inbyggda `unittest`-ramverk. Verifierar validering, felhantering (custom exceptions) och polymorf orkestrering.
* **Testtäckning:** 98% kodtäckning verifierad via `coverage.py`.
* **CI/CD Pipeline:** Automatiserat arbetsflöde i **GitHub Actions** (`.github/workflows/tests.yml`) som exekverar alla enhetstester och genererar täckningsrapport vid varje `push` och `pull request`.

### Kör tester och täckningsrapport lokalt:
```bash
# Kör alla enhetstester
python -m unittest discover -s tests

# Generera täckningsrapport
coverage run -m unittest discover -s tests
coverage report -m