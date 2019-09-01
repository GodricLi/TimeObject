# _*_ coding=utf-8 _*_

import pandas as pd
import dateutil

"""时间对象"""

# 灵活处理时间对象：dateutil
date = dateutil.parser.parse('02/03/2012')
print(date)
# 成组处理pd.to_datetime()
date_pd = pd.to_datetime(['2012/02/03', '2012/JAN/03'])
print(date_pd)
