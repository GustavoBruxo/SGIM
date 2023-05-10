$(document).ready(function(){
    var categoria = document.getElementById('categoria');
    categoria.addEventListener('change', function(){
        if (categoria.value == '8') {
            document.getElementById("opcoes1").style.display = "block";
        } else {
            document.getElementById("opcoes1").style.display = "none";
        }
    });

    var pessoa = document.getElementById('pessoa')
    pessoa.addEventListener('change', function(){
        var cpfcnpj = $("#cpfcnpj")
        cpfcnpj.val('');
        if (pessoa.value == 'Física'){
            $('#cpfcnpj').mask('000.000.000-00', {reverse: true})
        } else if (pessoa.value == 'Jurídica'){
            $('#cpfcnpj').mask('00.000.000/0000-00', {reverse: true});
        }
    });

    $('#cep').mask('00000-000');
    $('#telefone').mask('(00) 00000-0000');

    function limpa_formulário_cep() {
        // Limpa valores do formulário de cep.
        $("#logradouro").val("");
        $("#bairro").val("");
        $("#cidade").val("");
        $("#estado").val("");
    };
    
    //Quando o campo cep perde o foco.
    $("#cep").blur(function() {
        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');
        //Verifica se campo cep possui valor informado.
        if (cep != "") {
            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;
            //Valida o formato do CEP.
            if(validacep.test(cep)) {
                //Preenche os campos com "..." enquanto consulta webservice.
                $("#logradouro").val("...");
                $("#bairro").val("...");
                $("#cidade").val("...");
                $("#estado").val("...");
                //Consulta o webservice viacep.com.br/
                $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#logradouro").val(dados.logradouro);
                        $("#bairro").val(dados.bairro);
                        $("#cidade").val(dados.localidade);
                        $("#estado").val(dados.uf);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    });

    $('.dropify').dropify({
        // default file for the file input
        defaultFile: '',

        // max file size allowed
        maxFileSize: 0,

        // custom messages
        messages: {
            'default': 'Arraste e solte um arquivo aqui ou clique',
            'replace': 'Arraste e solte ou clique para substituir',
            'remove':  'Apagar',
            'error':   'Desculpe, este arquivo é muito grande'
        },
    });

  });