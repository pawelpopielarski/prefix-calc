# prefix-calc

Done with python 3.8.5<br>
Done with Flask

Part 1 - PrefixCalculator.py<br>
Part 2 - InfixCalculator.py<br>

Bonus -  CalcService.py<br>
curl -H "Content-Type: application/json" -X POST <url>/calc/v1/infix -d '{"statement":"( 1 + ( 2 * 3 ) )"}'<br>
curl -H "Content-Type: application/json" -X POST <url>/calc/v1/prefix -d '{"statement":"- / 10 + 1 1 * 1 2"}'<br>