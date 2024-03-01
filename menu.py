import pandas as pd
from bskinchanger import skinchanger,push_via_adb
# Загрузка данных из файлов CSV
characters_df = pd.read_csv("characters.csv")
ru_df = pd.read_csv("ru.csv")
en_df = pd.read_csv("texts.csv")
skins_df = pd.read_csv("skins.csv")
skins_conf_df = pd.read_csv("skin_confs.csv")
# Объединение данных по столбцу TID
merged_df = pd.merge(characters_df, ru_df, on="TID")
merged_df = pd.merge(merged_df, en_df, on="TID")
merged_skins = pd.merge(skins_df, skins_conf_df, on="Name")
merged_skins = pd.merge(merged_skins, ru_df, on="TID")
merged_skins = pd.merge(merged_skins, en_df, on="TID")

# Сортировка по алфавиту и обновление индексов
merged_df.sort_values(by="Name", inplace=True)
merged_df.reset_index(drop=True, inplace=True)

# Создание словаря для привязки номеров к именам
name_dict = {i + 1: name for i, name in enumerate(merged_df["Name"])}


# Функция для поиска значения RU и DefaultSkin по имени или номеру
def find_info_by_input(user_input):
    try:
        user_input = int(user_input)
        name = name_dict[user_input]
    except ValueError:
        name = user_input
    row = merged_df.loc[merged_df["Name"] == name]
    name_brawler = row["Name"].values[0]
    ru_value = row["RU"].values[0]
    en_value = row["EN"].values[0]
    default_skin = row["DefaultSkin"].values[0]
    return ru_value, default_skin, name_brawler, en_value


# Вывод списка имен для выбора
print("Select brawler:")
for i, row in merged_df.iterrows():
    print(f"{i + 1}. {row['Name']} - {row['RU']} - {row['EN']}")

# Запрос ввода пользователя и вывод данных
user_input = input("Enter a Name value or number: ")
ru_value, default_skin, name_brawler, en_value = find_info_by_input(user_input)

print(f"Name: {name_brawler}")
print(f"RU: {ru_value}")
print(f"EN: {en_value}")
print(f"DefaultSkin: {default_skin}")
filtered = merged_skins.loc[merged_skins["Character"] == name_brawler]
skins_names = []
for skin in filtered.values:
    if "Default" not in skin[0]:
        skins_names.append({"name":skin[1], "RU":skin[-2], "EN":skin[-1]})
for num in range(len(skins_names)):
    print(f"{num+1}. {skins_names[num]['name']} - {skins_names[num]['RU']} - {skins_names[num]['EN']}")
select_input = int(input("Select skin number: "))
skinchanger(default_skin, skins_names[select_input-1]['name'])
push = input("push via adb y/n: ").lower()
if push == 'y':
    push_via_adb()