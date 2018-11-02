# pp-etoro-hist-tab-web
autohtml.py generates a static html <tradername>.html with historical data of the last two years
	
**Usage:** `python autohtml.py -t < etoro tradername> -d <buy date as YYY-MM-DD> -w <invested value in $>`
	
The generated table will contain values in $ calculated from the invested value at the buy date

Supposing the investment started at 2018-01-01 with an invested value of $500, the present value shows how your investment has developed from the 2018-01-01 until the present day. The historical data continues toward past values until 2016-01-01.
  
