import pandas as pd

# 1) Charger le CSV
df = pd.read_csv("data/era5_z.csv")

# 2) Aperçu
print(df.head())
print("Shape:", df.shape)
print("Colonnes:", df.columns.tolist())

# Nigeria
df_ng = df[
    df["latitude"].between(4.2, 14.7) &
    df["longitude"].between(2.7, 14.7)
]

df_ng["valid_time"] = pd.to_datetime(df["valid_time"])

print(df_ng)


# 3) Exemple: récupérer la valeur z au point le plus proche de (lat, lon)
# lat0, lon0 = 48.85, 2.35  # Paris (exemple)
# i = ((df["latitude"] - lat0).abs() + (df["longitude"] - lon0).abs()).idxmin()
# print("Point le plus proche:", df.loc[i, ["latitude", "longitude"]].to_dict())
# print("z =", df.loc[i, "z"])
