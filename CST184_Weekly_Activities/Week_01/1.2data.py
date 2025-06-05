
# --- SETS ---
# Countries addressing SDG goals

sdg6 = {"Nepal", "India", "Kenya"}
sdg13 = {"Kenya", "Germany", "Brazil"}

print("Countries working on both SDG6 and SDG13:", sdg6 & sdg13)
print("Countries only in SDG6:", sdg6 - sdg13)

print("\n---\n")

# --- LIST OF TUPLES ---
# (Country, SDG Score)

sdg_scores = [("Nepal", 65), ("Kenya", 58), ("Brazil", 70)]

print("SDG Scores:")
for country, score in sdg_scores:
    print(f"{country} → {score}")

print("\n---\n")

# --- DICTIONARY: CO₂ EMISSIONS PER CAPITA ---

emissions = {
    "Nepal": 0.3,
    "Kenya": 0.5,
    "Brazil": 2.1
}

print("CO₂ Emissions per capita:")
for country in emissions:
    print(f"{country}: {emissions[country]} tonnes")

# Accessing specific value
print("\nBrazil's emissions:", emissions["Brazil"], "tonnes")

print("\n---\n")

# --- NESTED DICTIONARIES: POPULATION BY REGION ---

population_by_region = {
    "Asia": {"Nepal": 30, "India": 1400},
    "Africa": {"Kenya": 54, "Nigeria": 206}
}

print("Population by region:")
for region, countries in population_by_region.items():
    print(f"\n{region}:")
    for country, pop in countries.items():
        print(f"  {country} → {pop} million")
