import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

prices = data['Цена']

# Вычисление средней цены
average_price = prices.mean()

# Построение гистограммы
plt.hist(prices, bins=15, edgecolor='black', alpha=0.7)

# Добавление вертикальной линии для средней цены
plt.axvline(average_price, color='red', linestyle='dashed', linewidth=1, label=f'Средняя цена: {average_price:.2f}')

# Добавление легенды
plt.legend()

plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()