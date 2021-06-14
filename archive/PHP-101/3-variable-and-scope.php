<!-- Variable and Scope -->

<!DOCTYPE html>
<html>
<body>
<?php
	// global scope
	$text = "Incredible Dev!";
	$number = 7;
	$float_number = 3.1415;
	echo $text . "<br>";
	echo $number . "<br>";
	echo $float_number . "<br>";

	function addNumbers() {
		// local scope
		$sum = 0;
    	// access to global-scoped variables
		global $number, $float_number;
		$sum = $number + $float_number;
		echo $sum; // outputs 10.1415
	}
	addNumbers();
?>
</body>
</html>