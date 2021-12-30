from tabulate import tabulate

mydata = [("1","China*","1270","1376","1416")
,("2","India","1053","1311","1528"),
("3","United states","283","322","356"),
("4","Indonesia","212","258","295"),
("5","pakistan","136","208","245"),
("6","brazil","123","206","228"),
("7","Nigeria","131","182","263"),
("8","Bangladesh","146","161","186"),
("9","Russia","103","146","149"),
("10","Mexico","103","127","148")]

headers = ["#","Top ten most populous countries","2000","2015","2030*"]
print(tabulate(mydata, headers=headers, tablefmt="gride"))