<!---->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>LiveData</title>
<style type="text/css">

body {
	margin: 0px;
	font-family: arial;
	font-size: 11px;
}
.tblheader {
	color: #003254;
	background-color: #F0F7A9;
	font-weight: bold;
	padding-right: 5px;	
}
.mycell {
	padding-right: 5px;	
}
#data td {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #cccccc;
}
.style1 {
	color: #000066;
	font-weight: bold;
}
.style2 {
    padding-right: 5px; 
    font-weight: bold;	
	 }
-->
</style>
<script language="javascript" type="text/javascript">
function updatePage() {
	var divobj = document.getElementById("livedata");
	var XMLHttpRequestObject = false;
	try  {  XMLHttpRequestObject = new XMLHttpRequest();  }
	catch (e) {
		try {  XMLHttpRequestObject = new ActiveXObject("Msxml2.XMLHttp");  }
		catch (e) { 
			try  { XMLHttpRequestObject = new ActiveXObject("Microsoft.XMLHttp");  }
			catch (e) {
				return false; 
			}
		}
	}
		
	if ((XMLHttpRequestObject) && (divobj)) {	
		
		XMLHttpRequestObject.onreadystatechange = function()
		{
			if ((XMLHttpRequestObject.readyState == 4) && (XMLHttpRequestObject.status == 200)) {
				returnStr = XMLHttpRequestObject.responseText;
				divobj.innerHTML = returnStr;
			}
		}
	}
		
	XMLHttpRequestObject.open("GET", "livedata.asp?data", true);
	XMLHttpRequestObject.send(null);
	setTimeout("updatePage()", 60000);
}
window.onload = function() {
	updatePage();
}
</script>
<script type="text/javascript" language="JavaScript">
    function getCalendarDate() {
        var months = new Array(13);
        months[0] = "Jan";
        months[1] = "Feb";
        months[2] = "Mar";
        months[3] = "Apr";
        months[4] = "May";
        months[5] = "June";
        months[6] = "July";
        months[7] = "Aug";
        months[8] = "Sep";
        months[9] = "Oct";
        months[10] = "Nov";
        months[11] = "Dec";
        var now = new Date();
        var monthnumber = now.getMonth();
        var monthname = months[monthnumber];
        var monthday = now.getDate();
        var year = now.getYear();
        if (year < 2000) { year = year + 1900; }
        var dateString = monthname +
' ' +
monthday +
', ' +
year;
        return dateString;
    } // function getCalendarDate()
</script>
</head>
<body>
	<div id="livedata">

<table width="650" border="0" cellpadding="4" cellspacing="0" id="data">
	<tr>
		<td colspan="9" valign="middle" align=right>
		<!--<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF">
				<tr>-->
				<!--
			          <td align="right" width="20%" bgcolor="#FFFFFF">-->
			          <img src="nellydata.jpg" alt="nellydata" height=27 width=100 /><br />
			         <font size=1>NSE Live Feed: Wed 3:16:00 PM</font>
			  <!--  </tr>
			     <tr>
					<td valign="bottom" width="70%" align="right" nowrap="nowrap" style="background-color:#FFFFFF;padding-left:3px;font-size:9px">NSE Live Feed: Wed 3:16:00 PM&nbsp;</td>
				</tr>
			</table>--></td>
		</tr>
	<tr>
		<td width="1%" valign="middle" class="tblheader">#</td>
		<td width="15%" align="left" valign="middle" class="tblheader" style="padding-left: 5px;"><strong>Stock</strong></td>
		<td width="12%" align="right" valign="middle" class="tblheader"><strong>Yesterday</strong>
			</td>
		<td width="12%" align="right" valign="middle" class="tblheader"><strong>Today</strong></td>
		<td width="12%" align="center" valign="middle" class="tblheader"><strong>Change</strong></td>
		<td width="12%" align="center" valign="middle" class="tblheader"><strong></strong></td>
		<td width="13%" align="center" valign="middle" class="tblheader"><strong>% Change</strong></td>
		<td width="13%" align="right" valign="middle" class="tblheader"><strong>High</strong>
			</td>
		<td width="13%" align="right" valign="middle" class="tblheader"><strong>Low</strong>
			</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">1</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>AccessKenya Group</strong></td>
		<td width="" align="right" class="mycell">9.55</td>
		<td width="" align="right" class="style2">9.55</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">0.00</td>
		<td width="" align="right" class="mycell">0.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">2</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>ARM Cement Ltd</strong></td>
		<td width="" align="right" class="mycell">94.00</td>
		<td width="" align="right" class="style2">93.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-1.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.06 %</td>
		<td width="" align="right" class="mycell">94.00</td>
		<td width="" align="right" class="mycell">93.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">3</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Bamburi Cement</strong></td>
		<td width="" align="right" class="mycell">210.00</td>
		<td width="" align="right" class="style2">210.00</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">214.00</td>
		<td width="" align="right" class="mycell">210.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">4</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Barclays Bank</strong></td>
		<td width="" align="right" class="mycell">17.95</td>
		<td width="" align="right" class="style2">17.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.45</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-2.51 %</td>
		<td width="" align="right" class="mycell">18.00</td>
		<td width="" align="right" class="mycell">17.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">5</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>BOC Kenya</strong></td>
		<td width="" align="right" class="mycell">189.00</td>
		<td width="" align="right" class="style2">178.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-11.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-5.82 %</td>
		<td width="" align="right" class="mycell">185.00</td>
		<td width="" align="right" class="mycell">175.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">6</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>British American Tobacco</strong></td>
		<td width="" align="right" class="mycell">574.00</td>
		<td width="" align="right" class="style2">545.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-29.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-5.05 %</td>
		<td width="" align="right" class="mycell">560.00</td>
		<td width="" align="right" class="mycell">540.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">7</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>British-American Investments</strong></td>
		<td width="" align="right" class="mycell">19.85</td>
		<td width="" align="right" class="style2">19.30</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.55</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-2.77 %</td>
		<td width="" align="right" class="mycell">19.90</td>
		<td width="" align="right" class="mycell">18.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">8</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Car & General</strong></td>
		<td width="" align="right" class="mycell">36.75</td>
		<td width="" align="right" class="style2">45.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">8.25</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">22.45 %</td>
		<td width="" align="right" class="mycell">50.00</td>
		<td width="" align="right" class="mycell">42.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">9</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Carbacid Investments</strong></td>
		<td width="" align="right" class="mycell">42.50</td>
		<td width="" align="right" class="style2">39.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-3.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-7.06 %</td>
		<td width="" align="right" class="mycell">42.50</td>
		<td width="" align="right" class="mycell">39.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">10</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Centum Investment</strong></td>
		<td width="" align="right" class="mycell">37.75</td>
		<td width="" align="right" class="style2">37.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.25</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.66 %</td>
		<td width="" align="right" class="mycell">38.00</td>
		<td width="" align="right" class="mycell">37.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">11</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>CFC Insurance Holdings</strong></td>
		<td width="" align="right" class="mycell">16.00</td>
		<td width="" align="right" class="style2">15.45</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.55</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-3.44 %</td>
		<td width="" align="right" class="mycell">16.00</td>
		<td width="" align="right" class="mycell">15.05</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">12</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>CFC Stanbic</strong></td>
		<td width="" align="right" class="mycell">97.50</td>
		<td width="" align="right" class="style2">92.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-5.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-5.13 %</td>
		<td width="" align="right" class="mycell">96.00</td>
		<td width="" align="right" class="mycell">90.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">13</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>CIC Insurance</strong></td>
		<td width="" align="right" class="mycell">6.55</td>
		<td width="" align="right" class="style2">6.65</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">0.10</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">1.53 %</td>
		<td width="" align="right" class="mycell">6.90</td>
		<td width="" align="right" class="mycell">6.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">14</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>CMC Holdings</strong></td>
		<td width="" align="right" class="mycell">13.50</td>
		<td width="" align="right" class="style2">13.50</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">0.00</td>
		<td width="" align="right" class="mycell">0.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">15</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Cooperative Bank</strong></td>
		<td width="" align="right" class="mycell">19.00</td>
		<td width="" align="right" class="style2">18.40</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.60</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-3.16 %</td>
		<td width="" align="right" class="mycell">18.90</td>
		<td width="" align="right" class="mycell">18.05</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">16</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Crown Paints</strong></td>
		<td width="" align="right" class="mycell">84.00</td>
		<td width="" align="right" class="style2">85.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">1.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">1.19 %</td>
		<td width="" align="right" class="mycell">85.00</td>
		<td width="" align="right" class="mycell">84.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">17</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Diamond Trust Bank</strong></td>
		<td width="" align="right" class="mycell">223.00</td>
		<td width="" align="right" class="style2">224.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">1.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.45 %</td>
		<td width="" align="right" class="mycell">224.00</td>
		<td width="" align="right" class="mycell">221.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">18</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>EA Breweries</strong></td>
		<td width="" align="right" class="mycell">279.00</td>
		<td width="" align="right" class="style2">278.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-1.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.36 %</td>
		<td width="" align="right" class="mycell">279.00</td>
		<td width="" align="right" class="mycell">277.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">19</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>EA Cables</strong></td>
		<td width="" align="right" class="mycell">16.85</td>
		<td width="" align="right" class="style2">16.55</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.30</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.78 %</td>
		<td width="" align="right" class="mycell">16.80</td>
		<td width="" align="right" class="mycell">16.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">20</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>EA Portland Cement</strong></td>
		<td width="" align="right" class="mycell">74.00</td>
		<td width="" align="right" class="style2">71.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-2.50</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-3.38 %</td>
		<td width="" align="right" class="mycell">73.00</td>
		<td width="" align="right" class="mycell">70.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">21</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Eaagads</strong></td>
		<td width="" align="right" class="mycell">26.75</td>
		<td width="" align="right" class="style2">26.75</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">27.00</td>
		<td width="" align="right" class="mycell">26.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">22</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Equity Bank</strong></td>
		<td width="" align="right" class="mycell">32.75</td>
		<td width="" align="right" class="style2">32.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.75</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-2.29 %</td>
		<td width="" align="right" class="mycell">33.00</td>
		<td width="" align="right" class="mycell">32.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">23</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Eveready EA</strong></td>
		<td width="" align="right" class="mycell">2.90</td>
		<td width="" align="right" class="style2">3.05</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">0.15</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">5.17 %</td>
		<td width="" align="right" class="mycell">3.15</td>
		<td width="" align="right" class="mycell">2.85</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">24</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Express</strong></td>
		<td width="" align="right" class="mycell">4.55</td>
		<td width="" align="right" class="style2">4.55</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">4.55</td>
		<td width="" align="right" class="mycell">4.55</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">25</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Home Afrika Ltd</strong></td>
		<td width="" align="right" class="mycell">6.10</td>
		<td width="" align="right" class="style2">6.15</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">0.05</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.82 %</td>
		<td width="" align="right" class="mycell">6.40</td>
		<td width="" align="right" class="mycell">6.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">26</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Housing Finance</strong></td>
		<td width="" align="right" class="mycell">33.50</td>
		<td width="" align="right" class="style2">32.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-1.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-2.99 %</td>
		<td width="" align="right" class="mycell">33.25</td>
		<td width="" align="right" class="mycell">31.25</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">27</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>I&M bank</strong></td>
		<td width="" align="right" class="mycell">138.00</td>
		<td width="" align="right" class="style2">138.00</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">145.00</td>
		<td width="" align="right" class="mycell">138.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">28</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Jubilee Holdings</strong></td>
		<td width="" align="right" class="mycell">313.00</td>
		<td width="" align="right" class="style2">318.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">5.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">1.60 %</td>
		<td width="" align="right" class="mycell">320.00</td>
		<td width="" align="right" class="mycell">315.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">29</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Kakuzi</strong></td>
		<td width="" align="right" class="mycell">105.00</td>
		<td width="" align="right" class="style2">114.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">9.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">8.57 %</td>
		<td width="" align="right" class="mycell">115.00</td>
		<td width="" align="right" class="mycell">98.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">30</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Kapchorua Tea</strong></td>
		<td width="" align="right" class="mycell">152.00</td>
		<td width="" align="right" class="style2">149.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-3.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.97 %</td>
		<td width="" align="right" class="mycell">167.00</td>
		<td width="" align="right" class="mycell">148.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">31</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>KCB Bank</strong></td>
		<td width="" align="right" class="mycell">46.25</td>
		<td width="" align="right" class="style2">45.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.75</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.62 %</td>
		<td width="" align="right" class="mycell">46.25</td>
		<td width="" align="right" class="mycell">45.25</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">32</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Kengen</strong></td>
		<td width="" align="right" class="mycell">13.15</td>
		<td width="" align="right" class="style2">12.85</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.30</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-2.28 %</td>
		<td width="" align="right" class="mycell">13.00</td>
		<td width="" align="right" class="mycell">12.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">33</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>KenolKobil</strong></td>
		<td width="" align="right" class="mycell">9.55</td>
		<td width="" align="right" class="style2">9.35</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.20</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-2.09 %</td>
		<td width="" align="right" class="mycell">9.60</td>
		<td width="" align="right" class="mycell">9.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">34</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Kenya Airways</strong></td>
		<td width="" align="right" class="mycell">12.95</td>
		<td width="" align="right" class="style2">12.80</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.15</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.16 %</td>
		<td width="" align="right" class="mycell">13.00</td>
		<td width="" align="right" class="mycell">12.75</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">35</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Kenya Orchads</strong></td>
		<td width="" align="right" class="mycell">3.00</td>
		<td width="" align="right" class="style2">3.00</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">0.00</td>
		<td width="" align="right" class="mycell">0.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">36</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Kenya Power & Lighting</strong></td>
		<td width="" align="right" class="mycell">15.10</td>
		<td width="" align="right" class="style2">14.85</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.25</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.66 %</td>
		<td width="" align="right" class="mycell">16.00</td>
		<td width="" align="right" class="mycell">14.85</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">37</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Kenya Re-Insurance</strong></td>
		<td width="" align="right" class="mycell">19.45</td>
		<td width="" align="right" class="style2">19.15</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.30</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.54 %</td>
		<td width="" align="right" class="mycell">19.35</td>
		<td width="" align="right" class="mycell">19.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">38</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Limuru Tea</strong></td>
		<td width="" align="right" class="mycell">625.00</td>
		<td width="" align="right" class="style2">625.00</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">0.00</td>
		<td width="" align="right" class="mycell">0.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">39</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Longhorn Kenya Ltd</strong></td>
		<td width="" align="right" class="mycell">15.00</td>
		<td width="" align="right" class="style2">14.95</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.05</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.33 %</td>
		<td width="" align="right" class="mycell">14.95</td>
		<td width="" align="right" class="mycell">14.95</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">40</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Marshalls EA</strong></td>
		<td width="" align="right" class="mycell">11.95</td>
		<td width="" align="right" class="style2">11.95</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">12.00</td>
		<td width="" align="right" class="mycell">11.95</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">41</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Mumias Sugar</strong></td>
		<td width="" align="right" class="mycell">3.10</td>
		<td width="" align="right" class="style2">3.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.10</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-3.23 %</td>
		<td width="" align="right" class="mycell">3.15</td>
		<td width="" align="right" class="mycell">2.95</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">42</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Nation Media Group</strong></td>
		<td width="" align="right" class="mycell">318.00</td>
		<td width="" align="right" class="style2">320.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">2.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.63 %</td>
		<td width="" align="right" class="mycell">320.00</td>
		<td width="" align="right" class="mycell">320.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">43</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>National Bank of Kenya</strong></td>
		<td width="" align="right" class="mycell">35.00</td>
		<td width="" align="right" class="style2">34.75</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.25</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.71 %</td>
		<td width="" align="right" class="mycell">35.75</td>
		<td width="" align="right" class="mycell">34.75</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">44</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>NIC Bank</strong></td>
		<td width="" align="right" class="mycell">61.00</td>
		<td width="" align="right" class="style2">60.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.50</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.82 %</td>
		<td width="" align="right" class="mycell">61.00</td>
		<td width="" align="right" class="mycell">60.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">45</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Olympia Capital</strong></td>
		<td width="" align="right" class="mycell">4.75</td>
		<td width="" align="right" class="style2">4.75</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">5.00</td>
		<td width="" align="right" class="mycell">4.60</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">46</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Pan Africa Insurance</strong></td>
		<td width="" align="right" class="mycell">95.00</td>
		<td width="" align="right" class="style2">94.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.50</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.53 %</td>
		<td width="" align="right" class="mycell">95.00</td>
		<td width="" align="right" class="mycell">93.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">47</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Rea Vipingo Plantations</strong></td>
		<td width="" align="right" class="mycell">27.50</td>
		<td width="" align="right" class="style2">27.50</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">0.00</td>
		<td width="" align="right" class="mycell">0.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">48</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Safaricom Limited</strong></td>
		<td width="" align="right" class="mycell">12.05</td>
		<td width="" align="right" class="style2">11.85</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.20</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.66 %</td>
		<td width="" align="right" class="mycell">12.05</td>
		<td width="" align="right" class="mycell">11.75</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">49</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Sameer Africa</strong></td>
		<td width="" align="right" class="mycell">6.10</td>
		<td width="" align="right" class="style2">6.20</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">0.10</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">1.64 %</td>
		<td width="" align="right" class="mycell">6.30</td>
		<td width="" align="right" class="mycell">6.10</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">50</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Sasini</strong></td>
		<td width="" align="right" class="mycell">18.80</td>
		<td width="" align="right" class="style2">19.65</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">0.85</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">4.52 %</td>
		<td width="" align="right" class="mycell">19.95</td>
		<td width="" align="right" class="mycell">19.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">51</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Scangroup</strong></td>
		<td width="" align="right" class="mycell">53.00</td>
		<td width="" align="right" class="style2">52.50</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.50</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.94 %</td>
		<td width="" align="right" class="mycell">54.00</td>
		<td width="" align="right" class="mycell">52.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">52</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Standard Chartered Bank</strong></td>
		<td width="" align="right" class="mycell">303.00</td>
		<td width="" align="right" class="style2">302.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-1.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.33 %</td>
		<td width="" align="right" class="mycell">304.00</td>
		<td width="" align="right" class="mycell">301.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">53</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Standard Group</strong></td>
		<td width="" align="right" class="mycell">28.25</td>
		<td width="" align="right" class="style2">28.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.25</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.88 %</td>
		<td width="" align="right" class="mycell">28.25</td>
		<td width="" align="right" class="mycell">28.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">54</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Total Kenya</strong></td>
		<td width="" align="right" class="mycell">23.75</td>
		<td width="" align="right" class="style2">23.75</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">24.75</td>
		<td width="" align="right" class="mycell">23.75</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">55</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>TPS EA Serena</strong></td>
		<td width="" align="right" class="mycell">47.25</td>
		<td width="" align="right" class="style2">45.25</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-2.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-4.23 %</td>
		<td width="" align="right" class="mycell">47.25</td>
		<td width="" align="right" class="mycell">45.25</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">56</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Transcentury Limited</strong></td>
		<td width="" align="right" class="mycell">30.00</td>
		<td width="" align="right" class="style2">29.75</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.25</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-0.83 %</td>
		<td width="" align="right" class="mycell">30.00</td>
		<td width="" align="right" class="mycell">29.50</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">57</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Umeme</strong></td>
		<td width="" align="right" class="mycell">13.00</td>
		<td width="" align="right" class="style2">13.00</td>
		<td width="0" align="center" class="mycell"><strong></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/flat.jpg" height="2" width="8"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">0.00 %</td>
		<td width="" align="right" class="mycell">0.00</td>
		<td width="" align="right" class="mycell">0.00</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">58</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Unga Group</strong></td>
		<td width="" align="right" class="mycell">20.00</td>
		<td width="" align="right" class="style2">19.75</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#006734;">-0.25</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/down.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">-1.25 %</td>
		<td width="" align="right" class="mycell">20.00</td>
		<td width="" align="right" class="mycell">19.60</td>
		</tr>
			
		
	<tr>
		<td width="" class="mycell">59</td>
		<td width="" nowrap="nowrap" class="mycell"  onMouseOver="this.style.color='red';this.style.cursor='hand';" onMouseOut="this.style.color='Black';this.style.cursor='text/edit';" ><strong>Williamson Tea</strong></td>
		<td width="" align="right" class="mycell">300.00</td>
		<td width="" align="right" class="style2">308.00</td>
		<td width="0" align="center" class="mycell"><strong><span stlye="color:#990100;">8.00</span></strong></td>
		
		<td width="0" align="center" class="mycell"><img src="images/up.jpg" height="15" width="10"/></td>
		
		
		
		
		
		<td width="" align="center" nowrap="nowrap" class="mycell">2.67 %</td>
		<td width="" align="right" class="mycell">310.00</td>
		<td width="" align="right" class="mycell">300.00</td>
		</tr>
	
</table>

</div>
</body>
</html>
