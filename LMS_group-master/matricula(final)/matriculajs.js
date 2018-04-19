console.log("javascript carregado!!")

//Validação na submissão
document.getElementById("formulario").onsubmit = function(event){
    var aprovado = 0;
    var cancelado = 0;
    var valueCampo = document.getElementsByClassName("check");
    if (valueCampo.length < 40 ){
        alert("O mínimo permitido é de 20 alunos");
        return false;
    }else if(valueCampo.length > 120){
        alert("O máximo permitido é de 60 alunos");
    }else {
        for (var i = 0; i< valueCampo.length ; i += 2){
            if (valueCampo[i].checked == false && valueCampo[i+1].checked == false ){
                alert("Todos os campos devem ser preenchidos");
                return false;
            }
        }
        for (var i = 0; i < valueCampo.length; i++){
            if(valueCampo[i].checked == true ){
                if(valueCampo[i].value == "aprovado"){
                    aprovado++;
                }else{
                    cancelado++;
                }
            }
        }
        alert("Aprovados: "+aprovado+"\nCancelados: "+cancelado);
        return window.confirm("Deseja enviar o formulário ?");
    }
}



