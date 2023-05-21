import pandas as pd
from website import models

def load_excel_data_to_db():
    file_path = 'H:\_python-TrafficAccidentAnalysis-main\teamProject\高雄市事故統計.xlsx' 
    sheets = ['機車事故肇因排行', '小型車事故肇因排行', '自行車事故肇因排行', '行人事故肇因排行']
    
    for sheet in sheets:
        df = pd.read_excel(file_path, sheet_name=sheet,encoding='cp950')

        # 將數據轉換為整數
        df['件數'] = df['件數'].str.replace(',', '').astype(int)
        df['死亡人數'] = df['死亡人數'].astype(int)
        df['受傷人數'] = df['受傷人數'].str.replace(',', '').astype(int)
        df['死傷人數'] = df['死傷人數'].str.replace(',', '').astype(int)

        for index, row in df.iterrows():
            models.Accident.objects.create(
                RANKING=row['排行'],
                CAUSE=row['肇因'],
                COUNT=row['件數'],
                DEATH_COUNT=row['死亡人數'],
                INJURED_COUNT=row['受傷人數'],
                CASUALTIES_COUNT=row['死傷人數'],
                CATEGORY=sheet  # 這次我們使用工作表名稱作為類別
            )
 