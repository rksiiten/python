#!C:\Users\krist\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi

info = cgi.FieldStorage()

nat = info.getvalue("nationality")
sex = info.getvalue("sex")
yearlevel = info.getvalue("year")

flat_fee = 200 #all students
alien_fee = 200 #foreigner
rotc = 100 #male senior
girlscout = 75 #female freshmen and sophomore

if sex == "check":
	sex = "male"
else:
	sex = "female"

tuition = 200

if nat == "foreigner":
	tuition += alien_fee
if sex == "male" and yearlevel == "4":
	tuition += rotc
if sex == "female" and (yearlevel == "1" or yearlevel == "2"):
	tuition += girlscout

print ("Content-type:text/html\r\n\r\n")

print("""
	<html>
		<head>
			<title>TUITION FEE</title>
		</head>
		
		<style>
		body {
			background-image: url(https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700462770.jpg);
			font-family: Helvetica;
			color: #FFFFFF
		}
		div {
			background-color: maroon;
			width: 50%;
			border: 10px solid white;
			padding: 60px;
			margin: auto
		}
		table { 
			width:80%;
			border-spacing: 5px;
		}
		</style>
		
		<body>
			<div>
				<h1 style="text-align:center">TUITION FEE</h1><hr>
				<table>
				<tr>
					<th>
						<p style="text-align:right"><b>NATIONALITY:</b></p>
					</th>
					<td>&nbsp&nbsp""")
print(nat.title())
print("""
					</td>
				</tr>
				<tr>
					<th>
						<p style="text-align:right"><b>SEX:</b></p>
					</th>
					<td>&nbsp&nbsp""")
print(sex.title())
print("""
					</td>
				</tr>
				<tr>
					<th>
						<p style="text-align:right"><b>YEAR LEVEL:</b></p>
					</th>
					<td>&nbsp&nbsp""")
print(yearlevel)
print("""
					</td>
				</tr>
				<tr>
					<th>
						<p style="text-align:right"><b>TUITION FEE:</b></p>
					</th>
					<td>&nbsp&nbsp""")
print("%.2f" %tuition)
print("""
					</td>
				</tr>
			</div>
		</body>
	</html>
""")