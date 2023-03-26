#!C:\Users\krist\AppData\Local\Programs\Python\Python38-32\python.exe

print ("Content-type:text/html\r\n\r\n")

print("""
	<html>
		<head>
			<title>TUITION FORM</title>
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
			width:100%;
			border-spacing: 5px;
		}
		</style>
		
		<body>
			<div>
				
				<h1 style="text-align:center">TUITION FORM</h1><hr>
				
				<form action = "tuitioncalculate.cgi" method = "get">
					
					<table>
					<tr>
						<th>
							<p style="text-align:right"><b>NATIONALITY: </b></p>
						</th>
						<td>&nbsp&nbsp
							<input type = "radio" name = "nationality" value = "filipino"> Filipino
							<input type = "radio" name = "nationality" value = "foreigner"> Foreigner
						</td>
					</tr>
					
					<tr>
						<th>
							<p style="text-align:right"><b>SEX: </b></p>
						</th>
						<td>&nbsp&nbsp
							<input type = "checkbox" name = "sex" value = "check">
						</td>
					</tr>
					
					<tr>
						<th colspan="2">
							<p style="font-size: 12px;color:lightgray"><i>NOTE: Check if you are Male, Uncheck if you are Female.</i></p>
						</th>
					</tr>
					
					<tr>
						<th>
							<p style="text-align:right"><b>YEAR LEVEL: </b></p>
						</th>
						<td>&nbsp&nbsp
							<select name = "year">
							<option value = "1"> 1 </option>
							<option value = "2"> 2 </option>
							<option value = "3"> 3 </option>
							<option value = "4"> 4 </option>
						</select>
						</td>
					</tr>
					</table>
					
					<p style="text-align:center"><input type = "submit" value = "SUBMIT"></p>	
					
				</form>
			</div>
		</body>
	</html>
""")