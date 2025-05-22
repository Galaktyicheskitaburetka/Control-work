#n1
import pandas as pd
df_excel = pd.read_excel('ababaababa.xlsx')
print(df_excel)

#n2
print(df_excel.head(5))
#3
import matplotlib.pyplot as plt
values = [13,18,37,48,25]
plt.plot(values)
plt.title('эээ ну типо график')
plt.xlabel('индекс')
plt.ylabel('значение')
plt.show()
