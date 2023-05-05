//
//app.js
//
var company = document.getElementById("divCompany");
var admin = document.getElementById("divAdmin");
var user = document.getElementById("usertype");
user.oninput = function () {
	var cv = user.value;
	if(cv == "Admin"){
		admin.style.display = "block";
	}
	else{
		admin.style.display = "none";
	}
	if(cv == "Company"){
		company.style.display = "block";
	}
	else{
		company.style.display = "none";
	}
};
