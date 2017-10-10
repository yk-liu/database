Your arguments values are
<?php
$arguments  = $_GET["arguments"];
echo $arguments;
?>

and I ran a python script, the result is 
<?php 
$arguments  = $_GET["arguments"];
$result = exec("python3 echo.py $arguments",$output);
//$newresult = str_replace("\n","<br>",$result);
//echo $newresult;

//echo '<pre>';print_r($output);echo '</pre>';

//echo "\nline1: " . $output[0] . "\nline2: " . $output[1] . "\nline3: " . $output[2] ;


foreach($output as $line) {
    echo "$line <br>";
}



//for ($x = 0; $x <=10 ; $x++) {
//    echo "The line number is : $x <br>". $output[$x]. "<br>";
//}

//echo json_encode($output);
//echo "<pre>$result</pre>";

// foreach($result) {
//    echo $result[1], '<br />';
//}

?>
