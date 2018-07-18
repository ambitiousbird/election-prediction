
<html>
  <head>
	<title>WHO WILL WIN?</title>
    <style>
      html, body, #map { margin: 0; padding: 0; height: 100%; }
    </style>
    <script
      src="https://maps.googleapis.com/maps/api/js?libraries=visualization">
    </script>
    <script type="text/javascript">
40.721878, -98.970321
var map;
function initMap() {
	
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 40.721878, lng: -98.970321},
    zoom: 4
  });
  <?php
			$servername = "cis-linux2.temple.edu";
			$username = "tuf68743";
			$password = "ohogoofu";
			$dname="FA15_5015_tuf68743";

			// Create connection
			$conn = new mysqli($servername, $username, $password,$dname);

			// Check connection
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			} 
			//echo "Connected successfully ";
			//
			$sql = "SELECT * FROM Tweets";
			$result = $conn->query($sql);
			if ($result->num_rows > 0) {
				// output data of each row
				while($row = $result->fetch_assoc()) {
					//echo "ID: " . $row["ID"]."[lag,long] " . "[".$row["Lat"].",".$row["Lon"]."]"."<br>";
					echo '  var myLatlng1 = new google.maps.LatLng('.$row["Lat"].', '.$row["Lon"].');
					var marker1 = new google.maps.Marker({ 
					position: myLatlng1,
					//icon is to differentiate the color of the marker
					icon: \'http://maps.google.com/mapfiles/ms/icons/blue-dot.png\',
					animation: google.maps.Animation.DROP,
					map: map, 
					title:"'.$row["ID"].'"
					});';
				}
			} else {
				echo "0 results";
			}
			$sql = "SELECT * FROM Tweets2";
			$result1 = $conn->query($sql);
			if ($result1->num_rows > 0) {
				// output data of each row
				while($row = $result1->fetch_assoc()) {
					//echo "ID" . $row["ID"]."[lag,long] " . "[".$row["Lat"].",".$row["Lon"]."]"."<br>";
					echo '  var myLatlng1 = new google.maps.LatLng('.$row["Lat"].', '.$row["Lon"].');
					var marker1 = new google.maps.Marker({ 
					position: myLatlng1,
					//icon is to differentiate the color of the marker
					icon: \'http://maps.google.com/mapfiles/ms/icons/red-dot.png\',
					animation: google.maps.Animation.DROP,
					map: map, 
					title:"'.$row["ID"].'"
					});';
				}
			} else {
				echo "0 results";
			}	

		?>
  google.maps.event.addDomListener(window, 'load', initialize);
}

    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCw1el1ZgdpUFZiR3kTVtkpcl9uddHlYAs&callback=initMap"
        async defer>
	</script>
  </head>
  <body>
	<div> 
		<?php
		session_start();
		$username = $_GET['username'];
		$email = $_GET['email'];
		echo "Welcome!  ".$username. "!". " Your email address is ". $email.".";
		?>
		<p>Welcome to the final project! Bon vayage! </p>
	</div>
    <div id="map" style="height:480px;"></div>
    <div id="wordCloudDem">
	<h2> Democratic Candidate: </h2>
	<img src="democratic.png">
    </div>
    <div id="wordCloudRep">
	<h2> Republican Candidate: </h2>
	<img src="republican.png">
    </div>
    <div>
	<?php
		$servername = "cis-linux2.temple.edu";
		$username = "tuf68743";
		$password = "ohogoofu";		
		$dname="FA15_5015_tuf68743";

		// Create connection
		$conn = new mysqli($servername, $username, $password,$dname);

		// Check connection
		if ($conn->connect_error) {
			die("Connection failed: " . $conn->connect_error);
		} 
		echo "Connected successfully ";
		//
		$sql = "SELECT * FROM Tweets2";
		$result = $conn->query($sql);
		if ($result->num_rows > 0) {
			// output data of each row
			while($row = $result->fetch_assoc()) {
				echo "ID: " . $row["ID"]."[lat,lon] " . "[".$row["Lat"].",".$row["Lon"]."]"."<br>";
			}
		} else {
			echo "0 results";
		}	

	?>
     </div>
  </body>
</html>
