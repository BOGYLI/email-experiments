<?php
// the message
$msg = "Hallo!\nDies ist eine Test!";

// send email
mail("
    fakemailreceiver.pension987@passinbox.com",
    "Karlo ist da.",
    $msg,
    "From: Mickey Mouse<service@andrescherl.de>");
?>