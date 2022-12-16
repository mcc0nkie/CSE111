# %%
from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date)

# %%
one_day = timedelta(days=1)
yesterday = current_date - one_day
# %%
yesterday
# %%
print(yesterday)
# %%
print(yesterday.day)
# %%
birthday = '04/11/1996'
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print(birthday_date)
# %%
current_date = current_date.year.day
# %%
