import os
import sys

#print(sys.argv[1])

if sys.argv[1] == "A":
	os.popen("curl http://7.7.7.9/A_CH_TV.php -s")

elif sys.argv[1] == "B":
	os.popen("curl http://7.7.7.9/B_CH_TV.php -s")

else:
	print("Faulty argument")
exit

