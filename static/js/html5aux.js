function showDiv(id) {
    if (document.getElementById('welcomeDiv'+id).style.display == "block"){
		   document.getElementById('welcomeDiv'+id).style.display = "none";
	} else {
		document.getElementById('welcomeDiv'+id).style.display = "block";
	}
}