$(document).ready(function () {
    var table = $('#clientes').DataTable({
        responsive: true, // Datatable Responsivo
        dom: '<"top"l>frtip<"bottom"B>', // Posição dos itens da Datatable
        buttons: [ // Botões
            {
                extend: 'excelHtml5',
                className: 'btn btn-success',
            },
            {
                extend: 'pdfHtml5',
                className: 'btn btn-danger',
            },],
        aaSorting: [], // Não vai organizar de forma automatica, mas sim pelo backend
        pageLength: 30, // Nº de itens por página
        columnDefs: [{
            targets: [0, 1, 7, 8],
            orderable: false
        }], // Colunas sem a opção de ordenação
        stateSave: true, 
        language: {
            emptyTable: "Nenhum registro encontrado",
            info: "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            infoFiltered: "(Filtrados de _MAX_ registros)",
            infoThousands: ".",
            loadingRecords: "Carregando...",
            zeroRecords: "Nenhum registro encontrado",
            search: "Pesquisar",
            processing: "Carregando...",
            searchPlaceholder: "Buscar registros",
            paginate: {
                next: "Próximo",
                previous: "Anterior",
                first: "Primeiro",
                last: "Último"
            },
            lengthMenu: "Exibir _MENU_ resultados por página",
            infoEmpty: "Mostrando 0 até 0 de 0 registro(s)"
        },
    });

    $('#search').keyup(function () {
        table.search($(this).val()).draw();
    });
});