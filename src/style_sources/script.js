document.getElementById("creditForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const dealID = document.getElementById("dealID").value;
    const dealIDError = document.getElementById("dealIDError");
    let isValid = true;

    const dealDate = document.getElementById("dealDate").value;
    const dateError = document.getElementById("dateError");

    const datePattern = /^(0[1-9]|1[0-2])\.\d{4}$/;

    //dealID validation
    if(typeof(dealID) != 'number'){
        dealIDError.style.display = "block";
        isValid = false;
    } else{
        dealIDError.style.display = "none";
    }

    //dealDate validation
    if (!datePattern.test(dealDate)) {
        dateError.style.display = "block";
        isValid = false;
    } else {
        dateError.style.display = "none";
    }

    if (isValid){
        try{
            return true;
        }catch(error=>{
            alert("Произошла ошибка при отправке данных");
        })
    }
    return false;
});