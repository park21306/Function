unique_df = df.drop_duplicates(subset="columns ที่ต้องการเลือกว่าดูข้อมูลซ้ำ")[["columns ที่ต้องการ",]].copy()
unique_df["columns ที่ต้องการ"] = unique_df["columns ที่ต้องการเลือกว่าดูข้อมูลซ้ำ"].str.strip()
