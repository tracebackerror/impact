<?php

$EmailTo = "shilonmahadi7@gmail.com";
$Subject = "New Message Received";

$errorMSG = "";
$name = $email = $message = $phone = $subjects = null;

// NAME
if(isset($_POST["name"])) {
    if (empty($_POST["name"])) {
    	$errorMSG .= "Name is required ";
    } else {
    	$name = $_POST["name"];
    }
}

// EMAIL
if(isset($_POST["email"])) {
    if (empty($_POST["email"])) {
	    $errorMSG .= "Email is required ";
    } else {
    	$email = $_POST["email"];
    }   
}

// phone

if(isset($_POST["phone"])) {
    if (empty($_POST["phone"])) {
    	$errorMSG .= "phone is required ";
    } else {
    	$phone = $_POST["phone"];
    
    }
}

// subjects

if(isset($_POST["subjects"])) {
    if (empty($_POST["subjects"])) {
    	$errorMSG .= "subjects is required ";
    } else {
    	$subjects = $_POST["subjects"];
    
    }
}

// MESSAGE

if(isset($_POST["message"])) {
    if (empty($_POST["message"])) {
    	$errorMSG .= "Message is required ";
    } else {
    	$message = $_POST["message"];
    
    }
}

// Prepare Email Body Text
$Body = null;

if($name) {
    $Body .= "<p><b>Name:</b> {$name}</p>";
}
if($email) {
    $Body .= "<p><b>Email:</b> {$email}</p>";
}
if($phone) {
    $Body .= "<p><b>phone:</b> {$phone}</p>";
}
if($subjects) {
    $Body .= "<p><b>subjects:</b> {$subjects}</p>";
}
if($message) {
    $Body .= "<p><b>Message:</b> {$message}</p>";
}

// Send Email
$headers = 'MIME-Version: 1.0' . "\r\n";
$headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
$headers .= 'From:  ' . $name . ' <' . $email .'>' . " \r\n" .
			'Reply-To: '.  $fromEmail . "\r\n" .
			'X-Mailer: PHP/' . phpversion();

if($name || $email || $phone || $subjects || $message ){
	$success = mail($EmailTo, $Subject, $Body, $headers );
} else {
	$success = false;
}


if ($success && $errorMSG == "") {
   echo "success";
} else {
	if($errorMSG == ""){
		echo "Something went wrong :(";
	} else {
		echo $errorMSG;
	}
}