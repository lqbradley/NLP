import pandas as pd
import tabula
import re

def degree_list_db():
    return ["business", "computer science", "management", "tourism", "engineering",
            "economics", "IM", "health",
            "design", "psychology", "sport", "logistics"]

pdf_path = "https://www.th-deg.de/Studierende/Auslandsstudium/partnerunis_studenten.pdf"
df_list = tabula.read_pdf(pdf_path, pages='all')
df = pd.concat(df_list)
df.to_csv('test.csv', index=False)

'''Cleaning the data'''
raw_df = pd.read_csv('test.csv')
raw_df.dropna(how='all', inplace=True)
last_index = raw_df.index[-1]
extra_rows = [raw_df.iloc[0, i:i + 5] for i in range(0, len(df.columns), 5)]
for row in extra_rows:
    last_index += 1
    raw_df.loc[last_index] = row

raw_df.drop(raw_df.columns[5: len(df.columns)], axis=1, inplace=True, errors='ignore')
raw_df.ffill(inplace=True)
raw_df.drop_duplicates(inplace=True, keep='first')

def contains_url(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return bool(url_pattern.search(text))

url_mask = raw_df.iloc[:, 1].apply(contains_url)
merged_df = raw_df[~url_mask]
rows_to_drop = []

for index in range(1, len(merged_df)):
    prev_row = merged_df.iloc[index - 1]
    this_row = merged_df.iloc[index]
    merged_row = pd.concat([prev_row, this_row], ignore_index=True)  # Ensure ignore_index=True
    merged_df.loc[index] = merged_row

    partner_university = merged_df.iloc[index, 1]
    if partner_university in degree_list_db():
        rows_to_drop.append(index)

# Drop rows outside the loop
merged_df.drop(index=rows_to_drop, inplace=True, errors='ignore')

raw_unis = []
study_program = 'business'
erasmus = True

for index, row in merged_df.iterrows():
    partner_university = row.iloc[1]
    study_fields = row.iloc[2]

    if study_program is not None:
        if erasmus:
            if ((study_program.lower() in study_fields.lower()
                 and "erasmus".capitalize() in study_fields)
                    or study_fields == 'All Study Programs'):
                raw_unis.append(partner_university)
        else:
            if (study_program.lower() in study_fields.lower()
                    or study_fields == 'All Study Programs'):
                raw_unis.append(partner_university)
    else:
        if study_fields == "All Study Programs":
            raw_unis.append(partner_university)

universities = [item for item in raw_unis if 'www.' not in item]
print(universities)
