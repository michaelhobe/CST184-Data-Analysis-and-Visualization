
# --- SETS ---

# Create two sets of countries working on different SDGs
sdg6_countries = {"Nepal", "Kenya", "Brazil", "India"}
sdg13_countries = {"Brazil", "Kenya", "Norway", "Germany"}

# Union: All countries involved in either SDG
print("Union (SDG6 ∪ SDG13):", sdg6_countries.union(sdg13_countries))

# Intersection: Countries working on both
print("Intersection (SDG6 ∩ SDG13):", sdg6_countries.intersection(sdg13_countries))

# Difference: Countries working only on SDG6
print("Difference (SDG6 - SDG13):", sdg6_countries.difference(sdg13_countries))

# Cardinality
print("Number of countries working on SDG6:", len(sdg6_countries))

print("\n---\n")

# --- RELATIONS (as tuples) ---

# Each pair represents (Country, SDG Score)
sdg_scores = [("Nepal", 65), ("Kenya", 58), ("Brazil", 70)]

print("SDG Scores (as relations):")
for country, score in sdg_scores:
    print(f"{country}: {score}")

print("\n---\n")

# --- FUNCTIONS (as dictionaries) ---

# Representing SDG progress as a function: one value per country
emissions_per_capita = {
    "Nepal": 0.3,
    "Kenya": 0.5,
    "Brazil": 2.1
}

print("CO₂ emissions per capita:")
for country, emissions in emissions_per_capita.items():
    print(f"{country}: {emissions} tonnes")

# Example: Accessing a value from the function
print("\nBrazil's emissions per capita:", emissions_per_capita["Brazil"])

